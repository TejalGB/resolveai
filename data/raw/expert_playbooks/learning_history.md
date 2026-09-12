# Learning History and Completion Issues

## Category
Learning History and Completion

## Product
SAP SuccessFactors Learning

## Incident

A user reports that they completed a course or learning item, but the completion or learning history is not reflected correctly in LMS.

The user may report that the course is still showing as incomplete, the expected completion is not visible, or the learning history does not reflect the expected status.

## Problem Understanding

A learning history or completion issue does not necessarily indicate an LMS defect.

In many cases, the learner has not completed all the activities required for the learning item to be recorded as complete.

Common examples include:

- Required links within the content were not opened.
- A mandatory survey was not completed.
- Another required activity was not completed.
- The user did not complete the learning item according to the configured completion requirements.

The issue should therefore be investigated before assuming that the system has failed to record the completion.

---

## Troubleshooting Steps

### 1. Understand the User's Issue

First identify:

- Which course or learning item is affected?
- What status does the user currently see?
- When did the user complete the course?
- What does the user expect to see?
- Is the issue limited to one user or affecting multiple users?

Collect the relevant user and learning item information before proceeding.

### 2. Ask the User to Clear Cache and Retry

Ask the user to clear their browser cache and try the learning activity again.

This helps rule out browser or session-related issues.

### 3. Check Completion Requirements

Verify whether the learner has completed all required activities associated with the learning item.

Pay particular attention to:

- Required links within the content
- Mandatory surveys
- Required assessments
- Other activities required for completion

If a required activity has not been completed, ask the learner to complete it and retry.

### 4. Self-Assign and Test

If the issue persists, self-assign the learning item and test it independently where possible.

This helps determine whether the issue is:

- Specific to the individual user
- Related to the learning item
- Reproducible for other users

### 5. Compare the Results

Compare the user's experience with the result of the test assignment.

If the test assignment works correctly, investigate whether the issue is specific to the user's record or actions.

If the issue can also be reproduced during testing, investigate the learning item or system behavior further.

### 6. Investigate Further if Required

If the issue cannot be explained through the above checks, collect the relevant information and investigate further.

Depending on the issue, this may require checking the user's learning status, learning item details, class information, or other relevant LMS information.

### 7. Escalate When Required

If standard troubleshooting does not identify or resolve the issue, escalate it to the appropriate support team with the relevant user, learning item, class, and troubleshooting details.

---

## Decision Flow

User reports completion/history issue
→ Identify user and learning item
→ Clear cache and retry
→ Check completion requirements
→ Check required links/survey/activities
→ Self-assign and test
→ Compare results
→ Determine user-specific vs. general issue
→ Investigate further or escalate if required

---

## Common Causes

Possible causes include:

- Required links were not opened.
- Mandatory survey was not completed.
- Required activity or assessment was not completed.
- Browser/session-related issue.
- Issue is specific to the user's learning record.
- Learning item or class configuration requires further investigation.

---

## Resolution Logic

The first objective is to determine whether the learner has actually completed all requirements necessary for the learning item to be recorded as complete.

If the required activities have not been completed, guide the user to complete them.

If the issue persists after completing all requirements, reproduce the issue through self-assignment where possible.

If the issue is reproducible or cannot be explained through standard troubleshooting, investigate further and escalate with the relevant details.

---

## Important Considerations

- Do not immediately assume that a missing completion record is a system defect.
- Always check whether all required learning activities were completed.
- Required links and surveys can affect completion.
- Self-assignment can help determine whether the issue is user-specific or reproducible.
- Troubleshooting should be performed before escalation.
- The appropriate resolution depends on the specific learning item and its configured completion requirements.

---

## Source Type

Expert Resolution Playbook

## Knowledge Sources

- Internal LMS incident-resolution experience
- SAP SuccessFactors Learning documentation
- SAP Knowledge Base Articles (to be added)