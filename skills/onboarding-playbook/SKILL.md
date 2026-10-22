---
name: onboarding-playbook
description: "Design customer onboarding playbooks with milestone tracking, training plans, health checks, and success criteria"
---

# Onboarding Playbook

## Overview

Design comprehensive onboarding playbooks that accelerate time-to-value, ensure customer success, and build strong product adoption. Effective onboarding sets the foundation for long-term customer health, expansion, and retention.

## Onboarding Goals

**Primary Objectives**:
- Get customer live on the product (time-to-value: <30 days)
- Achieve 80% adoption of core features within 60 days
- Build internal champion for product expansion
- Establish positive relationship and trust
- Enable customer to operate independently

**Success Metrics**:
- Time to first value: 7-14 days
- First 30 days: Core workflows operational
- By day 60: 80% core features adopted; team trained
- By day 90: Expansion conversation; roadmap discussion
- By month 6: Renewal conversation with confidence

## Onboarding Playbook Template

### Phase 1: Pre-Implementation (Days -7 to 0)

**Week Before Go-Live**:

**Kickoff Meeting** (30-60 min):
- Attendees: Customer PM/owner, IT lead, CSM, Implementation lead
- Agenda:
  - Customer success plan overview
  - Timeline and milestones
  - Roles and responsibilities
  - Success criteria definition
  - Risk identification

**Deliverables**:
- [ ] Success plan documented (shared document)
- [ ] Timeline and key dates confirmed
- [ ] Customer DRI (Directly Responsible Individual) named
- [ ] Escalation path defined
- [ ] Communication cadence set (weekly check-ins)

**Pre-Implementation Prep**:
- [ ] Customer provides data (systems to integrate, data formats)
- [ ] Vendor prepares: Sandbox environment, test data, configurations
- [ ] Customer: Network access, credentials, IT approvals
- [ ] Vendor: Training materials, documentation, runbooks

**Stakeholder Alignment**:
```
Role | Name | Company | Responsibility | Communication Freq
-----|------|---------|-----------------|------------------
Executive Sponsor | [Name] | Customer | Executive alignment; approval | Monthly
Project Lead | [Name] | Customer | Day-to-day project ownership | Weekly
IT Lead | [Name] | Customer | System access; security; infrastructure | Weekly
Power Users | [Names] | Customer | Feature validation; training peers | 2x/week
CSM | [Name] | Vendor | Overall account; success planning | 2x/week
Implementation Lead | [Name] | Vendor | Technical implementation | 2x/week
Product SME | [Name] | Vendor | Feature training; workflow design | As needed
```

### Phase 2: Implementation & Enablement (Days 1-30)

**Week 1: Discovery & Design**

```
WEEK 1 ACTIVITIES:

MONDAY - Kickoff:
- Welcome call with full team
- Review success plan and timeline
- Agree on communication cadence
- First weekly check-in scheduled

TUESDAY - Technical Setup:
- Data export from legacy system (if migration needed)
- Credential provisioning and access testing
- System configuration begins (workflows, integrations)
- Environment validation

WEDNESDAY - Process Mapping:
- Current state process walkthrough
- Future state design (how workflows will work in new system)
- Pain points identified
- Change management concerns raised

THURSDAY - Initial Training:
- 2-hour system overview training
- Navigation and UI walkthrough
- Admin and user roles explained
- Q&A session

FRIDAY - Week 1 Review:
- What's complete? (data loaded, core config done)
- Blockers or issues? (address by EOD)
- On track for Week 2? (Yes/No; adjustments if needed)
- Team confidence level? (survey)
```

**Week 2-3: Configuration & Pilot**

```
WEEK 2-3 ACTIVITIES:

CONFIGURATION:
- Map legacy data to new system fields
- Build integrations with dependent systems
- Configure workflows and automation rules
- Test configurations with sample data
- Validate data accuracy

PILOT TESTING:
- Select 3-5 power users for pilot
- Conduct live transactions with real use cases
- Gather feedback on workflows
- Identify usability gaps
- Refine configurations based on feedback

TRAINING PLAN:
- Day 1: Admin/Workflow training (2 hours)
- Day 2: Data migration overview (1 hour)
- Day 3: Hands-on practice (2 hours)
- Day 4: Edge cases and exceptions (1 hour)
- Day 5: Train-the-trainer for power users (1 hour)

SUCCESS CRITERIA FOR WEEK 2-3:
- Core workflows configured and tested
- Data migrated and validated
- Pilot team comfortable with workflows
- Integration testing complete and successful
- No critical blockers
```

