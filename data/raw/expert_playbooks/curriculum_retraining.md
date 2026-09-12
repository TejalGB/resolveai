# Curriculum and Retraining Issues

## Category
Curricula and Retraining

## Product
SAP SuccessFactors Learning

## Incident

A user reports that they have already completed a course, but the course is still assigned to them and they continue to receive notifications asking them to complete it.

## Problem Understanding

A completed learning item remaining assigned does not necessarily indicate an LMS defect.

If the learning item is part of a curriculum and retraining is configured, the system may assign the learning item again according to the configured retraining rules.

The user may therefore see the course as assigned and continue receiving notifications even though they completed a previous instance of the course.

The key distinction is:

- Previous completion indicates that the learner completed an earlier learning requirement.
- The current curriculum requirement determines whether the learner needs to complete the learning item again.

Therefore, the analyst should investigate the curriculum and retraining configuration before considering the assignment incorrect.

---

## Troubleshooting Steps

### 1. Check Curriculum Association

Verify whether the learning item is part of a curriculum.

If the learning item is not associated with a curriculum, investigate the assignment using the applicable learning assignment rules.

If it is part of a curriculum, continue with the retraining investigation.

### 2. Determine Initial vs. Retraining Requirement

Determine whether the current requirement is:

- An initial curriculum requirement
- A retraining requirement

Initial and retraining requirements can have different configuration values and should not be treated as the same condition.

### 3. Check Retraining Configuration

Check whether retraining is configured for the relevant curriculum or learning requirement.

If retraining is configured, determine the applicable retraining settings.

### 4. Identify the Retraining Basis

Determine whether the retraining requirement is:

- Event-based
- Calendar-based

For event-based retraining, the relevant event or completion date is used to calculate the next requirement.

For calendar-based retraining, the configured basis date is used to establish the applicable training period.

### 5. Check the Basis Date or Event Date

For calendar-based retraining, check the configured basis date.

For event-based retraining, identify the relevant event date, such as the applicable completion event.

Use the appropriate date when calculating the next retraining requirement.

### 6. Check Retraining Number and Period

Check the configured retraining number and period.

Examples of periods include:

- Days
- Months
- Years

These values determine the retraining cadence.

For example, a configuration requiring retraining every 1 year creates a recurring training requirement based on the applicable retraining basis.

### 7. Calculate the Next Retraining Requirement

Use the applicable basis or event date together with the retraining number and period to determine when the next requirement becomes due.

### 8. Check the Required Date

Check the required date associated with the user's current curriculum requirement.

Compare the required date with:

- Previous completion date
- Current assignment
- Retraining configuration

This helps determine whether the current assignment is expected.

### 9. Check Effective Date When Curriculum Configuration Has Changed

If the curriculum or its learning items were recently changed, check the effective date of the change.

A curriculum change may not immediately affect the learner if the change has a future effective date.

### 10. Check Previous Completion Rules When Relevant

If the issue involves an older completion record, check whether previous completions are considered for the current curriculum requirement.

Where applicable, review the configuration related to ignoring previous completions older than a specified period.

---

## Resolution Logic

User completed course
→ Course is still assigned / notifications continue
→ Check whether course is part of a curriculum
→ Determine initial vs. retraining requirement
→ Check retraining configuration
→ Identify event-based or calendar-based retraining
→ Check applicable basis/event date
→ Check retraining number and period
→ Calculate next retraining requirement
→ Check required date
→ Check effective date if curriculum was recently changed
→ Determine whether current assignment is expected

---

## Expected System Behavior

If the learning item is part of a curriculum with a valid retraining requirement, the course may remain assigned or be assigned again when the next retraining requirement becomes applicable.

The learner may also continue receiving notifications associated with the current requirement.

In such cases, the behavior may be expected system behavior rather than a defect.

---

## Common User Question

> "I already completed this course. Why is it still assigned to me and why am I still receiving notifications?"

### Recommended Investigation

Do not immediately remove the assignment or treat the issue as a defect.

First verify:

1. Curriculum association
2. Retraining configuration
3. Retraining basis
4. Basis/event date
5. Retraining number
6. Retraining period
7. Required date
8. Effective date, if applicable
9. Previous completion rules, if applicable

---

## Resolution

If the current assignment matches the configured retraining requirement, explain to the user that the assignment and notifications are expected because the learning item has a recurring retraining requirement.

If the assignment does not match the configured retraining rules, investigate the curriculum configuration and assignment further.

If the issue cannot be resolved through standard investigation, collect the relevant configuration, dates, user information, and learning item details and escalate to the appropriate support team.

---

## Important Considerations

- A previous completion does not necessarily eliminate a future retraining requirement.
- Do not assume that a course remaining assigned means the assignment is incorrect.
- Always consider the curriculum and retraining configuration before modifying an assignment.
- The applicable date for calculation depends on whether the retraining basis is event-based or calendar-based.
- Curriculum changes may require checking the effective date.
- Historical completion records may affect curriculum status depending on the applicable configuration.

---

## Example Scenario

A user completed a mandatory course but reports that the same course is still assigned and they continue receiving reminders.

The analyst checks the curriculum and finds that the course has a yearly retraining requirement.

The analyst then checks the applicable retraining basis and date, calculates the next retraining requirement, and verifies the required date.

If the current assignment corresponds to the configured retraining cycle, the assignment and notifications are considered expected behavior and the user can be informed accordingly.

---

## Source Type

Expert Resolution Playbook

## Knowledge Sources

- Internal LMS incident-resolution experience
- SAP SuccessFactors Learning documentation
- SAP Knowledge Base Articles (to be added)