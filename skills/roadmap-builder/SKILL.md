---
name: roadmap-builder
description: "Build product roadmaps with quarterly planning, feature prioritization, dependency mapping, and stakeholder alignment. Create actionable roadmaps that communicate strategy and guide execution."
---

# Roadmap Builder

## Overview
The Roadmap Builder skill enables product managers to create clear, actionable product roadmaps that communicate strategy, align stakeholders, and guide execution. It combines prioritization frameworks, timeline planning, and dependency mapping.

## When to Use This Skill
- Planning quarterly or annual product strategy
- Communicating product vision to stakeholders
- Prioritizing features and initiatives
- Managing dependencies across teams
- Aligning engineering, design, marketing resources
- Creating investor/executive presentations
- Managing stakeholder expectations

## Roadmap Planning Framework

### Roadmap Horizon Definitions

**Immediate (Current Quarter - 0-12 weeks)**
- Confirmed features with clear specifications
- Active development or about to start
- High confidence in timeline and scope
- Team committed to delivery
- Detail level: Very high (stories, tasks, owners)

**Near-term (Quarters 2-3 - 3-6 months)**
- Features with strong business case and customer demand
- Good understanding of requirements
- Medium confidence in timeline
- Provisional team allocation
- Detail level: High (features, rough effort estimates)

**Medium-term (Quarters 4-5 - 6-9 months)**
- Strategic initiatives aligned with roadmap
- Directional roadmap visibility
- Lower confidence due to market changes
- Broad theme-based planning
- Detail level: Medium (themes, business outcomes)

**Long-term (6-12+ months)**
- Vision and strategic directions
- Subject to significant change
- Focus on outcomes not features
- Annual planning context
- Detail level: Low (goals and themes)

### Roadmap Themes Framework

**Theme 1: Platform Performance**
- Objective: Improve system speed and reliability
- Outcomes: Reduce page load by 40%, achieve 99.99% uptime
- Key features: Caching layer, database optimization, CDN expansion
- Estimated effort: 16 person-weeks

**Theme 2: AI/ML Integration**
- Objective: Enable intelligent automation of workflows
- Outcomes: 50% reduction in manual data entry, 35% productivity gain
- Key features: Automated categorization, smart recommendations, predictive analysis
- Estimated effort: 24 person-weeks

**Theme 3: Enterprise Compliance**
- Objective: Meet security and regulatory requirements
- Outcomes: SOC2 certification, ISO 27001 compliance
- Key features: SSO integration, audit logs, data residency options
- Estimated effort: 12 person-weeks

**Theme 4: Developer Experience**
- Objective: Make product more accessible to developers
- Outcomes: 500 API integrations, 100 third-party apps
- Key features: Comprehensive API docs, webhooks, SDK libraries
- Estimated effort: 20 person-weeks

## Quarterly Roadmap Template

### Q2 2024 Roadmap

**Themes:** [3-4 primary themes]
**Team Capacity:** [X person-weeks available]
**Business Goals:** [2-3 key outcomes]

**Theme 1: Collaboration Features** (8 person-weeks)
- Real-time co-editing
  - Status: In Progress
  - Owner: [Engineering lead]
  - Target completion: Week 6
  - Success metric: 60% of new projects use feature

- Activity feeds
  - Status: Planned
  - Owner: [Engineering lead]
  - Target completion: Week 10
  - Success metric: 40% of users weekly active

- Notification system
  - Status: Planned
  - Owner: [Engineering lead]
  - Target completion: Week 12
  - Success metric: 35% of delivered notifications opened

**Theme 2: Mobile Expansion** (6 person-weeks)
- iOS app redesign
  - Status: Planned
  - Owner: [Mobile lead]
  - Target completion: Week 8
  - Success metric: 4.5+ star rating

- Android feature parity
  - Status: Planned
  - Owner: [Mobile lead]
  - Target completion: Week 10
  - Success metric: 2K weekly active users

**Theme 3: Data & Analytics** (4 person-weeks)
- Advanced reporting
  - Status: Planned
  - Owner: [Data lead]
  - Target completion: Week 9
  - Success metric: 20% of projects using reports

- Usage analytics dashboard
  - Status: Planned
  - Owner: [Data lead]
  - Target completion: Week 11
  - Success metric: 30% of teams accessing analytics weekly

**Unscheduled Capacity:** 2 person-weeks (bug fixes, tech debt)

---

## Feature Prioritization

### Prioritization Matrix: Impact vs. Effort

```
         High Impact
              ↑
              │    [Quick Wins]    [Major Projects]
              │    Do first!       Plan carefully
              │
Effort ←──────●────────→
              │
              │   [Fill-ins]       [Avoid]
              │   Low priority     Deprioritize
              ↓
         Low Impact
```

**Quadrant Placement:**

**Quick Wins** (High impact, Low effort)
- Notification settings customization
- Dark mode support
- Search improvements
- Example: Real-time notifications (4 weeks, high user demand)

**Major Projects** (High impact, High effort)
- AI-powered recommendations
- Mobile app redesign
- Enterprise SSO integration
- Example: Real-time co-editing (12 weeks, strategic differentiator)

