#!/usr/bin/env node
/**
 * Valida findings.json contra report-schema.json.
 * Usage: node validate-findings.cjs <findings.json>
 *
 * Zero dependências. Exit 0 = success, exit 1 = falha.
 */
const fs = require("fs");
const path = require("path");

const file = process.argv[2];
if (!file) {
  console.error("Usage: node validate-findings.cjs <findings.json>");
  process.exit(1);
}

const schemaPath = path.join(__dirname, "..", "references", "report-schema.json");
let itemSchema;
try {
  const doc = JSON.parse(fs.readFileSync(schemaPath, "utf8"));
  itemSchema = doc.output_schema;
  if (!itemSchema) throw new Error('report-schema.json missing "output_schema"');
} catch (e) {
  console.error(`Failed to load schema from ${schemaPath}:`, e.message);
  process.exit(1);
}

let findings;
try {
  findings = JSON.parse(fs.readFileSync(file, "utf8"));
} catch (e) {
  console.error("Failed to parse JSON:", e.message);
  process.exit(1);
}

if (!Array.isArray(findings)) {
  console.error("findings.json must be an array");
  process.exit(1);
}

function typeOf(v) {
  if (Array.isArray(v)) return "array";
  if (v === null) return "null";
  return typeof v;
}

function findDiscriminator(schema) {
  if (!schema.properties) return null;
  for (const [key, sub] of Object.entries(schema.properties)) {
    if (sub && Object.prototype.hasOwnProperty.call(sub, "const")) {
      return { key, value: sub.const };
    }
  }
  return null;
}

function validate(value, schema, p, errors) {
  if (schema.oneOf) {
    for (const branch of schema.oneOf) {
      const disc = findDiscriminator(branch);
      if (disc && value && typeof value === "object" && value[disc.key] === disc.value) {
        validate(value, branch, p, errors);
        return;
      }
    }
    const discs = schema.oneOf.map(findDiscriminator).filter(Boolean);
    if (discs.length === schema.oneOf.length && value && typeof value === "object") {
      const key = discs[0].key;
      const allowed = discs.map((d) => JSON.stringify(d.value)).join(", ");
      errors.push(`${p}: "${key}" must be one of ${allowed}, got ${JSON.stringify(value[key])}`);
      return;
    }
    errors.push(`${p}: does not match exactly one of the allowed schemas`);
    return;
  }

  if (Object.prototype.hasOwnProperty.call(schema, "const") && value !== schema.const) {
    errors.push(`${p}: must equal ${JSON.stringify(schema.const)}, got ${JSON.stringify(value)}`);
  }
  if (schema.enum && !schema.enum.includes(value)) {
    errors.push(`${p}: invalid value ${JSON.stringify(value)} (expected one of ${schema.enum.join(", ")})`);
  }

  switch (schema.type) {
    case "object": {
      if (typeOf(value) !== "object") { errors.push(`${p}: expected object, got ${typeOf(value)}`); return; }
      for (const req of schema.required || []) {
        if (!(req in value)) errors.push(`${p}: missing required field "${req}"`);
      }
      for (const key of Object.keys(value)) {
        if (schema.properties && key in schema.properties) {
          validate(value[key], schema.properties[key], `${p}.${key}`, errors);
        } else if (schema.additionalProperties === false) {
          errors.push(`${p}: unexpected field "${key}"`);
        }
      }
      break;
    }
    case "array": {
      if (typeOf(value) !== "array") { errors.push(`${p}: expected array, got ${typeOf(value)}`); return; }
      if (typeof schema.minItems === "number" && value.length < schema.minItems) {
        errors.push(`${p}: must have at least ${schema.minItems} item(s), got ${value.length}`);
      }
      if (schema.items) {
        value.forEach((el, i) => validate(el, schema.items, `${p}[${i}]`, errors));
      }
      break;
    }
    case "integer": {
      if (typeOf(value) !== "number" || !Number.isInteger(value)) {
        errors.push(`${p}: expected integer, got ${typeOf(value)}`);
      }
      break;
    }
    case "string": {
      if (typeOf(value) !== "string") errors.push(`${p}: expected string, got ${typeOf(value)}`);
      break;
    }
  }
}

let errorCount = 0;
findings.forEach((f, i) => {
  const label = `[${i}] ${(f && (f.title || f.reason)) || "(untitled)"}`;
  console.log(`Checking ${label}`);
  const errs = [];
  validate(f, itemSchema, `[${i}]`, errs);

  // Semantic: confirmed trace must start at entrypoint and end at sink
  if (f && f.verdict === "confirmed" && Array.isArray(f.trace) && f.trace.length > 0) {
    if (f.trace[0] && f.trace[0].kind !== "entrypoint") {
      errs.push(`[${i}].trace[0].kind must be "entrypoint", got ${JSON.stringify(f.trace[0].kind)}`);
    }
    const last = f.trace.length - 1;
    if (f.trace[last] && f.trace[last].kind !== "sink") {
      errs.push(`[${i}].trace[${last}].kind must be "sink", got ${JSON.stringify(f.trace[last].kind)}`);
    }
  }

  for (const msg of errs) console.error("  ERROR:", msg);
  errorCount += errs.length;
});

console.log();
if (errorCount === 0) {
  console.log(`PASS: ${findings.length} findings valid`);
} else {
  console.error(`FAIL: ${errorCount} error(s) across ${findings.length} findings`);
  process.exit(1);
}
