---
name: vendor-evaluation
description: "Evaluate vendors with comparison matrices, TCO analysis, risk assessment, reference check templates, and negotiation strategies"
---

# Vendor Evaluation

## Overview

Systematically evaluate vendor options using quantitative and qualitative criteria. Comprehensive vendor evaluation combines total cost of ownership (TCO) analysis, risk assessment, reference verification, and strategic fit to select the best long-term partner.

## Vendor Comparison Matrix

**Basic Comparison** (3 vendors):

| Capability | Requirements | Vendor A | Vendor B | Vendor C |
|-----------|--------------|----------|----------|----------|
| **Functionality** | | | | |
| Real-time integrations | Mandatory | Yes | Yes | Yes |
| API rate limits | 1000 req/sec | 1000 | 2000 | 500 |
| Customization support | Available | Limited | Extensive | Standard |
| **Performance** | | | | |
| Response time (p95) | <200ms | 150ms | 180ms | 250ms |
| Uptime SLA | 99.9% | 99.95% | 99.9% | 99.5% |
| Data latency | <15 min | 5 min | 10 min | 30 min |
| **Security** | | | | |
| SOC 2 Type II | Mandatory | Yes | Yes | No |
| Data encryption | AES-256 | Yes | Yes | Yes |
| GDPR certified | Required | Yes | Yes | In progress |
| **Support** | | | | |
| 24/7 phone support | Desired | Yes | Yes | No |
| Avg response time (P1) | <30 min | 15 min | 30 min | 2 hours |
| Customer success manager | Yes | Included | Included | Extra cost |
| **Pricing** | | | | |
| Year 1 total cost | Benchmark | $115K | $95K | $80K |
| Implementation cost | Fixed | $30K | $25K | $40K |
| Hidden costs | Identify | Minimal | Minimal | Training extra |
| 3-year TCO | Compare | $285K | $270K | $290K |

## Total Cost of Ownership (TCO) Analysis

**Calculate True Cost Beyond License**:

```
VENDOR A - 3 YEAR TCO

ACQUISITION COSTS:
Software License (Year 1) | $50,000
Implementation Services | $30,000
Data Migration | $10,000
Initial Training (3 days) | $15,000
Subtotal | $105,000

ONGOING COSTS (Years 1-3):
Support & Maintenance (Y1) | $25,000
Support & Maintenance (Y2) | $26,250
Support & Maintenance (Y3) | $27,563
Annual Training Refresher (Y1) | $5,000
Annual Training Refresher (Y2) | $5,000
Annual Training Refresher (Y3) | $5,000
Infrastructure/Licenses (Y1) | $5,000
Infrastructure/Licenses (Y2) | $5,250
Infrastructure/Licenses (Y3) | $5,513
Software License Renewal (Y2) | $52,500
Software License Renewal (Y3) | $55,125
Subtotal | $217,388

HIDDEN COSTS:
Internal Project Management (500 hrs @ $100/hr) | $50,000
Vendor Management (100 hrs/year @ $100/hr) | $30,000
Process redesign (800 hrs @ $125/hr) | $100,000
Knowledge transfer (200 hrs @ $100/hr) | $20,000
System integration/customization (300 hrs @ $150/hr) | $45,000
Subtotal | $245,000

TOTAL 3-YEAR TCO | $567,388
```

**Cost Per User** (if 100 users):
- Year 1: $115,000 / 100 = $1,150/user
- 3 years: $567,388 / 100 = $5,674/user

**Comparison Across Vendors**:
- Vendor A: $567,388 (3-year TCO)
- Vendor B: $532,450 (3-year TCO)
- Vendor C: $625,000 (3-year TCO)

**Vendor B has lowest TCO** despite higher license cost; better support reduces internal costs.

## Risk Assessment Matrix

**Vendor Viability Risk**:

```
Risk Category | Vendor A | Vendor B | Vendor C | Mitigation
--------------|----------|----------|----------|----------
Financial Stability | Low | Medium | High | Request recent financials; check Dun & Bradstreet
Product Roadmap | Low | Low | Medium | Roadmap alignment with our priorities
Customer Concentration | Low | Medium | Low | Major customers (if <3, higher risk)
Key Personnel | Low | Medium | High | Ensure named resources committed to contracts
Technology Risk | Low | Low | Medium | Assess architecture scalability & maturity
Support Quality | Low | Low | High | Reference calls; ask about SLA breaches
Data Security | Low | Low | Medium | Require recent SOC 2 audit report
Integration Complexity | Low | Medium | Low | POC to verify integration capability
Switching Cost | Medium | High | Low | Cost to migrate if vendor fails
```

**Overall Risk Scoring** (1=Low, 3=Medium, 5=High):
- Vendor A: 8/50 (Low risk)
- Vendor B: 14/50 (Low-Medium risk)
- Vendor C: 24/50 (Medium risk)

## Reference Check Template

**Standard Reference Call** (30 minutes):

**Pre-Call**:
- Request 3 references from same industry
- Request 1-2 references with similar company size
- Request 1 reference from largest customer
- Ask vendor: "When was customer live? How long implemented?"

**Call Script**:

