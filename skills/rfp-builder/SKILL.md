---
name: rfp-builder
description: "Create Request for Proposals with requirements specifications, evaluation criteria, scoring rubrics, timelines, and compliance requirements"
---

# RFP Builder

## Overview

Design comprehensive Requests for Proposals (RFPs) that clearly specify requirements, establish fair evaluation processes, and attract qualified vendor responses. Well-crafted RFPs reduce confusion, streamline vendor comparison, and ensure compliance with procurement standards.

## RFP Structure

### 1. Executive Summary
- **Organization Overview**: Company, size, mission, relevant context
- **Procurement Objective**: What are we buying and why?
- **Key Dates**: Release date, deadline, evaluation timeline, vendor meeting date
- **Contact Information**: RFP coordinator name, email, phone
- **Bid Instructions**: Format requirements, submission method

### 2. Background & Context
- **Business Context**: Why are we buying this? What problems are we solving?
- **Current State**: What's in place today? What are the gaps?
- **Strategic Alignment**: How does this support company objectives?
- **Success Vision**: What does success look like 12-24 months post-implementation?

### 3. Detailed Requirements Specification

**Mandatory Requirements** (Yes/No; non-negotiable):
```
Req ID | Category | Requirement | Criticality | Evaluation
-------|----------|-------------|-------------|----------
F-001 | Functionality | Support 100K users | MANDATORY | Does product support this scale?
F-002 | Functionality | Real-time integration with Salesforce | MANDATORY | What's latency? Update frequency?
F-003 | Security | SOC 2 Type II certified | MANDATORY | Provide recent audit report
F-004 | Uptime | 99.9% uptime SLA | MANDATORY | What's the penalty for non-compliance?
```

**Desired Requirements** (Weighted for evaluation):
```
Req ID | Category | Requirement | Weight | Priority
-------|----------|-------------|--------|----------
D-001 | Performance | Sub-second query response | 15% | HIGH
D-002 | UX | Intuitive mobile interface | 10% | MEDIUM
D-003 | Analytics | Advanced reporting dashboards | 10% | MEDIUM
D-004 | Support | 24/7 phone support | 5% | LOW
```

**Technical Specifications**:
- Architecture requirements
- API specifications
- Data format requirements
- Integration endpoints
- Performance benchmarks
- Security standards

### 4. Evaluation Criteria & Scoring

**Scoring Rubric** (example with 100-point scale):

| Criterion | Weight | Points | Excellent (5) | Good (3) | Acceptable (1) | Unacceptable (0) |
|-----------|--------|--------|---------------|---------|----------------|-----------------|
| **Functionality (30%)** | 30 | 30 | Exceeds all requirements; advanced features | Meets core requirements; minor gaps | Meets 70% of requirements | Fails to meet key requirements |
| **Implementation Timeline (15%)** | 15 | 15 | Ready in 4 weeks; proven rollout | Ready in 8 weeks; standard approach | Ready in 12 weeks; custom work | >12 weeks or uncertain |
| **Pricing (20%)** | 20 | 20 | <$100K total; clear cost structure | $100-150K; transparent pricing | $150-200K; some unclear costs | >$200K or hidden fees |
| **Security & Compliance (20%)** | 20 | 20 | SOC 2 Type II + industry certifications | SOC 2 Type II compliant | Security audit in progress | No security certifications |
| **Support & SLA (10%)** | 10 | 10 | 24/7 phone + 99.99% uptime SLA | Business hours support + 99.9% SLA | Email support + 99% SLA | Limited support; no SLA |
| **References (5%)** | 5 | 5 | 5+ recent enterprise refs in our industry | 3+ relevant enterprise refs | Some references; smaller companies | No references or negative feedback |

**Scoring Method**:
- Each evaluator independently scores (1-5 per criterion)
- Average scores across evaluators
- Multiply by weight percentage
- Total possible: 100 points
- Minimum threshold for consideration: 70 points

### 5. Service Level Agreement Template

```
Service Availability:
- Uptime SLA: 99.9% (allows 43 minutes/month downtime)
- Availability window: 24/7/365
- Credit: 1% per 0.1% below target (max 10% monthly credits)

Performance Guarantees:
- API response time: <200ms (p95)
- Data sync latency: <15 minutes
- Report generation: <5 minutes for standard reports

Support:
- Emergency (P1): 15-minute response; 4-hour resolution
- High (P2): 1-hour response; 8-hour resolution
- Medium (P3): 4-hour response; 1-business-day resolution
- Low (P4): Next business day response; 5-business-day resolution

Escalation:
- P1 after 2 hours: Escalate to VP Engineering
- P1 after 4 hours: Escalate to VP Customer Success

Penalties:
- SLA breach: Monthly credit to next invoice
- Repeated breaches (>2/quarter): Right to terminate with 30 days notice
```

### 6. Pricing & Terms

