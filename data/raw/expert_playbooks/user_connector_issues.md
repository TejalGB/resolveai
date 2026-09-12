# User Connector and Synchronization Issues

## Category

User Connector and User Synchronization

## Product

SAP SuccessFactors Learning

## Incident

A user is missing from LMS, inactive in LMS, has outdated information, or user information from the source system has not synchronized correctly into SAP SuccessFactors Learning.

The issue may involve User Connector processing, synchronization timing, source-system data, user-specific errors, connector job failures, or profile update delays.

## Problem Understanding

User information in SAP SuccessFactors Learning may originate from an external source system and be transferred through scheduled synchronization processes.

Therefore, a user issue does not necessarily originate in LMS.

The problem may exist in:

- Source-system user data
- User Connector processing
- Synchronization timing
- User-specific connector errors
- Connector job failures
- Identity or profile information
- LMS user status

Before manually changing user information, first determine whether the expected synchronization process has occurred.

Do not assume that a missing or outdated LMS profile means the LMS profile itself is defective.

---

## Troubleshooting Steps

### 1. Identify the Affected User

Collect:

- User ID
- Username
- Email address
- Source-system status
- LMS status
- Hire or profile creation date
- Expected user information
- Actual user information

Determine whether the issue involves:

- Missing user
- Inactive user
- Incorrect user information
- Missing profile updates
- Synchronization delay

---

### 2. Check Source-System User Status

Verify the user's status in the source system.

Check whether the user is:

- Active
- Inactive
- On Leave of Absence
- Recently hired
- Recently reactivated

If the user is inactive in the source system, the LMS status may be expected behavior.

Always distinguish between source-system status and LMS status.

---

### 3. Check LMS User Status

Verify whether the user exists and is active in SAP SuccessFactors Learning.

Compare:

- Source-system status
- LMS status
- User attributes
- Email information
- Organizational information

A mismatch may indicate a synchronization issue.

---

### 4. Check Hire Date or Profile Creation Date

Determine when the user was created or when relevant information was changed.

Check whether:

- The user is newly created
- The profile was recently updated
- The expected synchronization cycle has occurred

A recently created user may not immediately appear in LMS.

Do not treat this as a connector failure until the expected synchronization timing has been considered.

---

### 5. Check User Connector Job or Report

Review the relevant User Connector job or synchronization report.

Determine whether:

- The connector job completed successfully
- The user was picked up by the job
- The user was processed successfully
- Errors were reported
- The job failed or partially completed

Use the report corresponding to the expected synchronization cycle.

---

### 6. Check User-Specific Errors

If the connector job completed but the affected user was not updated correctly, investigate user-specific errors.

Check for:

- Invalid user data
- Missing required information
- Incorrect attributes
- Email issues
- Organizational data issues
- Other connector validation errors

A successful connector job does not necessarily mean every individual user was processed successfully.

---

### 7. Check Source Data Accuracy

Verify that the source-system information is correct.

Pay attention to:

- User status
- Email address
- Username
- Organizational information
- Job-related attributes
- Other attributes required for LMS processing

If the source information is incorrect, it may need to be corrected through the appropriate source system or identity-management process.

---

### 8. Check Synchronization Timing

Determine the expected processing schedule.

Check:

- When the relevant change was made
- When the next synchronization cycle was expected
- Whether the cycle has completed

Do not escalate a synchronization issue before the expected processing window has passed.

---

### 9. Reprocess or Synchronize Where Appropriate

If the source information is correct and the expected synchronization cycle has completed but the LMS profile was not updated:

- Review connector errors
- Confirm whether the user was picked up
- Determine whether reprocessing is available
- Perform manual synchronization only according to the approved support process

Do not manually recreate or modify user information without following the appropriate process.

---

### 10. Verify the Updated LMS Profile

After synchronization or corrective action, verify:

- User exists in LMS
- User is active where expected
- Relevant attributes are updated
- User can access LMS where applicable

Confirm that the issue has been resolved.

---

### 11. Escalate When Required

If the issue cannot be resolved through source data verification and standard connector troubleshooting, escalate with the relevant evidence.

---

## Decision Flow

User profile issue reported

→ Identify affected user

→ Check source-system status

→ Check LMS status

→ Compare source and LMS information

→ Check hire/profile creation date

→ Determine expected synchronization cycle

→ Has synchronization cycle occurred?

**If NO:**

→ Wait for expected processing cycle

→ Recheck LMS profile

**If YES:**

→ Check User Connector job/report

→ Was user picked up?

**If NO:**

→ Investigate source data and connector selection

**If YES:**

→ Check user-specific processing errors

→ Correct source data if required

→ Reprocess according to approved process

→ Verify LMS profile

→ Escalate if unresolved

---

## Common Causes

Possible causes include:

- User is inactive in the source system
- User is on Leave of Absence
- User was recently hired
- Expected synchronization cycle has not occurred
- User Connector job failed
- User was not picked up by the connector
- User-specific validation error occurred
- Incorrect email information
- Missing required source data
- Incorrect organizational information
- Source-system and LMS status mismatch

---

## Resolution Logic

First determine whether the issue is caused by:

- Source-system data
- Synchronization timing
- Connector processing
- User-specific processing errors
- LMS profile status

If the expected synchronization cycle has not occurred, wait for the relevant processing cycle.

If the cycle has occurred, use the connector report to determine whether the user was picked up and processed.

If the source data is incorrect, correct it through the appropriate approved process before attempting further synchronization.

---

## Important Considerations

- Do not assume every LMS user issue is an LMS defect.
- Always compare source-system and LMS status.
- Newly created users may require time for synchronization.
- A successful connector job may still contain user-specific errors.
- Use the connector report corresponding to the relevant processing date.
- Do not manually recreate user profiles without following approved procedures.
- Identity-related information may need to be corrected by the appropriate source or IDM team.
- Verify the LMS profile after synchronization.

---

## Evidence for Escalation

Collect:

- User ID
- Username
- Source-system status
- LMS status
- Hire/profile creation date
- Relevant source information
- Expected synchronization date
- Connector job or report
- Whether the user was picked up
- Connector processing result
- User-specific error details
- Expected behavior
- Actual behavior

---

## Source Type

Expert Resolution Playbook

## Knowledge Sources

- Internal LMS incident-resolution experience
- SAP SuccessFactors Learning documentation
- SAP Knowledge Base Articles