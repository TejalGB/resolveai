# Assignment Profile Issues

## Category
Assignment Profiles and Learning Assignments

## Product
SAP SuccessFactors Learning

## Incident

A user reports that a learning item or curriculum was unexpectedly assigned, was not assigned when expected, or was assigned again after completion.

## Problem Understanding

Assignment Profiles in SAP SuccessFactors Learning automatically assign learning items and other learning objects to users based on defined user attributes and assignment criteria.

An assignment issue should therefore be investigated by determining:

- What was assigned?
- To whom was it assigned?
- Why should it have been assigned?
- Which Assignment Profile caused the assignment?
- Whether the user currently meets the Assignment Profile criteria
- Whether the assignment is manual, automatic, curriculum-based, or retraining-related

---

## Common Scenarios

### 1. Course Was Not Assigned to the User

A user expected to receive a course but cannot find it in their Learning Plan.

Possible causes include:

- User does not meet the Assignment Profile criteria.
- User attributes do not match the expected criteria.
- Assignment Profile has not been processed.
- Learning item is not included in the Assignment Profile.
- The Assignment Profile is inactive or not configured as expected.
- The user was recently created or their attributes were recently changed and synchronization/assignment processing has not occurred yet.

### 2. Course Was Assigned Unexpectedly

A user receives a learning item that they believe they should not have.

Check:

- Which Assignment Profile assigned the item.
- Whether the user's attributes match the profile criteria.
- Whether the user belongs to multiple Assignment Profiles.
- Whether the item was also manually assigned.
- Whether the item is part of a curriculum or other automatic assignment.

### 3. Course Was Assigned Again After Completion

A user reports:

> "I already completed this course. Why is it assigned again?"

Possible causes include:

- Retraining configuration.
- The course is part of a curriculum with retraining.
- The user belongs to multiple Assignment Profiles containing the same item.
- The course was manually assigned in addition to an Assignment Profile assignment.
- The user was removed from and later re-added to an Assignment Profile.
- User attributes changed, causing the user to enter an Assignment Profile again.
- The completed item exists as a free-floating assignment while another assignment mechanism assigns it again.

Do not assume that a repeated assignment is a system defect.

First determine the source of the assignment.

---

## Troubleshooting Steps

### 1. Identify the Learning Object

Determine what was assigned:

- Learning Item
- Curriculum
- Program
- Other learning object

Record the relevant ID if available.

### 2. Identify the User

Check the affected user's:

- User ID
- Active status
- Relevant attributes
- Organizational information
- Job-related information
- Other attributes used by Assignment Profiles

### 3. Determine How the Item Was Assigned

Check whether the assignment was:

- Automatically assigned through an Assignment Profile
- Manually assigned by an administrator
- Self-assigned by the user
- Assigned through a curriculum
- Generated through retraining

This distinction is important before making any configuration change.

### 4. Check Assignment Profiles

For the affected learning item, identify the Assignment Profiles that can assign it.

Review:

- Assignment Profile name
- Status
- Assignment criteria
- Learning item/curriculum included
- User population
- Processing status

### 5. Compare User Attributes With Assignment Criteria

Determine whether the affected user satisfies the criteria configured in the Assignment Profile.

For example, the profile may use:

- Location
- Organization
- Job Code
- Department
- Employee status
- Other user attributes

If the user meets the criteria, the assignment may be expected.

### 6. Check for Multiple Assignment Profiles

A user may belong to more than one Assignment Profile.

If the same learning item exists in multiple profiles, the item may be assigned through more than one assignment mechanism.

Do not immediately remove the assignment without determining why it exists.

### 7. Check Curriculum and Retraining

If the learning item is part of a curriculum, check:

- Curriculum assignment
- Requirement status
- Retraining configuration
- Initial completion
- Retraining period
- Retraining basis
- Basis date
- Effective date

A course appearing again after completion may be expected behavior when retraining is configured.

### 8. Check Assignment History / Assigned By

Where available, review assignment information to determine whether the item was assigned by:

- Assignment Profile
- Administrator
- System
- Other assignment mechanism

This can help identify the source of an unexpected assignment.

### 9. Consider Recent User Changes

If the issue started after a user change, check whether attributes such as:

- Location
- Department
- Job
- Organization
- Employee status

changed recently.

A change may cause the user to enter or leave an Assignment Profile population.

### 10. Determine Expected vs. Incorrect Assignment

After identifying the assignment source, determine whether the assignment is:

**Expected**

→ Explain the assignment reason to the user.

**Incorrect**

→ Follow the approved process to correct the Assignment Profile, user attributes, or assignment configuration.

Do not manually remove an assignment when an Assignment Profile or curriculum will automatically assign it again.

---

## Decision Flow

User reports assignment issue
→ Identify learning item/curriculum
→ Identify user
→ Determine assignment source
→ Check Assignment Profiles
→ Compare user attributes with profile criteria
→ Check multiple profiles
→ Check curriculum/retraining
→ Check assignment information

If assignment is expected:
→ Explain the reason

If assignment is incorrect:
→ Identify incorrect configuration
→ Correct through approved process

If assignment keeps returning:
→ Check Assignment Profile / curriculum / retraining
→ Do not repeatedly remove the assignment manually

If configuration appears correct:
→ Collect details
→ Escalate for further investigation

---

## Important Considerations

- Assignment Profiles are rule-based and can automatically assign learning.
- A user may belong to multiple Assignment Profiles.
- The same learning item may be assigned through multiple mechanisms.
- Removing an assignment manually may not resolve the underlying problem if an Assignment Profile continues to assign it.
- Retraining assignments should be investigated separately from unexpected Assignment Profile assignments.
- User attribute changes can affect Assignment Profile membership.
- Always identify the source of an assignment before changing it.
- Do not modify Assignment Profile criteria without confirming the intended business requirement.

---

## Common Resolution

If a user was correctly assigned through an Assignment Profile, explain why the assignment occurred.

If the user was incorrectly included in the Assignment Profile population, review the user's relevant attributes and/or Assignment Profile criteria according to the organization's approved process.

If the learning item is repeatedly assigned, identify whether the cause is:

- Multiple Assignment Profiles
- Curriculum assignment
- Retraining
- Manual assignment
- User attribute changes

Correct the underlying assignment mechanism rather than repeatedly removing the learning assignment.

---

## Escalation Information

When escalating, provide:

- User ID
- Learning item/curriculum ID
- Assignment Profile name
- Assignment Profile criteria
- User attributes relevant to the criteria
- Assignment source / Assigned By information
- Assignment date
- Completion date, if applicable
- Retraining configuration, if applicable
- Whether the user belongs to multiple Assignment Profiles
- Screenshots or relevant error messages, if available

---

## Knowledge Sources

- Internal LMS incident-resolution experience
- SAP SuccessFactors Learning documentation
- SAP Knowledge Base Articles
- Assignment Profile configuration and troubleshooting documentation