**Fill-Ins** (Low impact, Low effort)
- UI polish improvements
- Minor feature enhancements
- Bug fixes and technical debt
- Example: Additional export formats (2 weeks, low demand)

**Avoid** (Low impact, High effort)
- Requested but rarely used features
- Technical solutions to minor problems
- Complex integrations with low user count
- Example: Exotic compliance requirement with 2 users (10 weeks, rare need)

### RICE Prioritization Application

**Feature 1: Real-time Co-editing**
- Reach: 5,000 users (potential monthly)
- Impact: 3x (massive workflow improvement)
- Confidence: 90% (strong customer data)
- Effort: 12 weeks
- **RICE Score = (5000 × 3 × 0.9) / 12 = 1,125**

**Feature 2: Mobile App Redesign**
- Reach: 3,000 users (monthly mobile users)
- Impact: 2x (improved experience)
- Confidence: 80% (user feedback + analytics)
- Effort: 10 weeks
- **RICE Score = (3000 × 2 × 0.8) / 10 = 480**

**Feature 3: Dark Mode**
- Reach: 6,000 users (many would use)
- Impact: 1x (nice to have)
- Confidence: 75% (requested feature)
- Effort: 3 weeks
- **RICE Score = (6000 × 1 × 0.75) / 3 = 1,500**

**Prioritized Ranking:** Dark Mode (1,500) > Real-time Co-editing (1,125) > Mobile Redesign (480)

---

## Dependency Mapping

### Dependency Types

**Technical Dependencies** (Feature A requires Feature B)
- Example: Real-time co-editing requires WebSocket infrastructure
- Impact: Cannot ship feature until dependency complete
- Planning: Build in sequence, allocate effort for both

**Data Dependencies** (Feature requires data or infrastructure)
- Example: Analytics dashboard requires data warehouse implementation
- Impact: Delays feature if data work behind schedule
- Planning: Start data work early, plan parallel streams

**Organizational Dependencies** (Cross-team coordination)
- Example: Mobile redesign requires design system alignment
- Impact: Requires coordination, possible schedule conflicts
- Planning: Plan kick-off together, regular syncs

**External Dependencies** (Third-party or customer)
- Example: Enterprise SSO requires customer IT approval
- Impact: Out of control, high risk
- Planning: Start early, have backup plans

### Dependency Map Example

```
┌─────────────────────────────────────────────────┐
│         WebSocket Infrastructure (4w)           │
│              [Q2, Weeks 1-4]                    │
└──────────────────┬──────────────────────────────┘
                   │ Required by
    ┌──────────────┴──────────────┐
    │                             │
    v                             v
Real-time Updates (3w)    Co-editing Engine (6w)
[Q2, Weeks 5-7]           [Q2, Weeks 5-10]
    │                             │
    └──────────┬───────────────────┘
               v
        Activity Feed (2w)
       [Q2, Weeks 11-12]
```

### Critical Path Analysis

**Critical Path:** Longest sequence of dependent activities

```
WebSocket (4w) → Co-editing Engine (6w) → Activity Feed (2w) = 12 weeks

Non-critical path:
WebSocket (4w) → Real-time Updates (3w) = 7 weeks (5-week float)

Project completion: 12 weeks minimum
```

**Implications:**
- Cannot parallelize co-editing and activity feed
- Real-time updates can slip 5 weeks without impacting overall timeline
- Delays to WebSocket infrastructure delay entire project
- Resource freed from real-time updates after week 7 can join other work

---

## Resource Planning and Capacity

### Team Capacity Calculation

**Q2 (13 weeks)**
- Team size: 8 engineers
- Person-weeks available: 8 × 13 = 104 person-weeks
- Buffer for overhead (meetings, 1-on-1s, onboarding): 20%
- Available capacity: 104 × 0.8 = 83 person-weeks

**Work Allocation:**
- Feature development: 75 person-weeks (70 × 83)
- Bug fixes and maintenance: 15 person-weeks (18% × 83)
- Tech debt / infrastructure: 8 person-weeks (10% × 83)
- Unplanned work / buffer: 2 person-weeks (2% × 83)

**Feature Fit:**
- Theme 1 (Collaboration): 8 person-weeks ✓
- Theme 2 (Mobile): 6 person-weeks ✓
- Theme 3 (Analytics): 4 person-weeks ✓
- **Total: 18 person-weeks (within 75 available)** ✓

### Resource Timeline

**W1-4: Foundation Work**
- WebSocket infrastructure (4 engineers)
- Design system updates (2 designers)
- Data warehouse setup (2 data engineers)

**W5-8: Feature Development**
- Real-time updates (2 engineers)
- Co-editing engine (4 engineers)
- iOS redesign (2 mobile engineers)

**W9-12: Integration & Polish**
- Activity feed (2 engineers)
- Analytics implementation (2 data engineers)
- Testing and optimization (3 engineers)
- Android feature parity (2 mobile engineers)

---

## Roadmap Communication Strategies

### Executive Summary Version (1 page)

**Q2 2024 Product Roadmap**

