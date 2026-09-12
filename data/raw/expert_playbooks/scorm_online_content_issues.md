# SCORM and Online Content Issues

## Category

SCORM and Online Content

## Product

SAP SuccessFactors Learning

## Incident

A user reports that online learning content is not launching, is not loading correctly, does not record completion, or does not update the learning status in SAP SuccessFactors Learning.

The issue may involve SCORM packages, Content Objects, browser behavior, launch configuration, completion communication, or content-specific problems.

## Problem Understanding

Online content issues should not immediately be assumed to be LMS defects.

The problem may originate from:

- The SCORM package
- Content Object configuration
- Browser or session behavior
- Content launch settings
- Completion requirements
- Communication between the content and LMS
- Pop-up or browser restrictions
- User-specific issues

Before troubleshooting, determine whether the issue affects one user or multiple users.

This helps distinguish between a user-specific issue and a broader content or configuration issue.

---

## Troubleshooting Steps

### 1. Identify the Affected Content

Collect the relevant information:

- Learning Item ID
- Learning Item title
- Content Object ID
- Type of online content
- SCORM version if known
- Affected user ID
- Error message or screenshot
- Expected behavior
- Actual behavior

Determine whether the issue involves:

- Content launch
- Content loading
- Completion
- Progress tracking
- Browser behavior
- Error messages

---

### 2. Determine the Scope of the Issue

Check whether the problem affects:

- One user
- Multiple users
- All users accessing the content

If only one user is affected, investigate:

- Browser cache
- Session issues
- Browser configuration
- User-specific learning records

If multiple users experience the same issue, investigate the content package or Content Object configuration.

---

### 3. Check Learning Item and Content Object Association

Verify that the correct Content Object is associated with the learning item.

Check:

- Whether the Content Object exists
- Whether it is active
- Whether the correct version is associated
- Whether recent content updates were made
- Whether the content was replaced

An incorrect or inactive Content Object may prevent the learning content from functioning correctly.

---

### 4. Check Whether the Content Launches

Ask the user whether the content:

- Opens successfully
- Opens in a new window or browser tab
- Remains blank
- Displays an error
- Closes unexpectedly

If the content does not launch, investigate browser restrictions and Content Object configuration.

---

### 5. Check Browser and Pop-Up Restrictions

Verify whether browser settings may be preventing the content from launching correctly.

Check:

- Pop-up blockers
- Browser restrictions
- Cached data
- Session issues
- Browser compatibility

Ask the user to:

- Clear browser cache
- Try another supported browser where appropriate
- Allow pop-ups if required
- Start a new session and retry

---

### 6. Check Completion Requirements

If the content launches but does not show as complete, verify whether the learner completed all required activities.

Depending on the content, completion may require:

- Viewing all required sections
- Completing assessments
- Passing a quiz
- Opening required links
- Completing required interactions
- Reaching the configured completion threshold

Launching or partially viewing SCORM content does not necessarily result in completion.

---

### 7. Check LMS Communication and Completion Status

Determine whether the online content successfully communicates completion information back to LMS.

Check whether:

- The content shows completion internally
- The LMS learning item remains incomplete
- Progress is saved correctly
- Completion is recorded in Learning History

If the content indicates completion but LMS does not update the status, investigate the content package and LMS communication behavior.

---

### 8. Test the Content Independently

Where possible, self-assign the learning item or test it using another user.

Determine whether:

- The content launches successfully
- Progress is saved
- Completion is recorded
- The issue can be reproduced

This helps distinguish between:

- User-specific issues
- Content package issues
- LMS configuration issues

---

### 9. Check Recent Content Changes

Determine whether the issue started after changes were made to the content.

Check:

- New SCORM package upload
- Content replacement
- New content version
- Content Object changes
- Learning Item changes

Compare the timing of the issue with recent updates.

---

### 10. Investigate SCORM Package Issues

If the issue is reproducible across users, the SCORM package itself may require investigation.

Possible issues may include:

- Incorrect packaging
- Manifest problems
- SCORM communication issues
- Completion status configuration
- Content errors
- Unsupported behavior

Where appropriate, involve the content provider or content development team.

---

### 11. Check Learning History

If the user reports successful completion but the assignment remains incomplete, verify whether a completion record exists in Learning History.

If completion exists:

- Check curriculum requirements
- Check retraining configuration
- Check assignment behavior

Do not assume that an active assignment means the SCORM content failed.

---

### 12. Escalate When Required

If the issue is reproducible and cannot be resolved through browser, configuration, or standard troubleshooting, collect relevant evidence and escalate.

Include details about:

- Learning Item
- Content Object
- SCORM package
- User
- Browser
- Error messages
- Test results

---

## Decision Flow

User reports online content issue

→ Identify learning item and Content Object

→ Determine whether issue affects one or multiple users

→ Check content association

→ Check whether content launches

→ Check browser and pop-up restrictions

→ Check completion requirements

→ Check LMS communication and completion status

→ Test with another user

→ Check recent content changes

→ Investigate SCORM package if reproducible

→ Check Learning History

→ Escalate if required

---

## Common Causes

Possible causes include:

- Incorrect Content Object association
- Inactive or incorrect content version
- Browser cache or session issue
- Pop-up blocker
- Browser compatibility issue
- Required content activities not completed
- SCORM package communication issue
- SCORM completion configuration issue
- Recent content replacement
- User-specific learning record issue
- Content package error

---

## Resolution Logic

First determine whether the issue occurs during:

- Launch
- Content loading
- Progress tracking
- Completion
- LMS status update

Then determine whether the issue affects one user or multiple users.

One user affected:

→ Investigate browser, session, and user-specific issues.

Multiple users affected:

→ Investigate Content Object configuration and the SCORM package.

Content completed internally but LMS remains incomplete:

→ Investigate LMS communication, completion records, and assignment behavior.

---

## Important Considerations

- Do not assume every SCORM issue is an LMS defect.
- Launching content does not guarantee completion.
- Internal content completion and LMS completion should be distinguished.
- Browser and pop-up restrictions can affect launch behavior.
- Testing with another user helps identify reproducibility.
- Recent content changes may explain newly occurring issues.
- If multiple users experience the same issue, investigate the content package.

---

## Evidence for Escalation

Collect:

- Learning Item ID
- Learning Item title
- Content Object ID
- SCORM version if known
- Affected user ID
- Browser and version
- Error message
- Screenshot where available
- Expected behavior
- Actual behavior
- Whether the issue is reproducible
- Test results
- Recent content changes

---

## Source Type

Expert Resolution Playbook

## Knowledge Sources

- Internal LMS incident-resolution experience
- SAP SuccessFactors Learning documentation
- SAP Knowledge Base Articles