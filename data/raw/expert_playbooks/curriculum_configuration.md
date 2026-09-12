# Curriculum Configuration Issues

## Category

Curriculum Configuration

## Product

SAP SuccessFactors Learning

## Incident

A user, administrator, or support team reports that a curriculum is not behaving as expected.

The issue may involve curriculum visibility, assignment, requirements, completion status, required items, optional items, sub-curricula, effective dates, or recent configuration changes.

## Problem Understanding

A curriculum is a structured learning object that may contain multiple learning requirements.

Issues related to a curriculum may originate from:

- Curriculum configuration
- Learning item requirements
- Sub-curriculum relationships
- Assignment mechanisms
- Completion logic
- Effective dates
- User eligibility
- Retraining configuration

Before making configuration changes, determine whether the issue is related to the curriculum itself or to an individual learning item within the curriculum.

Do not assume that every incomplete curriculum indicates a system defect.

The curriculum may remain incomplete because one or more requirements have not been satisfied.

---

## Troubleshooting Steps

### 1. Identify the Curriculum

Collect the relevant information:

- Curriculum ID
- Curriculum title
- Affected user or users
- Expected behavior
- Actual behavior
- Current curriculum status
- Date when the issue began

Determine whether the issue involves:

- Curriculum visibility
- Assignment
- Completion
- Requirements
- Individual learning items
- Retraining
- Configuration changes

---

### 2. Check Curriculum Status

Verify the current status and configuration of the curriculum.

Check whether:

- The curriculum is active
- The curriculum is available
- The curriculum has been retired or made inactive
- Recent configuration changes were made

An inactive or incorrectly configured curriculum may not behave as expected.

---

### 3. Check Curriculum Assignment

Determine how the curriculum was assigned to the affected user.

Possible assignment mechanisms may include:

- Assignment Profile
- Manual assignment
- Other automatic assignment processes

If the curriculum is not appearing for the user, verify whether the user meets the assignment criteria before changing the curriculum configuration.

---

### 4. Review Curriculum Requirements

Review the learning requirements within the curriculum.

Check:

- Required learning items
- Optional learning items where applicable
- Requirement status
- Completion status of individual requirements
- Whether all required requirements have been satisfied

A curriculum may remain incomplete even when the user has completed some or most of the learning items.

Identify the specific requirement preventing completion.

---

### 5. Check Individual Learning Items

If the curriculum is incomplete, review the learning items associated with the curriculum.

Verify:

- Item status
- User completion status
- Assignment status
- Completion requirements
- Whether the item itself is behaving correctly

An issue with an individual item may affect the overall curriculum status.

---

### 6. Check Sub-Curriculum Relationships

Determine whether the curriculum contains sub-curricula or nested learning requirements.

If applicable, verify:

- Sub-curriculum status
- Completion status of requirements within the sub-curriculum
- Whether the parent curriculum depends on completion of the sub-curriculum

A parent curriculum may remain incomplete because a requirement within a sub-curriculum has not been completed.

---

### 7. Check Required vs Optional Requirements

Verify whether the user has completed all mandatory requirements.

Do not assume that completing optional items affects curriculum completion.

Identify:

- Mandatory requirements
- Optional requirements
- Requirements that remain incomplete

Focus troubleshooting on the requirements necessary for curriculum completion.

---

### 8. Check Curriculum Completion Logic

Determine why the curriculum is not showing as complete.

Check whether:

- All required learning items are complete
- All required sub-curricula are complete
- Any requirement remains active or incomplete
- Completion records are correctly reflected

If all requirements appear complete but the curriculum remains incomplete, investigate the relationship between the requirement records and the curriculum configuration.

---

### 9. Check Effective Dates and Recent Changes

Determine whether the curriculum was recently modified.

Check:

- Effective dates
- Recent requirement changes
- Added or removed learning items
- Curriculum updates
- Configuration changes

A recently added requirement may cause a previously completed curriculum to become incomplete or active again.

Compare the timing of the issue with recent configuration changes.

---

### 10. Check Assignment and User Eligibility

If the curriculum is not visible or assigned as expected, check:

- User attributes
- Assignment Profile criteria
- User eligibility
- User status
- Assignment processing

Do not treat an assignment issue as a curriculum configuration issue until the assignment mechanism has been verified.

---

### 11. Check Retraining Configuration When Relevant

If a previously completed curriculum becomes active again, investigate retraining configuration separately.

Check:

- Whether retraining is configured
- Retraining basis
- Retraining period
- Requirement dates

Refer to curriculum retraining troubleshooting when the issue involves repeated requirements or periodic reassignment.

---

### 12. Test the Configuration

Where appropriate, test the curriculum behavior with another user or test user.

Determine whether:

- The curriculum is assigned correctly
- Requirements appear correctly
- Completion is calculated as expected
- The issue is reproducible

This helps distinguish between:

- User-specific issues
- Curriculum configuration issues
- Individual learning item issues
- Assignment processing issues

---

### 13. Escalate When Required

If the issue cannot be explained through curriculum configuration and standard troubleshooting, collect relevant evidence and escalate to the appropriate support team.

---

## Decision Flow

User reports curriculum issue

→ Identify curriculum and affected user

→ Determine issue type

→ Check curriculum status

→ Check assignment mechanism

→ Review curriculum requirements

→ Identify incomplete requirement

→ Check individual learning items

→ Check sub-curriculum relationships

→ Check required vs optional requirements

→ Check completion logic

→ Check effective dates and recent changes

→ Check user eligibility and assignment processing

→ Check retraining if relevant

→ Test with another user

→ Investigate further or escalate

---

## Common Causes

Possible causes include:

- Curriculum is inactive or unavailable
- Curriculum was not assigned to the user
- Assignment criteria were not met
- Required learning item remains incomplete
- Sub-curriculum remains incomplete
- Mandatory requirement was not completed
- Individual learning item has a completion issue
- Recent curriculum changes introduced new requirements
- Effective date or configuration changes affected behavior
- Retraining configuration caused the curriculum to become active again

---

## Resolution Logic

First determine whether the issue relates to:

- Curriculum assignment
- Curriculum requirements
- Individual learning item completion
- Sub-curriculum completion
- Configuration changes
- Retraining

If a specific requirement is incomplete, investigate that requirement rather than changing the entire curriculum.

If all requirements appear complete but the curriculum remains incomplete, investigate curriculum completion logic and requirement records.

---

## Important Considerations

- Do not assume every incomplete curriculum is a system defect.
- Identify the exact requirement preventing completion.
- Individual item issues can affect curriculum completion.
- Sub-curricula can affect parent curriculum status.
- Assignment and configuration should be investigated separately.
- Recent curriculum changes may introduce new requirements.
- Retraining issues should be investigated separately from standard curriculum configuration.
- Test configuration changes before making broad updates.

---

## Evidence for Escalation

Collect:

- Curriculum ID
- Curriculum title
- Affected user ID
- Curriculum status
- Assignment method
- Requirement details
- Incomplete requirement details
- Learning item or sub-curriculum information
- Completion status
- Effective dates
- Recent configuration changes
- Test results
- Expected behavior
- Actual behavior

---

## Source Type

Expert Resolution Playbook

## Knowledge Sources

- Internal LMS incident-resolution experience
- SAP SuccessFactors Learning documentation
- SAP Knowledge Base Articles