```
Hi [Name], thanks for taking time. I'm evaluating [Vendor] for [Use Case].
[Vendor] mentioned you're a customer; happy to verify that first?

1. RELATIONSHIP CONTEXT
- How long have you been a customer?
- What use cases do you primarily use it for?
- How many users do you have?
- How many internal resources did implementation require?

2. IMPLEMENTATION EXPERIENCE
- How long did implementation take? (vs. promised timeline)
- Were there unexpected costs or delays?
- How responsive was the vendor during implementation?
- Would you rate the data migration: Easy / Acceptable / Difficult?
- Did training resources match your needs?

3. PRODUCT FUNCTIONALITY
- Does it do what you need? Any significant gaps?
- Have you had to build custom integrations? How complex?
- Any performance issues or latency problems?
- How does it compare to competitors you evaluated?
- What features are you missing most?

4. VENDOR SUPPORT & SUCCESS
- How responsive is their support?
- Any SLA breaches you can recall?
- Do you have a dedicated customer success manager?
- Would you rate communication: Excellent / Good / Fair / Poor?
- Any unpleasant surprises (billing, features, behavior)?

5. RELIABILITY & OPERATIONS
- Have you experienced outages? How often? Duration?
- How's their security posture? Any concerns?
- Is data migration/export easy if you need to leave?
- How's their roadmap? Aligned with your needs?
- Are they financially stable in your view?

6. RECOMMENDATION
- Would you recommend them to a peer? Why/why not?
- What would you do differently if choosing again?
- Any advice for new customers?
- Can I reach out with follow-up questions?

7. CLOSING
- Thank you for your time and candor.
- I'll keep your feedback confidential.
```

**Reference Red Flags**:
- Hesitant to recommend
- Long implementation delays mentioned
- Unresolved technical issues
- Support unresponsiveness
- Cost overruns
- Data migration concerns
- Vendor not delivering roadmap commitments

## Weighted Scoring Model

**Establish Relative Importance** (weights sum to 100):

| Criterion | Weight | Vendor A | Vendor B | Vendor C |
|-----------|--------|----------|----------|----------|
| Functionality (does it work?) | 25% | 95 | 90 | 75 |
| Implementation Timeline | 15% | 90 | 70 | 50 |
| Total Cost of Ownership (TCO) | 20% | 85 | 90 | 65 |
| Security & Compliance | 15% | 95 | 90 | 70 |
| Support & Success | 15% | 80 | 85 | 60 |
| Risk Profile (lower is better) | 10% | 92 | 85 | 70 |

**Weighted Score**:
- Vendor A: (95×.25) + (90×.15) + (85×.20) + (95×.15) + (80×.15) + (92×.10) = 89.9
- Vendor B: (90×.25) + (70×.15) + (90×.20) + (90×.15) + (85×.15) + (85×.10) = 84.5
- Vendor C: (75×.25) + (50×.15) + (65×.20) + (70×.15) + (60×.15) + (70×.10) = 66.0

**Recommendation**: Vendor A (highest score), but Vendor B competitive on cost.

## Proof of Concept (POC)

**When to Require POC**:
- Complex technical integration
- Critical functionality concerns
- Unproven vendor or new product
- High switching costs if wrong choice
- Custom workflow requirements

**POC Scope**:
- **Objective**: Verify integration and core functionality
- **Duration**: 2-4 weeks
- **Cost**: [Usually vendor cost; sometimes shared]
- **Resources**: [# developers, data] needed for POC
- **Success Criteria**: [Specific technical outcomes]

**POC Plan Example**:
```
Week 1: Vendor sets up sandbox environment
        Our team imports sample data
        Basic user testing

Week 2: API integration testing
        Real-time sync validation
        Reporting accuracy verification

Week 3: Load testing (1000 users simulation)
        Edge case handling
        Security vulnerability scan

Week 4: Documentation review
        Go/No-Go decision
        Roadmap discussion if proceeding
```

**POC Decision Gate**:
- If POC successful: Proceed to contract
- If minor gaps: Document workarounds; proceed with conditions
- If significant gaps: Re-evaluate alternatives or custom development

## Vendor Negotiation Strategy

**Leverage Points** (use in negotiation):

1. **Competition**: "We're evaluating 3 vendors; your pricing needs to be competitive"
2. **Volume Commitment**: "If you can hit $90K, we'll commit 3-year contract"
3. **Long-term Partnership**: "We want a 3-year relationship with guaranteed renewal"
4. **Reference Status**: "We'll be your primary reference in our industry"
5. **Implementation Support**: "We have strong internal resources to minimize your services"

**Negotiation Playbook**:

```
ROUND 1 - OPENING (Initial proposals)
- Standard pricing: $115K
- Standard SLA: 99.9%
- Standard support: Business hours

ROUND 2 - INITIAL NEGOTIATION
- Your ask: "We need 24/7 support included for $100K"
- Vendor likely counter: "24/7 support costs extra; we can do $115K + $15K"
- Counter-counter: "If you include 24/7, we'll commit 3-year deal today ($95K/yr)"

ROUND 3 - VALUE-ADD NEGOTIATION
- Ask for free items: First year training, data migration, setup
- Vendor likely says: "No, those are paid services"
- Negotiate bundling: "Include all of those + 24/7 support for $110K/year"

ROUND 4 - FINAL OFFERS
- Get vendor's best offer in writing
- Make final counter-offer based on total value
- Establish walk-away price: If >$115K all-in, re-evaluate alternatives
```

**Non-Price Negotiables**:
- SLA penalties (require credits for breaches)
- Data export/migration assistance
- Transition support (if switching vendors)
- Key personnel commitment (named resources)
- Roadmap alignment (when will features appear?)
- Early termination clause (if not working)

## Final Selection Checklist

Before signing:
- [ ] Reference calls completed; no red flags
- [ ] POC (if needed) successful
- [ ] Weighted scoring complete; vendor selected
- [ ] TCO analysis presented to stakeholders
- [ ] Risk assessment acceptable; mitigations planned
- [ ] Negotiation complete; pricing/terms acceptable
- [ ] Contract reviewed by legal
- [ ] IT security review completed
- [ ] Executive approval obtained
- [ ] Implementation plan developed

---

**Use this skill to**: Select vendors systematically, negotiate favorable terms, minimize risk, and ensure long-term partnership success.