**Week 4: Go-Live Preparation**

```
WEEK 4 ACTIVITIES:

GO-LIVE PREPARATION:
- Final data migration (production data)
- Cutover plan documented (what's turning off, what's turning on)
- Rollback plan documented (in case of critical issues)
- Support escalation path confirmed
- Go-live schedule finalized (date, time window, teams)

FINAL TRAINING:
- End-user training for all 30 users (4 sessions x 30 min)
- Knowledge base created and shared
- Quick reference guides printed
- FAQ document reviewed
- Recorded training available

GO-LIVE DECISION GATE:
- Vendor: All critical configurations complete (Yes/No)
- Customer: Team trained and confident (Yes/No)
- Data: Migration validated; zero errors (Yes/No)
- Support: Escalation path ready; 24/7 if needed (Yes/No)
- Risk: Identified and mitigated; no blockers (Yes/No)

IF ALL YES: Proceed to go-live
IF ANY NO: Delay and resolve before proceeding
```

### Phase 3: Launch & Hypercare (Days 31-45)

**Go-Live Week**:

```
GO-LIVE SCHEDULE:

Monday 9:00 AM - Go-Live Meeting:
- All teams on call
- Final system checks
- Load production data
- Activate new system
- De-activate legacy system

Monday 9:30 AM - First Transactions:
- Power users execute first transactions
- Live support from implementation team
- Issues logged and resolved immediately
- Feedback gathered

Monday 2:00 PM - Team Rollout:
- Phased rollout to all users
- Training reinforcement
- Real-time support available
- Managers monitoring adoption

Tuesday-Friday - Hypercare:
- CSM + implementation team monitoring 24/7
- On-call support for any issues
- Daily sync meetings (30 min)
- Issue escalation triggers immediate response
- Performance monitoring (system health, data accuracy)

GO-LIVE METRICS:
- System uptime: 99.9%+
- All critical workflows operational
- User adoption: 100% of power users active
- Issue resolution: <2 hours average
- Data accuracy: 100% validation
- Support: 0 critical issues unresolved
```

**Hypercare Support** (2-4 weeks post-go-live):

```
HYPERCARE TEAM:
- CSM (primary contact for business issues)
- Implementation Lead (technical issues)
- Product SME (feature/workflow questions)
- Escalation: Vendor VP if critical issues

AVAILABLE 24/7 FOR:
- Production outages
- Data accuracy issues
- Critical workflow failures
- Security/compliance issues

AVAILABLE BUSINESS HOURS FOR:
- Training questions
- Process optimization
- Non-critical issues
- Enhancement requests

ISSUE SEVERITY:

P1 (CRITICAL):
- System down or unavailable
- Data loss or corruption
- Security breach
- SLA: 30-minute response, 4-hour resolution

P2 (HIGH):
- Core workflow not functioning
- Performance degradation
- Workaround available
- SLA: 2-hour response, same-day resolution

P3 (MEDIUM):
- Non-core functionality issue
- User confusion on feature
- Workflow slower than expected
- SLA: 4-hour response, 24-hour resolution

P4 (LOW):
- Enhancement request
- Documentation question
- UI preference
- SLA: Next business day response

DAILY HYPERCARE MEETING (15 min):
- P1 issues: Are they resolved? (Yes/No; if no, escalate)
- Key metrics: System health, adoption, satisfaction
- Feedback: What's working well? What needs attention?
- Next day focus: What's priority?
```

### Phase 4: Transition to Support (Days 46-90)

**Week 7-8: From Hypercare to Standard Support**

```
TRANSITION PLAN:

Week 7:
- Hypercare team on 9-5 support (instead of 24/7)
- CSM takes on account health monitoring
- Customer support ticket system activated
- Training on support processes

Week 8:
- Transition complete to standard support
- SLA: Business hours; P1 next morning
- Customer escalation: CSM → Vendor Support
- Final go-live retrospective meeting

GO-LIVE RETROSPECTIVE:
Attendees: Customer leadership, CSM, Implementation lead
Agenda:
- What went well? (celebrate wins)
- What was challenging? (identify learnings)
- Feedback on vendor team (CSM, implementation, support)
- Feedback from vendor on customer team (partnership quality)
- Recommendations for future projects (if applicable)
- Document learnings for organizational improvement

CUSTOMER FEEDBACK:
Ask for:
- Overall satisfaction (1-10 scale)
- Would you recommend us? (NPS question)
- What could we have done better?
- How confident are you operating independently?
```

