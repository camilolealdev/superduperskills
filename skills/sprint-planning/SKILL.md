---
name: sprint-planning
description: "Plan sprints with story point estimation, capacity planning, sprint goals, and retrospective frameworks. Organize teams for effective iteration with clear goals, realistic commitments, and continuous improvement."
---

# Sprint Planning

## Overview
The Sprint Planning skill enables product managers and engineering leaders to organize work into effective sprints that balance delivery with quality. It covers goal-setting, capacity planning, story estimation, and retrospective analysis for continuous improvement.

## When to Use This Skill
- Planning 2-week or 1-week sprints
- Estimating feature complexity and effort
- Balancing feature work with technical debt
- Setting realistic sprint commitments
- Conducting effective sprint kickoffs
- Running productive retrospectives
- Improving team velocity and processes

## Sprint Planning Framework

### Pre-Planning Preparation (1 week before)

**Step 1: Backlog Grooming**
- [ ] Review top 20 backlog items
- [ ] Ensure items have clear acceptance criteria
- [ ] Clarify any ambiguous requirements with PM
- [ ] Break down large items into 2-4 point stories
- [ ] Mark dependencies and blockers
- [ ] Update priority ordering

**Step 2: Capacity Planning**
- [ ] Count available person-days (total days - planned PTO)
- [ ] Account for meetings and overhead (20% typical)
- [ ] Calculate net capacity for dev work
- [ ] Identify team members with special focus areas

**Step 3: Dependency Review**
- [ ] Identify items blocked by previous sprints
- [ ] Ensure unblocking work is prioritized
- [ ] Flag external dependencies (design, third-party)
- [ ] Plan workarounds for external delays

---

## Story Point Estimation

### Estimation Framework (Fibonacci Scale)

**Story points represent relative complexity/effort, not hours**

```
1 point    - Trivial changes: typo fixes, simple config updates
           Example: "Fix button color from blue to red"

2 points   - Simple changes: straightforward feature, 1-2 day effort
           Example: "Add email field to user profile form"

3 points   - Small feature: touches 1-2 components, clear requirements
           Example: "Implement forgot password email flow"

5 points   - Medium feature: crosses multiple systems, some complexity
           Example: "Add two-factor authentication"

8 points   - Complex feature: significant complexity, multiple dependencies
           Example: "Build real-time notification system"

13 points  - Very complex: major feature, high uncertainty
           Example: "Rebuild authentication system"

21 points  - Epic (break down): too large for single sprint
           Example: "Complete mobile app redesign"
```

### Estimation Process (Planning Poker)

**Step 1: Story presentation (2 minutes)**
- PM reads story aloud
- Clarifies acceptance criteria
- Discusses edge cases and dependencies

**Step 2: Silent estimation (1-2 minutes)**
- Team members estimate independently
- Use Fibonacci cards or online tool
- No discussion yet

**Step 3: Discussion (3-5 minutes)**
- High estimates speak first ("Why did you estimate 8?")
- Low estimates speak next ("Why did you estimate 3?")
- PM clarifies requirements if confusion
- Team discusses complexity/uncertainty

**Step 4: Re-estimate (1 minute)**
- Final round of estimation
- Usually converges to one or two adjacent numbers
- If still divergent (1 and 8), break story down further

**Step 5: Acceptance (by story owner)**
- Estimate accepted if team agreement
- Document final estimate
- Flag if story needs re-breaking

### Estimation Tips

**Avoid over-estimating:**
- Assign 1-2 point stories to experienced team member working on same system
- Break down unknowns into separate story
- Don't penalize for learning time

**Avoid under-estimating:**
- Account for testing and bug fixes (usually 20-30%)
- Include integration work and code review
- Consider system complexity, not just happy path
- Don't be optimistic about "easy" items

**Stories that are often underestimated:**
- Anything involving databases or data migration
- Cross-browser or multi-platform support
- Anything with integration requirements
- Anything involving third-party APIs
- Bug fixes (more complex than features)

**Estimation anchoring:**
- Compare to similar stories completed in past
- Use team velocity trend (average points completed per sprint)
- If estimate > 8 points, break into smaller pieces
- Reserve estimation time: typical team estimates 20-30 stories in 2 hours

