# SAP Learning History and Completion - SF Knowledge

## Category

Learning History and Completion Management

## Product

SAP SuccessFactors Learning

## Source Type

SAP Official Documentation and Knowledge Base Articles

## SAP References

- SAP Help Portal - Learning History in SAP SuccessFactors Learning
- SAP Help Portal - Recording Learning Completion
- SAP Help Portal - Item Completion and Learning History
- SAP Support Knowledge Base - Learning Completion Troubleshooting

---

## Knowledge Area: Learning History

Learning History stores records of learning activities that have been successfully completed or otherwise recorded for a user.

A learning item may appear in Learning History after completion is successfully processed and recorded in SAP SuccessFactors Learning.

When a user reports that a course was completed but is not visible in Learning History, the investigation should distinguish between:

- Content completion
- LMS completion status
- Learning History record creation
- Assignment status
- Curriculum or retraining requirements

Completion inside online content does not always automatically confirm that the LMS has successfully recorded the completion.

---

## Knowledge Area: Completion Status

A learning activity can have different statuses depending on the learning process and configuration.

When investigating a completion issue, determine:

- Whether the user completed the required learning activity
- Whether the content reported completion to LMS
- Whether the LMS recorded the completion
- Whether a Learning History record exists
- Whether the assignment remains active for another reason

A course appearing as incomplete does not always mean that the user failed to complete the content.

The issue may occur during communication between the learning content and LMS or during completion processing.

---

## Knowledge Area: Online Content Completion

For online learning content, completion information may be communicated from the content package to SAP SuccessFactors Learning.

The learner may complete the content internally while the LMS does not receive or process the completion status correctly.

When investigating online completion issues, check:

- Whether the content itself shows completion
- Whether all required activities were completed
- Whether assessments or quizzes were passed where required
- Whether the LMS received the completion status
- Whether progress was saved
- Whether a Learning History record was created

If the content shows completion but LMS remains incomplete, investigate content-to-LMS communication and completion processing.

---

## Knowledge Area: Learning History Record

When a completion is successfully recorded, verify the relevant Learning History entry.

Check:

- User
- Learning Item
- Completion status
- Completion date
- Completion type where applicable
- Whether the correct learning item was recorded

If no Learning History record exists, determine whether the completion was successfully processed.

If a Learning History record exists but the assignment remains active, investigate assignment rules, curriculum requirements, or retraining configuration separately.

---

## Knowledge Area: Assignment Remaining After Completion

A completed learning item may still appear as assigned for reasons unrelated to a missing completion record.

Possible reasons may include:

- Curriculum requirements
- Retraining requirements
- Recurring training
- New assignment generation
- Assignment Profile assignment
- Multiple assignment mechanisms

Therefore, the following should be checked separately:

1. Was the completion successfully recorded?
2. Does the completion appear in Learning History?
3. Why does the assignment remain active?

Do not assume that an active assignment automatically means the completion failed.

---

## Knowledge Area: Scope of the Issue

Determine whether the issue affects:

- One user
- Multiple users
- One learning item
- Multiple learning items

If one user is affected, investigate:

- User-specific learning records
- Browser or session issues
- Individual completion processing

If multiple users are affected for the same learning item, investigate:

- Learning Item configuration
- Online content configuration
- Content package behavior
- Completion processing

The scope of the issue helps determine whether the problem is user-specific or configuration-related.

---

## Knowledge Area: Completion Date Issues

When investigating an incorrect completion date, determine:

- When the learning was actually completed
- When the completion was recorded
- Whether the completion was manually recorded
- Whether the completion originated from online content
- Whether historical completion information was imported or updated

The completion record should be reviewed before modifying any Learning History information.

Changes to completion records should follow the approved support or administration process.

---

## Common Technical Investigation Points

Investigate the following when Learning History or completion issues occur:

- Learning Item ID
- User ID
- Completion status
- Learning History record
- Completion date
- Online content status
- Assessment or quiz completion
- Content-to-LMS communication
- Assignment status
- Curriculum association
- Retraining configuration
- Whether the issue affects one or multiple users

---

## Resolution Logic

User reports course completed but status is incorrect

→ Verify the learning activity was completed

→ Check whether the content reports completion internally

→ Check whether LMS received the completion status

→ Check Learning History

→ Does a completion record exist?

If NO:

→ Investigate completion processing

→ Check online content communication where applicable

→ Check whether the issue affects other users

If YES:

→ Verify completion details

→ Check why the assignment remains active

→ Investigate curriculum, retraining, or assignment rules separately

If completion is incorrect:

→ Review the applicable learning record

→ Correct according to the approved support process

→ Verify the updated Learning History status

---

## Important Considerations

- Completion inside learning content and LMS completion should be treated separately.
- A completed course does not always immediately indicate that a Learning History record was successfully created.
- An active assignment does not necessarily mean that completion failed.
- Curriculum and retraining requirements may create additional learning requirements after completion.
- Check Learning History before modifying assignments.
- Determine whether the issue affects one user or multiple users.
- Do not modify completion records without following the approved process.
- Investigate the source of the completion issue before making configuration changes.

---

## SAP References

SAP SuccessFactors Learning documentation describes Learning History as the record of completed learning activities.

SAP documentation distinguishes learning completion processing, assignment status, and Learning History records.

For official SAP documentation and product-specific troubleshooting, refer to the SAP Help Portal and SAP Support Knowledge Base.