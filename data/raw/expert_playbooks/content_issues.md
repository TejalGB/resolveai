# Content Issues

## Category
Learning Content and Completion

## Product
SAP SuccessFactors Learning

## Incident

A user reports that they cannot launch learning content, the content does not work correctly, or the system does not record completion after the user finishes the content.

## Problem Understanding

Content-related issues can occur at different stages of the learning process:

1. The user cannot launch the content.
2. The content launches but displays an error.
3. The content works but does not record completion.
4. The content records completion incorrectly.
5. The user completes the content but the learning item remains assigned.

The first step is therefore to identify whether the problem is related to **launching, content behavior, completion tracking, or learning item configuration**.

---

## Common Scenarios

### 1. Content Does Not Launch

The user clicks the learning item but the content does not open.

Possible causes include:

- Incorrect content configuration.
- Broken or unavailable content.
- Incorrect content object configuration.
- Browser/session issues.
- Access or permission problems.
- Content package configuration problems.

First determine whether the issue affects only one user or multiple users.

### 2. Content Displays an Error

The user launches the content but receives an error such as:

- 404 error
- 403 error
- Session/logout issue
- Content loading error
- Blank page

Capture the exact error message and determine whether the problem is specific to the user, browser, content object, or learning item.

### 3. Content Does Not Mark the Learning Item Complete

The user completes the course but the learning item remains incomplete or assigned.

Possible causes include:

- Content did not send the expected completion status.
- Completion requirements were not satisfied.
- Item-level completion settings are incorrect.
- User did not complete all required content.
- Required survey or other completion activity was not completed.
- Content requires the user to exit/close/submit the course for completion to be recorded.
- SCORM/AICC communication is not working as expected.

### 4. SCORM/AICC Completion Issues

For SCORM or AICC content, the LMS depends on the content package communicating status and completion information correctly.

If the content reports a status that does not match the expected LMS configuration, the learning item may not be marked complete.

Check:

- Content type
- Content object
- Completion status sent by the content
- Item completion settings
- Expected completion status
- Content package configuration

### 5. Video Content Does Not Complete

Some video content may not communicate completion in the same way as SCORM/AICC content.

If the user watches the video but the learning item remains incomplete, check how the content object and learning item are configured to determine completion.

---

## Troubleshooting Steps

### 1. Identify the Exact Learning Item

Record:

- Learning item ID
- Learning item title
- Content object
- Content type
- Affected user ID

### 2. Reproduce the Issue

If possible:

- Self-assign the learning item.
- Launch the content.
- Perform the same steps as the user.
- Check whether the issue can be reproduced.

This helps determine whether the problem is user-specific or affects the learning item/content itself.

### 3. Check Whether the Content Launches

If the content does not launch:

- Record the exact error.
- Check whether other users experience the same issue.
- Check the content object configuration.
- Check whether the issue is browser/session specific.
- Check whether the content is available and correctly configured.

### 4. Check Completion Requirements

If the content launches successfully but does not complete, verify:

- All required sections were completed.
- Required links were accessed.
- Required surveys were completed.
- Required assessments were completed.
- The user followed the required exit/submit process.

Do not assume that simply opening or viewing the course means that the LMS should mark it complete.

### 5. Check Content Communication

For SCORM/AICC content, determine whether the content is sending the expected completion information to Learning.

Check for:

- Completion status
- Success status
- Exit status
- Communication/session issues

### 6. Check Item-Level Configuration

Review the learning item's completion-related settings and confirm that they match the content's expected behavior.

A correctly functioning content package can still fail to complete if the learning item is configured incorrectly.

### 7. Test With Another User

If possible, test the same content with another user.

Interpretation:

**Only one user affected**

→ Investigate user/browser/session/environment.

**Multiple users affected**

→ Investigate content object, learning item, or configuration.

### 8. Check Learning History

If the user believes they completed the content, check whether a completion record exists in Learning History.

If completion exists in history but the assignment remains active, investigate curriculum/retraining/assignment behavior rather than treating it purely as a content issue.

### 9. Determine Expected vs. Incorrect Behavior

If the content requires additional actions for completion:

→ Inform the user of the required steps.

If the content should have completed but did not:

→ Investigate content communication and learning item configuration.

If the issue affects multiple users:

→ Collect evidence and investigate/escalate the content configuration.

---

## Decision Flow

User reports content issue
→ Identify learning item
→ Identify content object/type
→ Determine whether content launches
→ Reproduce issue if possible

If content does not launch:
→ Check error
→ Check content/configuration
→ Check user/browser
→ Investigate or escalate

If content launches but does not complete:
→ Check completion requirements
→ Check user actions
→ Check content completion status
→ Check item configuration

If completion exists in Learning History:
→ Check assignment/curriculum/retraining behavior

If multiple users are affected:
→ Treat as potential content/configuration issue

If only one user is affected:
→ Investigate user/session/browser/environment

---

## Important Considerations

- Opening content does not necessarily mean that the learning item is complete.
- The LMS depends on content packages such as SCORM/AICC to communicate completion information where applicable.
- A completion issue may be caused by either the content or the learning item configuration.
- Required surveys, assessments, links, or other activities may be part of the completion requirement.
- Always capture the exact error message when content fails to launch.
- Reproducing the issue through self-assignment can help distinguish user-specific issues from learning item/content issues.
- If the learning item is part of a curriculum, investigate curriculum/retraining rules separately.

---

## Common Resolution

If the issue is caused by incomplete user actions, guide the user to complete the required steps.

If the content is not communicating completion correctly, investigate the content object/package and its configuration.

If the learning item configuration does not match the content's expected completion behavior, correct the configuration through the appropriate administration process.

If the issue cannot be resolved through configuration or user troubleshooting, collect the relevant technical details and escalate.

---

## Escalation Information

Provide:

- User ID
- Learning item ID
- Learning item title
- Content object ID
- Content type
- Exact error message
- Date/time of occurrence
- Browser/environment information
- Whether other users are affected
- Completion status reported by the content, if available
- Relevant screenshots
- Steps to reproduce
- Whether the issue occurs after self-assignment/testing

---

## Knowledge Sources

- Internal LMS incident-resolution experience
- SAP SuccessFactors Learning documentation
- SAP Knowledge Base Articles
- SCORM/AICC content documentation