---

## Sprint Goal Definition

### Goal-Setting Framework

**Effective sprint goal characteristics:**
- Clear and specific (not vague)
- Achievable in single sprint (not epic)
- Represents customer/business value (not just tasks)
- Motivating for team (connects to larger mission)
- Measurable (clear definition of done)

**Sprint Goal Template:**

**Sprint 12 Goal:** "Enable real-time project collaboration"

**Supporting stories:**
1. Real-time task status updates (8 points)
2. Activity feed display (5 points)
3. Notification system MVP (8 points)
4. WebSocket infrastructure (5 points)
5. Technical debt: Upgrade database drivers (3 points)

**Non-goals (explicitly out of scope):**
- Email notification integration (planned for Sprint 13)
- Mobile notification support (Sprint 13)
- Slack integration (Sprint 14)

**Success criteria:**
- Team delivers 80%+ of committed points
- Feature is production-ready with <2% error rate
- Performance <200ms latency for real-time updates

**Why this matters:**
- Reduces meeting-heavy workflows for teams
- Foundation for async communication improvements
- Expected to improve retention by 8%

### Multi-Team Goal Alignment

**Team Goals → Sprint Goal → Initiative Goal → Quarterly Goal**

**Quarterly Goal:** Improve team communication efficiency
├─ Initiative 1: Real-time collaboration (Sprints 12-13)
│  ├─ Team A Goal: Build WebSocket infrastructure
│  ├─ Team B Goal: Create activity feeds
│  └─ Team C Goal: Implement notifications
├─ Initiative 2: Mobile app (Sprints 14-15)
└─ Initiative 3: Advanced analytics (Sprints 16)

---

## Sprint Capacity Planning

### Team Capacity Calculation

**Total sprint capacity (2 weeks):**
- Team size: 8 engineers
- Days per engineer: 10 days (2 weeks)
- Total person-days: 80 person-days

**Subtract unavailable time:**
- Vacation: 2 people × 2 days = 4 person-days
- Conferences/training: 1 person × 2 days = 2 person-days
- Holidays: 0 person-days
- Available person-days: 80 - 6 = 74 person-days

**Subtract overhead and meetings:**
- Daily standup: 15 min × 10 days × 8 people = 2 person-days
- Sprint planning: 4 hours = 0.5 person-days
- Sprint review/retro: 3 hours = 0.375 person-days
- 1-on-1s and admin: 1 hour/week × 8 people = 1.6 person-days
- Meetings/overhead total: ~4.5 person-days

**Net development capacity: 74 - 4.5 = 69.5 person-days**

**Points available (based on velocity):**
- Historical velocity: 120 points per sprint (over last 4 sprints)
- Adjusted for current capacity: 120 × (69.5/74) = 112 points target

### Balanced Work Distribution

**Recommended allocation:**
- Feature stories: 85 points (76%)
- Bug fixes: 15 points (13%)
- Technical debt: 12 points (11%)
- **Total committed: 112 points**

**By team/focus area:**
- Backend: 40 points (35%)
- Frontend: 35 points (31%)
- Mobile: 20 points (18%)
- QA/Infrastructure: 17 points (15%)

### Buffer and Contingency

**Conservative estimation (90% confidence):**
- Committed points: 85 (75% capacity)
- Buffer: 27 points (25% capacity)
- Buffer used for: Bugs, unplanned work, opportunities

**Medium estimation (75% confidence):**
- Committed points: 112 (100% capacity)
- Requires: Perfect execution, no major blockers

**Aggressive estimation (50% confidence):**
- Committed points: 130+ (>100% capacity)
- Results in: Incomplete sprints, team burnout (avoid)

**Recommendation:** Commit 85-95 points per sprint (75-85% capacity)

---

## Sprint Planning Meeting Structure

### Sprint Planning Meeting Agenda (4 hours for 2-week sprint)

**Part 1: Context and Goal Setting (30 minutes)**

"What will we accomplish this sprint and why?"

- Product Manager presents top priority items
- Context on customer feedback driving priorities
- Business goals for the sprint
- Dependencies and blockers to be aware of
- Team asks clarifying questions

**Part 2: Story Refinement and Estimation (2 hours)

