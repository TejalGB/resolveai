# SAP Learning Assignment Issues - SF Knowledge

## Category

Learning Assignment and Availability

## Product

SAP SuccessFactors Learning

## Source Type

SAP Official Documentation and Knowledge Base Articles

## SAP References

- SAP Help Portal - Assigning Learning in SAP SuccessFactors Learning
- SAP Help Portal - Learning Assignments
- SAP Help Portal - Learning Item Availability
- SAP Support Knowledge Base - Learning Assignment Troubleshooting

---

## Knowledge Area: Learning Assignments

Learning can be assigned to users through different mechanisms in SAP SuccessFactors Learning.

An assignment may originate from:

- Assignment Profiles
- Curricula
- Programs
- Administrator assignment
- User self-assignment
- Automated business processes
- Retraining requirements

When a user reports that learning is missing, unavailable, or behaving unexpectedly, first identify whether the learning was actually assigned and determine the source of the assignment.

Assignment generation and assignment visibility should be investigated separately.

---

## Knowledge Area: Assigned Learning Not Visible

A user may report that a course was assigned but is not visible in their learning assignments.

When investigating this issue, verify:

- User ID
- Learning Item ID
- Learning Item status
- Whether the assignment exists
- Assignment source
- User status
- Learning availability
- Whether the issue affects one or multiple users

If the assignment exists but is not visible to the user, investigate assignment availability and learner-facing access.

Do not assume that a missing course automatically means the assignment was never created.

---

## Knowledge Area: Learning Item Availability

A learning assignment may exist while the learning item itself is unavailable.

Check whether the learning item is:

- Active
- Available to the applicable user population
- Correctly configured
- Associated with the required content
- Restricted by availability settings where applicable

A user may have an assignment but still experience difficulty accessing the learning content.

Assignment status and learning availability should therefore be checked separately.

---

## Knowledge Area: Assignment Source

Determine how the learning was assigned.

Possible assignment sources include:

- Assignment Profile
- Curriculum
- Program
- Administrator
- System-generated assignment
- Self-assignment
- Retraining requirement

The assignment source is important because different sources may control whether the assignment remains active.

Do not remove or modify an assignment before identifying its source.

---

## Knowledge Area: Missing Learning Assignment

If a user expects a course but cannot find it, determine whether the learning should actually be assigned.

Check:

- Assignment Profile membership
- Curriculum membership
- User eligibility
- Relevant user attributes
- Learning assignment rules
- Assignment processing status

If the user meets the expected assignment criteria but does not have the learning assigned, investigate whether the assignment process completed successfully.

---

## Knowledge Area: Assignment Status

Review the current status of the learning assignment.

Determine whether the assignment is:

- Active
- Completed
- Overdue
- Removed
- Reassigned
- Replaced by another requirement

The status should be interpreted together with Learning History and curriculum requirements.

For example, a completion record may exist even when another learning requirement remains active.

---

## Knowledge Area: Required Dates

Learning assignments may include required or due dates.

When investigating date-related issues, verify:

- Assignment date
- Required date
- Assignment source
- Curriculum requirements where applicable
- Retraining configuration where applicable

Incorrect or unexpected dates should not be changed without first identifying the mechanism that generated them.

---

## Knowledge Area: One User Versus Multiple Users

Determine the scope of the issue.

If one user is affected, investigate:

- User-specific assignment
- User attributes
- Assignment Profile membership
- Individual learning record

If multiple users are affected, investigate:

- Learning Item configuration
- Assignment rules
- Assignment Profile processing
- Curriculum configuration
- System-wide assignment behavior

The scope helps determine whether the issue is user-specific or configuration-related.

---

## Knowledge Area: Learning Assignment Versus Assignment Profile

Learning assignment issues should be distinguished from Assignment Profile issues.

Assignment Profiles determine whether learning is automatically assigned based on configured criteria.

Learning Assignment troubleshooting focuses on whether:

- The assignment was generated
- The assignment exists
- The assignment is visible
- The learning item is available
- The assignment status behaves as expected

If the underlying issue is why the user received the assignment, investigate Assignment Profiles or other assignment sources.

---

## Common Technical Investigation Points

When investigating learning assignment issues, collect:

- User ID
- Learning Item ID
- Learning Item title
- Assignment status
- Assignment source
- Assignment date
- Required date
- User attributes
- Curriculum or Program association
- Assignment Profile involvement
- Learning Item status
- Whether the issue affects one or multiple users

---

## Resolution Logic

User reports learning assignment issue

→ Identify the user

→ Identify the learning item

→ Determine whether the assignment exists

If NO:

→ Determine whether the user should receive the learning

→ Check Assignment Profiles, curriculum, program, or other assignment mechanisms

→ Verify assignment processing

If YES:

→ Check assignment status

→ Check whether the learning is visible to the user

→ Check Learning Item availability

→ Determine whether the learning item is active and accessible

If assignment source is unclear:

→ Review assignment information

→ Identify whether Assignment Profile, curriculum, administrator, or another mechanism created the assignment

If the issue affects one user:

→ Investigate user-specific data and assignment information

If multiple users are affected:

→ Investigate learning configuration or assignment rules

→ Correct through the approved process

→ Verify the assignment and learner access

---

## Important Considerations

- Always identify the source of a learning assignment.
- Assignment generation and assignment visibility are separate issues.
- An assignment may exist even if the learner cannot access the learning content.
- Do not assume that a missing course means the assignment was never generated.
- Check Learning Item status and availability.
- Assignment Profiles should be investigated separately when the issue concerns why learning was assigned.
- Curriculum and retraining requirements can affect assignment behavior.
- Do not manually remove or recreate assignments without identifying the underlying cause.
- Determine whether the issue affects one user or multiple users before investigating configuration.

---

## SAP References

SAP SuccessFactors Learning documentation explains that learning can be assigned through multiple mechanisms and managed through assignment processes.

SAP documentation distinguishes learning assignment, learner access, and automated assignment configuration.

For official SAP documentation and product-specific troubleshooting, refer to the SAP Help Portal and SAP Support Knowledge Base.