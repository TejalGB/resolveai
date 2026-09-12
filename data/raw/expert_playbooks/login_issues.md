# LMS Login Issues

## Category

User Access and Authentication

## Product

SAP SuccessFactors Learning

## Incident

A user is unable to log in to or access SAP SuccessFactors Learning.

## Problem Understanding

LMS login issues can originate from different points in the user lifecycle.

The user may be inactive in the source system, may be on Leave of Absence (LOA), may have incorrect user information, may be inactive in LMS even though they are active in the source system, or may not have been successfully synchronized into LMS.

The source-system status and LMS status should therefore be checked separately.

---

## Troubleshooting Steps

### 1. Check User Status in the Source System

Check whether the user's profile is active in the source employee/user system.

If the user is inactive because they are on Leave of Absence (LOA), access may not be available until the applicable return date.

Inform the user about the applicable access restriction and return date.

### 2. Check User Email ID

Verify that the user's email ID follows the expected corporate format.

For example:

`cdsid@example.com`

If the email information is incorrect, it should be corrected through the appropriate process.

If the required change must be made in the identity-management system, contact the relevant IDM team.

### 3. Compare Source-System and LMS Status

If the user is active in the source system, check whether the user is also active in LMS.

A difference between the two statuses may indicate a synchronization issue.

### 4. Check User Hire/Creation Date and Expected Synchronization Cycle

If the user is active in the source system but inactive or missing in LMS, first check the user's hire/profile creation date.

Determine when the user is expected to be picked up by the relevant synchronization process.

For example, if a user's profile was created on 29 August and the relevant synchronization process is expected to run on 30 August, the user may not appear in LMS until the next processing cycle.

This check helps distinguish between a normal synchronization delay and an actual synchronization failure.

Do not immediately assume that the User Connector has failed if the expected synchronization cycle has not yet occurred.

### 5. Check User Connector

Once the expected synchronization date or processing cycle has been established, check the relevant User Connector job or report for the applicable processing date.

Review whether the user was picked up and successfully processed.

Look for:

- Connector job failures
- Processing errors
- User-specific errors
- Whether the user was picked up by the synchronization process
- Whether the user was successfully processed
- Synchronization issues

If the relevant processing report retains limited historical information, use the report corresponding to the expected synchronization date.

For example:

**Profile created:** 29 August  
**Expected synchronization:** 30 August  
**Report to check:** 30 August synchronization report

### 6. Check Whether the User Was Processed

If applicable, verify whether the user's profile was included and successfully processed by the relevant synchronization job.

This helps determine whether the issue is related to the user not being picked up by the synchronization process or whether the synchronization itself failed.

### 7. Manual Synchronization

If the expected synchronization cycle has passed and the user was not successfully processed, and no relevant connector error explains the issue, the profile may be manually synchronized through the appropriate integration process.

The result should then be verified in LMS.

### 8. Recheck User Access

After correcting the source information or synchronizing the user, verify whether the LMS profile is active and whether the user can access the system.

If the user is active in both the source system and LMS, investigate other possible access or authentication factors.

---

## Decision Flow

User cannot access LMS

→ Check source-system status

→ Is user active?

**If NO:**

→ Check whether user is on LOA

→ Inform user about applicable access restriction/return date

**If YES:**

→ Check email information

→ Is email information correct?

**If NO:**

→ Correct through the appropriate process / contact IDM team

**If YES:**

→ Check LMS user status

→ Is user active in LMS?

**If NO:**

→ Check hire/profile creation date

→ Determine expected synchronization cycle

→ Has the expected synchronization cycle occurred?

**If NO:**

→ Allow the relevant synchronization cycle to occur

**If YES:**

→ Check User Connector report/job

→ Check whether the user was picked up and processed

→ Check for connector or user-specific errors

→ If required, manually synchronize the profile

→ Verify LMS status and access

**If YES:**

→ Investigate other possible access/authentication factors

---

## Common Causes

Common causes may include:

- User is inactive in the source system.
- User is on Leave of Absence.
- Incorrect user email information.
- User is active in the source system but inactive in LMS.
- Expected synchronization cycle has not yet occurred.
- User synchronization did not complete successfully.
- User Connector processing error.
- User profile was not picked up by the synchronization job.
- User-specific synchronization error.

---

## Resolution Logic

Source-system status

→ LOA check

→ User information

→ LMS status

→ Hire/profile creation date

→ Expected synchronization cycle

→ User Connector

→ Synchronization status

→ Manual synchronization if required

→ Verify access

---

## Important Considerations

- Do not assume every login issue is a password or authentication problem.
- Always distinguish between source-system status and LMS status.
- An LOA-related inactive status may be expected behavior.
- Check the user's hire/profile creation date before treating a synchronization delay as an error.
- Confirm that the expected synchronization cycle has occurred before escalating a synchronization issue.
- Use the synchronization report corresponding to the expected processing date.
- Changes to identity-related information may need to be handled by the appropriate identity-management team.
- Do not manually change or recreate user information without following the approved process.
- If synchronization is involved, check the connector before assuming that the LMS profile itself is defective.
- A user not appearing in LMS immediately after profile creation does not necessarily indicate a connector failure.

---

## Evidence for Escalation

If the issue cannot be resolved through standard troubleshooting, collect relevant information such as:

- User identifier
- Hire/profile creation date
- Source-system status
- LMS status
- Email information/status
- Expected synchronization date
- Relevant connector job/report
- Connector error details
- Whether the user was picked up by the synchronization process
- Synchronization result

Provide the collected evidence to the appropriate support team.

---

## Source Type

Expert Resolution Playbook

## Knowledge Sources

- Internal LMS incident-resolution experience
- SAP SuccessFactors Learning documentation
- SAP Knowledge Base Articles (to be added)