"How complex is the work and what will done look like?"

- PM presents stories in priority order
- Engineering discusses technical approach
- Estimation using planning poker (30-40 stories/hour typical)
- Break down stories > 8 points
- Identify dependencies and risks

**Part 3: Capacity Planning and Commitment (45 minutes)**

"What can we realistically commit to?"

- Scrum master presents available capacity
- Team considers estimation results
- Decide which items to include in sprint
- Total committed points should be 75-85% of capacity
- Explicitly note what's NOT being done and why

**Part 4: Sprint Planning and Kickoff (45 minutes)**

"How will we execute and who does what?"

- Discuss technical approach for major items
- Identify who will take lead on each story
- Plan pair programming or knowledge sharing
- Clarify any remaining acceptance criteria
- Confirm sprint goal
- Set success criteria and metrics

### Sprint Planning Checklist

- [ ] Product Manager has prioritized backlog
- [ ] Backlog items have acceptance criteria
- [ ] Stories >8 points are broken down
- [ ] Team has calculated available capacity
- [ ] Vacation, meetings, overhead accounted for
- [ ] Top 15-20 stories estimated
- [ ] Sprint goal clearly defined
- [ ] Team has committed to sprint (not mandatory)
- [ ] Success metrics agreed upon
- [ ] Dependencies identified and planned for
- [ ] Risks flagged and mitigation planned
- [ ] All team members understand goals and assignments

---

## Daily Standup Management

### Standup Format (15 minutes, time-boxed)

**Three questions each person answers:**
1. "What did I accomplish yesterday?"
2. "What will I accomplish today?"
3. "What blockers do I have?"

**Example:**
- Developer A: "Finished user auth story (3 pts). Today: start password reset. No blockers."
- Developer B: "Code review and small bugfixes. Today: password reset tests. Waiting on database schema (blocker)."
- QA: "Tested auth flows. Today: edge case testing. Need password reset ready."

**Standup discipline:**
- Same time daily (consistency)
- 15 minute time box (keep focused)
- Stand up (energy/focus)
- Report on sprint commitments
- Capture blockers for follow-up

### Blocker Resolution

**Blocker formats:**
- Dependency on another team
- Technical blockers (unclear requirements, architecture decision needed)
- Resource blockers (waiting for code review, infrastructure)
- External blockers (third-party service, customer response)

**Blocker escalation:**
- Flag in standup
- Scrum Master follows up immediately
- Resolve before next standup if possible
- Reassign work if blocker will last >1 day
- Don't let team get blocked

---

## Sprint Metrics and Tracking

### Key Sprint Metrics

**Velocity (points completed per sprint)**
- Definition: Points in stories marked "done" by end of sprint
- Calculation: Sum story points of completed items
- Tracked: Over last 4-6 sprints (trendline)
- Stable velocity: Good predictor for future sprints
- Rising velocity: Improving efficiency or easier work
- Falling velocity: Challenges, tech debt buildup

**Burn-down Chart (work remaining over time)**
```
Sprint Points Remaining
120 |
    | ● (Sprint start)
100 | \●
    |  \●
80  |   \●●
    |    \   ●
60  |     \●
    |      \
40  |       ●\
    |        \●
20  |         \●
    |          \●
0   |___________●●___→
    0  2  4  6  8  10  Days
      (ideal line shown)
```

- Slope = velocity
- Bumps = new work added mid-sprint (try to avoid)
- Flat spots = days with no progress (investigate)
- Trend should be downward toward zero by day 10

**Scope Creep (points added/removed mid-sprint)**
- Target: 0 (no mid-sprint changes)
- Acceptable: <5% of committed points
- Bad: >10% of committed points (scope not protected)

**Defect Escape Rate (bugs found after sprint)**
- Definition: % of stories that require follow-up fixes
- Target: <10%
- High rate: Quality issues (invest in testing)
- Low rate: Good QA process

### Burndown Interpretation

**Healthy sprint (burndown on track):**
- Steady downward trend
- Minimal scope changes
- Completed by end of sprint
- Team confident in forecast

**Scope creep sprint (creeping burndown):**
- Work added throughout sprint
- Burndown appears stuck
- Team overcommitted or reactive
- Action: Stop adding work, review commitment process

