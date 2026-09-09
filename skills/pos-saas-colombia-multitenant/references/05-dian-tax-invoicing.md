# Facturación Electrónica DIAN (Documento tributario, no confundir con billing SaaS)

⚠️ **No confundir dos flujos de "facturación" distintos que coexisten en este sistema:**

| | Facturación de suscripción SaaS | Facturación DIAN |
|---|---|---|
| Quién le cobra a quién | Tu plataforma le cobra al tenant | El tenant (comerciante) le factura a su propio cliente final |
| Documento | `subscriptions`, `payment_transactions` | `tax_invoices` |
| Pasarela | Wompi, ePayco, PSE, Nequi (ver `03-payment-gateways-colombia.md`) | Proveedor tecnológico DIAN (Alanube, MATIAS, Factus, NortServer, o software propio) |
| Obligatoriedad | Contractual (tu negocio) | Legal — Art. 615 del Estatuto Tributario y Resolución 000042 de 2020 |

Este documento cubre **solo** la segunda: cada venta que un cajero del tenant registra en `sales` debe generar un documento tributario electrónico y transmitirse a la DIAN en tiempo real.

## 1. Por qué el Facturador Gratuito de la DIAN NO sirve aquí

El Facturador Gratuito de la DIAN (accesible desde MUISCA) no expone una API — es un formulario web para llenar manualmente, pensado para independientes de bajo volumen. Un POS SaaS necesita generar el documento automáticamente en el momento de cada venta, sin intervención humana. Por eso este patrón usa un **proveedor tecnológico privado autorizado ante la DIAN**, que sí ofrece API REST.

## 2. Regla de negocio: qué documento generar según el monto

- Ventas **hasta 5 UVT** ($261.870 COP en 2026): Documento Equivalente Electrónico POS (DEE POS) — versión simplificada del tiquete, no da derecho a costos ni deducciones para quien lo recibe.
- Ventas **superiores a 5 UVT**: Factura electrónica de venta completa, con descripción de bienes/servicios, impuestos discriminados (IVA, INC), firma digital, CUFE y código QR.

```typescript
function determineDocumentType(totalCOP: number): 'dee_pos' | 'factura_electronica' {
  const UVT_2026 = 52374; // valor UVT vigente — actualizar cada año fiscal
  const threshold = UVT_2026 * 5;
  return totalCOP <= threshold ? 'dee_pos' : 'factura_electronica';
}
```

**Nota de mantenimiento**: el valor de la UVT cambia cada año (lo fija la DIAN). No hardcodear el número sin un mecanismo de actualización — es un valor de configuración, no una constante de código.

## 3. Abstracción de proveedor (mismo patrón que las pasarelas de pago)

```typescript
// dian-provider.interface.ts
export interface DianInvoiceRequest {
  tenantId: string;
  saleId: string;
  documentType: 'dee_pos' | 'factura_electronica';
  seller: { nit: string; name: string };
  buyer?: { idType: string; idNumber: string; email?: string }; // opcional en DEE POS
  items: Array<{ description: string; quantity: number; unitPrice: number; taxRate: number }>;
  totalCOP: number;
}

export interface DianInvoiceResponse {
  cufe: string;
  xmlUrl: string;
  pdfUrl: string;
  qrCode: string;
  status: 'issued' | 'rejected';
  rawResponse: unknown;
}

export interface DianProviderAdapter {
  issueInvoice(request: DianInvoiceRequest): Promise<DianInvoiceResponse>;
}
```

Cada proveedor (`AlanubeAdapter`, `MatiasAdapter`, `FactusAdapter`, `PropioAdapter`) implementa esta interfaz. El servicio de ventas no conoce el proveedor concreto, solo `DianProviderAdapter` — así cambiar de proveedor es una configuración, no una reescritura.

## 4. Flujo end-to-end en el momento de la venta

```
Cajero cierra la venta (INSERT en sales + sale_items)
        │
        ▼
Determinar tipo de documento según monto (5 UVT)
        │
        ▼
Encolar job "issue-tax-invoice" con tenantId + saleId
  (asíncrono: NO bloquear el cierre de caja esperando a la DIAN)
        │
        ▼
Worker llama a DianProviderAdapter.issueInvoice(...)
        │
        ├── issued → INSERT en tax_invoices (cufe, xml_url, pdf_url, qr_code, status='issued')
        │            → mostrar QR/CUFE en el recibo impreso o digital
        │
        └── rejected → INSERT en tax_invoices (status='rejected', provider_response)
                     → alertar al tenant (la venta ya se registró, pero el
                       documento tributario falló y requiere reintento o
                       corrección manual — esto NO debe pasar silencioso)
```

**Por qué asíncrono**: si el proveedor DIAN tiene latencia o cae, no puede bloquear el cierre de caja de un cajero con un cliente esperando. La venta se registra siempre; el documento tributario se emite en segundo plano con reintentos.

## 5. Reintentos y contingencia

- Si el proveedor tecnológico no responde, reintentar con backoff (ej. 3 intentos en 5 minutos).
- Si tras los reintentos sigue fallando, la venta queda con `tax_invoices.status = 'rejected'` y debe aparecer en un panel de "documentos pendientes" del tenant — la ley permite contingencia tecnológica comprobada, pero exige regularizar dentro de un plazo corto una vez resuelto el problema técnico.
- No se debe rehacer la venta ni duplicar el `sale_id` al reintentar — el reintento reutiliza los mismos datos de la venta original.

## 6. Prerrequisitos por tenant (no técnicos, pero bloquean el flujo)

Antes de que un tenant pueda emitir su primer documento, necesita:

1. RUT actualizado con responsabilidad de facturación electrónica y actividad económica (código CIIU) correcta.
2. Certificado digital de firma electrónica vigente (normalmente lo gestiona el proveedor tecnológico elegido).
3. Resolución de numeración DIAN para su rango de documentos (también gestionada por la mayoría de proveedores en el onboarding).

El sistema debe bloquear la emisión de documentos para un tenant que no haya completado este onboarding fiscal — es responsabilidad del tenant, no de la plataforma, pero la plataforma debe detectarlo y no fallar en silencio.

## 7. Decisión pendiente

Cuál proveedor tecnológico específico (Alanube, MATIAS API, Factus, NortServer, u homologación propia bajo Resolución 000042) determina: costo por documento vs. costo fijo mensual, SLA de disponibilidad, y si necesitas certificado digital propio o el proveedor lo incluye. No asumir uno sin cotizar — el rango visto en el mercado va desde modelos por consumo (BaaS) hasta planes fijos mensuales con volumen incluido.