**Themes:**
1. **Collaboration** - Enable real-time teamwork
   - Key features: Co-editing, activity feeds, notifications
   - Business impact: Increase retention by 10%

2. **Mobile** - Mobile-first experience
   - Key features: iOS redesign, Android parity
   - Business impact: 2K weekly mobile users

3. **Data** - Insights and analytics
   - Key features: Advanced reporting, usage analytics
   - Business impact: Support enterprise customers

**Capacity:** 75 person-weeks available, 18 committed to roadmap

---

### Quarterly Detailed Version (2-3 pages)

**[Include full quarterly roadmap template from above]**

---

### Strategic Vision Document (5-10 pages)

**FY 2024 Product Vision**

**Market Opportunity:** [Context]
**Strategic Pillars:** [3-5 key directions]
**Year-long themes:** [Major initiatives]
**Success metrics:** [Overall goals]
**Quarterly focus areas:** [Progression of themes]

---

## Roadmap Governance

### Approval and Change Process

**Change Request Intake:**
1. Request submitted with business justification
2. PM evaluates against current roadmap
3. If adding feature: Which quadrant in prioritization matrix?
4. If adding to current quarter: What gets bumped?
5. Approval criteria: RICE score, alignment with strategy

**Change Categories:**

**Critical Bugs or Compliance** (Expedited)
- Approve with minimal process
- Allocate from buffer/maintenance capacity
- Communicate impact to stakeholders

**Customer or Competitive Pressure** (Standard)
- Evaluate with prioritization framework
- Present trade-off (what gets delayed)
- Stakeholder review and approval

**Nice-to-have Requests** (Queue for consideration)
- Add to backlog for future prioritization
- Review quarterly for potential inclusion
- Track demand signals

**Rejected** (Document reasoning)
- Explain why outside current priorities
- Leave open for future reconsideration
- Provide alternative solutions if possible

### Stakeholder Review Cadence

**Weekly:** Product team sync (15 min check-in on progress)
**Monthly:** Stakeholder review (30 min status on completion, blockers)
**Quarterly:** Planning session (2-hour roadmap setting and approval)
**Annually:** Strategy review (full-day off-site on vision and direction)

---

## Roadmap Contingency Planning

### Risk Categories and Responses

**Technical Risk:**
- Risk: WebSocket scalability issues with 10K concurrent users
- Response: Load test early (W2-3), have fallback architecture
- Impact if realized: 3-week delay

**Resource Risk:**
- Risk: Key engineer leaves mid-quarter
- Response: Cross-training, knowledge documentation
- Contingency: Reduce feature scope or extend timeline

**Market Risk:**
- Risk: Competitor launches similar feature
- Response: Monitor landscape, acceleration plan ready
- Decision point: If competitor ships, accelerate timeline

**Execution Risk:**
- Risk: Requirements unclear, rework needed
- Response: Robust design review, customer validation
- Contingency: Time-box discovery, decide to pivot or proceed

---

## Roadmap Visualization Options

### Timeline/Gantt Format
```
                Q2 2024         Q3 2024
Feature       |═══════════════|═══════════════|
              W1  W5  W10  W13 W18  W23  W26

Co-editing    |──────────────────|
Notifications |─────────────|
Activity Feed |──────────────────────|
Mobile v2     |────────────────|
Analytics     |──────────────────────|
```

### Theme-based Format
```
Collaboration      ████ 8w
├─ Co-editing      ██████ 6w
├─ Notifications   ███ 3w
├─ Activity feed   ██ 2w

Mobile            ██████ 6w
├─ iOS redesign   ███ 4w
├─ Android parity ███ 3w

Analytics         ████ 4w
├─ Reporting      ██ 2w
└─ Dashboard      ██ 2w
```

### Feature Status Board
```
On Track (75%)    ✓ Co-editing, Mobile v2, Reporting
At Risk (15%)     ⚠ Notifications (blocked on infrastructure)
Not Started (10%) ◯ Activity feed (starts week 10)
```

---

## Roadmap Checklist

- [ ] Strategic themes defined and aligned with company goals
- [ ] Features prioritized using RICE or MoSCoW framework
- [ ] Team capacity assessed and realistic
- [ ] Interdependencies mapped and critical path identified
- [ ] Timeline realistic with buffer for unknowns
- [ ] Resource allocation across themes and initiatives
- [ ] Success metrics defined for each initiative
- [ ] Risks identified with mitigation strategies
- [ ] Stakeholder alignment and approvals obtained
- [ ] Communication plan for sharing roadmap
- [ ] Change management process established
- [ ] Contingency plans for key risks
- [ ] Roadmap shared with team and stakeholders

## Output Deliverables

1. **Quarterly Roadmap** - Detailed features, owners, timeline
2. **Strategic Vision** - Annual themes and directions
3. **Dependency Map** - Visual representation of dependencies
4. **Resource Plan** - Capacity allocation and timeline
5. **Prioritization Analysis** - RICE scores and rationale
6. **Risk Register** - Risks and mitigation strategies
7. **Executive Summary** - 1-page overview for stakeholders
8. **Change Management Process** - How changes will be evaluated
9. **Success Metrics Dashboard** - KPIs to track delivery
