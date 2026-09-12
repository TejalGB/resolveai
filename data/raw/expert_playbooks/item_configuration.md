# Learning Item Configuration Issues

## Category

Learning Item Configuration

## Product

SAP SuccessFactors Learning

## Incident

A user, administrator, or support team reports that a learning item is not behaving as expected.

The issue may involve item visibility, availability, assignment behavior, completion settings, content association, effective dates, prerequisites, or incorrect item configuration.

## Problem Understanding

A learning item issue does not always indicate a system defect.

The behavior may be caused by the item's configuration, assignment mechanism, availability settings, associated content, or relationship with curricula and other learning objects.

Before making changes, first determine:

- Which learning item is affected
- Whether the issue affects one user or multiple users
- Whether the item is active and available
- How the item was assigned
- Whether the item is associated with a curriculum
- Whether recent configuration changes were made

Do not assume that changing the item configuration will immediately resolve the issue without understanding the assignment and completion logic.

---

## Troubleshooting Steps

### 1. Identify the Learning Item

Collect the relevant information:

- Item ID
- Item title
- Item type
- Current item status
- Affected user or users
- Expected behavior
- Actual behavior

Determine whether the issue affects:

- Item visibility
- Assignment
- Launch or content access
- Completion
- Availability
- Configuration

---

### 2. Check Item Status

Verify that the learning item is active and configured as expected.

Check whether:

- The item is active
- The item is available to the relevant users
- The item has been retired or made inactive
- Recent configuration changes were made

An inactive or unavailable item may not behave as expected for users.

---

### 3. Check Item Assignment

Determine how the learning item was assigned.

Possible assignment mechanisms include:

- Assignment Profile
- Curriculum
- Manual assignment
- Other automatic assignment processes

If the item is not appearing for a user, do not investigate item configuration alone.

Also verify whether the user was expected to receive the assignment.

---

### 4. Check Availability and User Access

Verify whether the affected user should be able to access the learning item.

Check:

- User status
- Assignment status
- Library availability where applicable
- User eligibility
- Security or access restrictions where relevant

An item may exist and be active but still not be visible or available to a specific user.

---

### 5. Check Associated Content

If the learning item contains online learning content, verify the associated Content Object or content configuration.

Check:

- Whether content is associated correctly
- Whether the correct content version is being used
- Whether the content is active and available
- Whether recent content changes were made

For SCORM-specific launch or completion issues, investigate the online content separately.

---

### 6. Check Completion Configuration

If the issue relates to completion, determine what is required for the item to be marked complete.

Depending on the learning item, completion may depend on:

- Online content completion
- Assessment completion
- Required activities
- Instructor or administrator actions
- Scheduled offering attendance
- Other configured completion requirements

Do not assume that opening or launching the item automatically results in completion.

---

### 7. Check Prerequisites and Requirements

Verify whether the learning item has prerequisites or other requirements that affect user access or completion.

Check whether:

- Required prerequisites have been completed
- The user meets the relevant requirements
- The item is part of a larger learning structure

A prerequisite or related requirement may explain why the user cannot proceed as expected.

---

### 8. Check Curriculum Association

Determine whether the learning item is part of a curriculum.

If it is:

- Check the curriculum requirement
- Determine whether the item is required or optional
- Check whether the curriculum controls assignment behavior
- Investigate retraining separately if the item was assigned again

The item's behavior may be influenced by curriculum configuration rather than the item itself.

---

### 9. Check Effective Dates and Recent Changes

Determine whether recent configuration changes may have affected behavior.

Check:

- Item effective date
- Recent item updates
- Content replacement
- Assignment changes
- Curriculum changes

Compare the timing of the issue with recent configuration changes.

---

### 10. Test with Another User

Where appropriate, test the learning item with another user or administrator.

Determine whether:

- The item is visible
- The item can be accessed
- The item can be completed
- The issue is reproducible

This helps distinguish between:

- User-specific issues
- Item configuration issues
- Content issues
- General system behavior

---

### 11. Escalate When Required

If the issue cannot be resolved through configuration and standard troubleshooting, collect relevant information and escalate to the appropriate support team.

---

## Decision Flow

User reports learning item issue

→ Identify item and affected user

→ Determine issue type

→ Check item status

→ Check assignment mechanism

→ Check availability and user access

→ Check associated content

→ Check completion configuration

→ Check prerequisites

→ Check curriculum association

→ Check effective dates and recent changes

→ Test with another user

→ Determine configuration issue vs. user-specific issue

→ Investigate further or escalate

---

## Common Causes

Possible causes include:

- Item is inactive or unavailable
- Item was not assigned to the user
- Assignment mechanism did not process as expected
- User does not meet eligibility requirements
- Content is incorrectly associated
- Content was recently replaced or changed
- Completion requirements were not met
- Prerequisites were not completed
- Curriculum configuration affects item behavior
- Recent configuration changes affected availability

---

## Resolution Logic

First determine whether the issue originates from the learning item configuration, assignment mechanism, user access, associated content, or curriculum relationship.

If the item configuration is correct, investigate the relevant related component rather than repeatedly changing the item.

For example:

Item visibility issue
→ Check assignment and availability.

Completion issue
→ Check completion requirements and associated content.

Repeated assignment
→ Check curriculum and retraining.

Launch issue
→ Check online content and Content Object configuration.

---

## Important Considerations

- Do not assume every item issue is caused by item configuration.
- Assignment behavior and item configuration should be investigated separately.
- An active item may still be unavailable to a particular user.
- Curriculum relationships can affect assignment and completion behavior.
- Associated content may introduce separate launch or completion issues.
- Test changes before making broad configuration updates.
- Compare affected and unaffected users where possible.

---

## Evidence for Escalation

Collect:

- Item ID
- Item title
- Affected user ID
- Item status
- Assignment method
- Curriculum association
- Content Object information if applicable
- Expected behavior
- Actual behavior
- Date and time issue began
- Recent configuration changes
- Test results

---

## Source Type

Expert Resolution Playbook

## Knowledge Sources

- Internal LMS incident-resolution experience
- SAP SuccessFactors Learning documentation
- SAP Knowledge Base Articles