**Pricing Format** (be specific about what's included):

```
Category | Year 1 | Year 2 | Year 3 | Notes
---------|--------|--------|--------|-------
Software License | $50,000 | $55,000 | $60,500 | 5% annual increase max
Implementation | $30,000 | - | - | Professional services
Training (4 days) | $10,000 | - | - | On-site training
Support (24/7) | $25,000 | $26,250 | $27,563 | Included in license
TOTAL YEAR 1 | $115,000 | $81,250 | $88,063 |
3-YEAR TOTAL | | | | $284,313
```

**Payment Terms** (specify expectations):
- 50% on signature; 50% on go-live
- Net 30 for support invoices
- No price increases >5% annually without written approval

### 7. Legal & Compliance Requirements

**Data Security**:
- GDPR-compliant (if applicable)
- SOC 2 Type II certification required
- Data stored in [country/region]
- Encryption at rest and in transit (AES-256 minimum)
- Annual security audit required

**Intellectual Property**:
- Who owns custom code/configurations?
- Can we use vendor logo/case study?
- What happens to our data if relationship ends?

**Termination Clauses**:
- Termination for convenience: [period] days notice
- Data migration assistance: [details]
- Post-termination support: [duration]

**Insurance**:
- General liability: $2M minimum
- Professional liability: $1M minimum
- Evidence of insurance upon contract signing

### 8. Timeline & Key Dates

```
Date | Event | Details
-----|-------|--------
Feb 28 | RFP Release | Posted publicly; vendor portal opens
Mar 7 | Vendor Q&A Deadline | Questions must be submitted by 5 PM ET
Mar 10 | Vendor Response Released | Answers shared with all vendors
Mar 20 | Proposal Deadline | Final proposals due; no exceptions
Mar 25-29 | Initial Evaluation | First-pass scoring; vendor short-list selected
Apr 2-5 | Demos | Shortlisted vendors present demos (1 hour each)
Apr 10 | Final Scoring | Evaluation committee final scoring
Apr 12 | Reference Calls | Calls with top 2-3 vendors' references
Apr 15 | Negotiation | Begin contract negotiation with top vendor
Apr 30 | Contract Signed | Expected signature date
May 5 | Project Kickoff | Implementation begins
```

### 9. Proposal Submission Instructions

**Format Requirements**:
- PDF format; single document
- Maximum 50 pages (excluding appendices)
- Use standard fonts (Arial, Times New Roman, 11pt+)
- Executive summary on first page
- Numbered sections matching RFP structure
- Table of contents with page numbers

**Required Sections**:
1. Executive Summary
2. Company Overview & Qualifications
3. Solution Description & Approach
4. Technical Architecture & Integration
5. Implementation Plan & Timeline
6. Pricing & Terms
7. References (minimum 3)
8. Appendices (case studies, data sheets)

**Submission Method**:
- Email to [RFP coordinator] with subject line: "[Company Name] - [Product Name] Proposal"
- File naming: [Company]_[Product]_Proposal_[Date].pdf
- Deadline: March 20, 2024, 5:00 PM ET (no exceptions)

### 10. Vendor Qualification Questions

**Organization**:
- How long have you been in business?
- What's your financial stability? (Provide latest financial statements)
- Who's your management team? (Org chart, bios)

**Product Maturity**:
- How many customers use this product?
- What's your user base growth rate?
- How long has the current version been in production?

**Experience**:
- How many customers similar to ours do you have?
- Can you provide 3 references from [our industry]?
- What's your average customer tenure?

**Support & Success**:
- What's your customer success model?
- How many support staff per 1000 customers?
- What's your NPS score? (Provide recent survey)

## Evaluation Committee

**Roles**:
- **Committee Chair**: [Name, Title] - Oversees process
- **Subject Matter Experts**: [2-3 technical leads] - Rate functionality
- **Business Owner**: [Finance/Operations] - Rates fit and value
- **Procurement**: [Name] - Rates legal/compliance

**Committee Agreement**:
All evaluators agree to:
- Score independently before discussion
- Avoid conflicts of interest
- Keep evaluations confidential
- Evaluate based on criteria only (not personal preferences)

## Communication with Vendors

**Vendor Briefing** (optional):
- 30-minute call for all vendors
- Overview of requirements
- Q&A opportunity
- No competitive intelligence sharing

**RFP Q&A Process**:
- Questions submitted in writing
- Answers shared with all vendors equally
- No side conversations about requirements

**Post-RFP Communication**:
- Notify all vendors of shortlist decision
- Provide feedback: "We chose another vendor because..."
- Maintain professional relationships (may re-bid in future)

## Negotiation Strategy

**Post-Award**:
Before signing contract, negotiate:
- Specific implementation timeline
- Data migration plan
- Training schedule and resource commitment
- Support escalation procedures
- Pricing lock-in period
- Renewal terms and discounts

**Red Flags During Negotiation**:
- Vendor reluctant to commit to SLAs
- Significant scope changes not in proposal
- Hidden implementation costs surfacing
- Key personnel listed in proposal unavailable
- References no longer willing to talk to vendor

---

**Use this skill to**: Attract qualified vendors, ensure fair evaluation, establish clear expectations, and negotiate contracts with confidence.