**Quality issue sprint (sudden jump back up):**
- Spike in blockers or bugs found
- Unexpected rework discovered
- Requires investigation in retrospective
- Action: Reduce commitment, invest in QA

**Blocked sprint (flat burndown):**
- Team stuck on blockers
- Waiting for dependency resolution
- Work not progressing
- Action: Address blockers immediately, reassign work

---

## Sprint Review and Retrospective

### Sprint Review (30-45 minutes)

"What did we accomplish and what will customers see?"

**Agenda:**
1. Context and sprint goal recap (2 min)
2. Demo of completed work (20 min)
   - Show working features
   - Live demo on staging/production
   - Gather feedback from stakeholders
3. Incomplete work discussion (5 min)
   - Why wasn't it finished?
   - Will it carry to next sprint?
4. Feedback and Q&A (10 min)
   - Customer and stakeholder feedback
   - Feature requests
   - Directional feedback for future work

**Demo best practices:**
- Prepare demos in advance
- Show real data, not demo data
- Show edge cases and error handling
- Have a demo failure backup plan
- Explain "why" not just "what"

### Sprint Retrospective (45-60 minutes)

"What went well? What can we improve?"

**Three main questions:**
1. "What went well this sprint?"
2. "What could we improve?"
3. "What will we commit to trying next sprint?"

**Retrospective format options:**

**Standard Format (45 min):**
- Warm-up/icebreaker (5 min)
- Brainstorm went well (5 min)
- Brainstorm improvements (5 min)
- Vote on priority issues (5 min)
- Discuss top 2-3 issues (20 min)
- Define actions and commitments (5 min)

**Sailboat Format (35 min):**
```
Wind (what's moving us forward)
    ▲
    | ✓ Clear requirements
    | ✓ Good pairing
Anchor (what's slowing us)
    | ✗ Slow builds
    | ✗ Meetings interrupting focus
Rocks (what could sink us)
    | ⚠ Tech debt accumulation
```

**Start-Stop-Continue Format (30 min):**
- Start: New practices to adopt
- Stop: Practices to discontinue
- Continue: Good practices to maintain

### Retrospective Actions and Commitment

**Action items should be:**
- Specific: "Implement automated tests for API endpoints" (not "improve testing")
- Measurable: "Reduce build time from 8 min to <3 min" (not "faster builds")
- Owner: Assigned to specific person or pair
- Timeline: Complete by mid-sprint checkpoint
- Tracked: Review in next retro

**Example actions:**
- "Set up code owner reviews by mid-sprint" (Owner: Tech lead)
- "Document API integration patterns" (Owner: Frontend lead)
- "Schedule focus time 9-11 AM daily" (Whole team commitment)
- "Limit Slack during standups" (Team commitment)

**Retrospective metrics:**
- Team identifies 3-5 improvement areas per sprint
- 60%+ of previous sprint actions completed
- Team morale trending up or stable
- Velocity stable or improving

---

## Sprint Planning Checklist

- [ ] Backlog groomed and prioritized
- [ ] Top 20 items estimated
- [ ] Team capacity calculated
- [ ] Stories >8 points broken down
- [ ] Sprint goal defined and aligned
- [ ] Stories assigned to team members
- [ ] Dependencies and blockers identified
- [ ] Success metrics and acceptance criteria clear
- [ ] Story descriptions in JIRA/tracking system
- [ ] Team confident in commitment (feeling: 8/10)
- [ ] Sprint kickoff meeting completed
- [ ] Burndown chart setup and ready
- [ ] Daily standup time scheduled
- [ ] Sprint review and retro scheduled

## Output Deliverables

1. **Sprint Plan** - Goal, committed stories, capacity plan
2. **Story Estimates** - Breakdown of all sprint items
3. **Capacity Analysis** - Available capacity vs. commitment
4. **Burndown Dashboard** - Track sprint progress daily
5. **Risk Register** - Blockers and mitigation for sprint
6. **Team Commitments** - Individual assignments and goals
7. **Success Metrics** - How we'll measure sprint success
8. **Retro Actions** - Documented improvements and commitments
9. **Velocity Trend** - Historical data for forecasting