## Milestone-Based Onboarding

**Create Customer-Visible Milestones**:

```
ONBOARDING ROADMAP - SHARED WITH CUSTOMER

PHASE 1: DISCOVERY (Weeks 1-2)
Milestone 1: Kickoff Complete
- Success plan finalized
- Stakeholders aligned
- Timeline confirmed
- Due: Day 5
- Status: [Complete] / [On Track] / [At Risk]

Milestone 2: Technical Setup Complete
- Systems access provisioned
- Integrations defined
- Data migration strategy confirmed
- Due: Day 10
- Status: [Complete] / [On Track] / [At Risk]

PHASE 2: BUILD (Weeks 3-4)
Milestone 3: Configurations Complete
- Core workflows configured
- Data mapped and tested
- Integrations built and tested
- Due: Day 20
- Status: [Complete] / [On Track] / [At Risk]

Milestone 4: Training Complete
- All users trained
- Knowledge base ready
- Power users certified to train others
- Due: Day 27
- Status: [Complete] / [On Track] / [At Risk]

PHASE 3: GO-LIVE (Week 5)
Milestone 5: Go-Live
- Production data loaded
- Legacy system turned off
- All users on new system
- Hypercare in place
- Due: Day 35
- Status: [Complete] / [On Track] / [At Risk]

PHASE 4: STABILIZE (Weeks 6-13)
Milestone 6: 100% Adoption
- All users active on system
- No usage of legacy system
- User confidence high
- Due: Day 60
- Status: [Complete] / [On Track] / [At Risk]

Milestone 7: Full Independence
- Customer operating without vendor support
- Standard support model in place
- Documentation complete
- Team can handle routine issues
- Due: Day 90
- Status: [Complete] / [On Track] / [At Risk]
```

## Health Checks During Onboarding

**Track Customer Health Weekly**:

```
WEEKLY HEALTH ASSESSMENT (Checklist)

ADOPTION:
[ ] 80%+ of target users actively using system
[ ] Core workflows executing daily
[ ] Integration working as expected
[ ] Data quality meets standard (>95% accuracy)

ENGAGEMENT:
[ ] Leadership engaged and informed
[ ] Power users productive and confident
[ ] Training feedback positive
[ ] No significant user complaints

TECHNICAL:
[ ] System uptime 99.5%+
[ ] Performance acceptable (no slowdowns)
[ ] Data integrity verified
[ ] Security controls operating

RELATIONSHIP:
[ ] Communication cadence maintained
[ ] Issues resolved promptly
[ ] Customer feeling supported
[ ] Trust building positively

TIMELINE:
[ ] On schedule for Phase completion
[ ] Milestones being met
[ ] Resource constraints manageable
[ ] No blockers preventing progress

SCORING:
- All YES: GREEN - Healthy onboarding
- 1-2 NO: YELLOW - Monitor closely; address gaps
- 3+ NO: RED - At-risk; escalate and remediate

IF RED: Escalation meeting within 24 hours
```

## Success Criteria Definition

**Define What Success Looks Like** (before implementation):

```
ONBOARDING SUCCESS CRITERIA - ACME CORP

OPERATIONAL SUCCESS:
- All 30 users trained and comfortable using system
- Core workflows (Sales → Fulfillment → Payment) operating daily
- Integration with accounting system live and syncing
- Report generation working; stakeholders using insights
- Zero critical production issues for 7+ consecutive days

BUSINESS SUCCESS:
- Operational efficiency improved 25% (vs. legacy system)
- Processing time reduced from 2 days to 4 hours
- Error rate <0.5% (vs. 3% in legacy system)
- Time to insights: <24 hours (vs. 1 week)
- ROI positive within 90 days

ADOPTION SUCCESS:
- 80%+ of users daily active (login 5+ days/week)
- Core features adopted by 90%+ of users
- Advanced features (automation, reporting) adopted by 60%+
- User satisfaction NPS: 50+
- No critical skill gaps preventing independent operation

RELATIONSHIP SUCCESS:
- Customer feels supported throughout transition
- Issues resolved promptly and transparently
- Trust established with CSM and support team
- Expansion conversation starting by day 90
- Renewal confidence high

METRICS TO TRACK:
- Days to go-live (target: 30 days)
- Adoption rate at 30/60/90 days
- Support ticket volume and resolution time
- System uptime and performance metrics
- Customer satisfaction and NPS
- Revenue/cost impact metrics

FINAL SIGN-OFF:
Upon completion, customer acknowledges:
[ ] All onboarding milestones complete
[ ] Team trained and confident
[ ] System operating as expected
[ ] Ready for standard support transition
[ ] Excited about future partnership

Signed: _________________________ Date: _________
```

## Onboarding Playbook by Customer Segment

**Customize for Customer Size**:

```
PLAYBOOK VARIATIONS:

ENTERPRISE (100+ users, $100K+ ACV):
- Duration: 16-20 weeks
- Implementation lead assigned full-time
- Weekly steering committee meetings
- Dedicated success manager post-launch
- Custom integrations and configurations
- Extensive change management
- Formal risk and issue management
- Post-implementation review and optimization

MID-MARKET (20-100 users, $20K-$100K ACV):
- Duration: 8-12 weeks
- Part-time implementation lead
- Bi-weekly stakeholder meetings
- CSM assigned upon go-live
- Standard integrations (API-based)
- Moderate change management
- Weekly issue tracking
- Post-implementation lessons learned

SMB (1-20 users, <$20K ACV):
- Duration: 4-6 weeks
- Vendor CSM manages implementation
- Weekly status calls
- CSM assigned upon go-live
- Self-service setup + phone support
- Light touch change management
- Issue tracking via support system
- Post-launch check-in at 30/60/90 days

STARTUP (1-10 users, <$5K ACV):
- Duration: 2 weeks
- Automated onboarding with email/chat
- Asynchronous check-ins
- Self-service setup and training
- Chat-based support
- Success metrics: Usage and retention
- Auto-renewal playbook
```

## Common Onboarding Mistakes (To Avoid)

1. **Unclear Success Criteria**: Define success before starting
2. **No Dedicated CSM**: Customer needs single point of contact
3. **Insufficient Training**: Time investment upfront prevents support burden later
4. **Scope Creep**: Say no to out-of-scope requests; track for phase 2
5. **Poor Change Management**: Address user resistance; get champions
6. **Technical Readiness Gaps**: Assume nothing; validate all assumptions
7. **Neglecting Data Quality**: Bad data in = bad results out
8. **Over-Customization**: Encourage vendor best practices, not custom workflows
9. **No Contingency Plan**: Assume something will go wrong; have rollback plan
10. **Ending Too Early**: Hypercare shouldn't end until independence confirmed

## Post-Onboarding Success

**60-Day Success Review**:

```
60-DAY SUCCESS REVIEW MEETING

Attendees: Customer leadership, CSM, VP Customer Success
Duration: 60 minutes
Agenda:

1. ONBOARDING RECAP (5 min)
   - Timeline adherence
   - Milestone achievement
   - Team feedback

2. OPERATIONAL METRICS (10 min)
   - System adoption (% active users)
   - Feature utilization (% features used)
   - Data quality (validation results)
   - Performance vs. targets
   - Issue resolution time

3. BUSINESS IMPACT (10 min)
   - Cost savings achieved
   - Efficiency improvements
   - Revenue impact
   - ROI progress
   - Payback period

4. CUSTOMER FEEDBACK (10 min)
   - Satisfaction with onboarding
   - Satisfaction with vendor
   - Areas for improvement
   - Likelihood to recommend (NPS)

5. EXPANSION OPPORTUNITIES (15 min)
   - Feature adoption gaps (training needed?)
   - Adjacent business units (expansion potential)
   - Workflow optimization (advanced features)
   - Custom development (custom integrations)
   - Total addressable opportunity

6. ROADMAP & RENEWAL (10 min)
   - Customer roadmap alignment
   - Vendor roadmap (what's coming)
   - Renewal confidence (Yes/No)
   - Expansion commitment (if any)

SUCCESS DEFINITION:
Customer acknowledges:
[ ] Onboarding successful
[ ] System operating as expected
[ ] Team trained and confident
[ ] Value being realized
[ ] Ready for expansion/renewal discussion

NEXT STEPS:
- Monthly touch-bases (vs. weekly)
- Expansion planning (if applicable)
- Renewal conversation (if <120 days to renewal)
- Continuous improvement plan
```

---

**Use this skill to**: Accelerate customer time-to-value, ensure successful adoption, build strong relationships, and create expansion and retention foundations.
