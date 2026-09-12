# Scheduled Offering Configuration Issues

## Category

Scheduled Offering and Class Configuration

## Product

SAP SuccessFactors Learning

## Incident

A user, instructor, administrator, or support team reports an issue related to a scheduled offering or class in SAP SuccessFactors Learning.

The issue may involve class visibility, registration, dates, capacity, instructors, locations, enrollment, availability, or completion processing.

## Problem Understanding

Scheduled offering issues should be separated from general learning item issues.

A learning item may be configured correctly while its scheduled offering has separate configuration problems.

Before troubleshooting, determine whether the issue relates to:

- Class visibility
- Registration
- Enrollment
- Capacity
- Schedule or dates
- Instructor assignment
- Location
- Completion
- User eligibility

Do not assume that the existence of a class means it is automatically available to every user.

---

## Troubleshooting Steps

### 1. Identify the Scheduled Offering

Collect:

- Scheduled Offering or Class ID
- Learning Item ID
- Class title
- Affected user ID
- Expected behavior
- Actual behavior
- Date and time of the class

Determine the exact type of issue before making configuration changes.

---

### 2. Check Scheduled Offering Status

Verify whether the scheduled offering is active and available.

Check:

- Class status
- Scheduled dates
- Start and end dates
- Whether the class has been cancelled
- Whether the registration period is active

An inactive, cancelled, or unavailable class may not appear to users.

---

### 3. Check Registration Dates

Verify the registration period.

Check:

- Registration start date
- Registration end date
- Current date relative to the registration period

A user may not be able to register if:

- Registration has not started
- Registration has closed
- The class is outside the configured registration window

---

### 4. Check Class Capacity

Verify whether the class has reached its maximum capacity.

Check:

- Maximum enrollment
- Current enrollment
- Waitlist configuration where applicable

A user may be unable to register because the class is full.

---

### 5. Check User Eligibility

Determine whether the user is eligible to view or register for the scheduled offering.

Check:

- User status
- Assignment or access
- Prerequisites
- Eligibility requirements
- Security or organizational restrictions where applicable

A scheduled offering may exist but still not be available to a particular user.

---

### 6. Check Learning Item and Scheduled Offering Association

Verify that the scheduled offering is correctly associated with the intended learning item.

Check:

- Learning Item ID
- Scheduled Offering configuration
- Associated instructors
- Relevant delivery settings

An incorrect association may cause unexpected behavior.

---

### 7. Check Instructor Configuration

If the issue involves instructor access or class delivery, verify:

- Instructor assignment
- Instructor permissions
- Relevant administrator roles
- Access to the scheduled offering

An instructor or administrator may require appropriate permissions to manage or access the class.

---

### 8. Check Location and Schedule Information

Verify the configured:

- Location
- Time zone where applicable
- Start date and time
- End date and time

Incorrect scheduling information may cause confusion regarding class availability or attendance.

---

### 9. Check Enrollment Status

Determine the user's current enrollment status.

Possible statuses may indicate:

- Successfully registered
- Waitlisted
- Withdrawn
- Pending
- Cancelled

Do not assume that a user is registered simply because they can see the scheduled offering.

---

### 10. Check Completion Processing

If the issue involves completion after attending a class, verify:

- Attendance status
- Completion processing
- Instructor or administrator actions
- Required completion records

Attending a class does not always automatically result in completion unless the required completion process has been performed.

---

### 11. Check Recent Configuration Changes

Determine whether the issue started after changes were made.

Check:

- Date changes
- Capacity changes
- Instructor changes
- Registration changes
- Status changes

Compare the timing of the issue with recent updates.

---

### 12. Test the Scheduled Offering

Where possible, test with another user or administrator.

Determine whether:

- The class is visible
- Registration is available
- Enrollment behaves correctly
- The issue is reproducible

This helps distinguish between:

- User-specific issues
- Configuration issues
- Access issues
- General system behavior

---

### 13. Escalate When Required

If standard troubleshooting does not identify the cause, collect relevant information and escalate to the appropriate support team.

---

## Decision Flow

User reports scheduled offering issue

→ Identify class and affected user

→ Determine issue type

→ Check scheduled offering status

→ Check dates and registration period

→ Check class capacity

→ Check user eligibility

→ Check learning item association

→ Check instructor configuration

→ Check location and schedule

→ Check enrollment status

→ Check completion processing if relevant

→ Check recent configuration changes

→ Test with another user

→ Investigate further or escalate

---

## Common Causes

Possible causes include:

- Scheduled offering is inactive or cancelled
- Registration period has not started
- Registration period has ended
- Class capacity has been reached
- User does not meet eligibility requirements
- Prerequisites are incomplete
- Incorrect learning item association
- Instructor configuration issue
- Incorrect schedule or location information
- User is waitlisted or withdrawn
- Completion processing was not completed
- Recent configuration changes affected the class

---

## Resolution Logic

First determine whether the issue occurs before registration, during enrollment, during class delivery, or after attendance.

For visibility issues:

→ Check class status, registration dates, and eligibility.

For registration issues:

→ Check registration period, capacity, prerequisites, and enrollment status.

For completion issues:

→ Check attendance and completion processing.

Do not investigate the learning item configuration alone when the issue is specific to a scheduled offering.

---

## Important Considerations

- A scheduled offering can exist without being available to every user.
- Registration windows control when users can enroll.
- Capacity limits may prevent registration.
- Enrollment status should be verified before assuming registration failed.
- Class attendance and LMS completion may require separate processing.
- Instructor and administrator access may depend on permissions.
- Recent configuration changes can affect scheduled offering behavior.

---

## Evidence for Escalation

Collect:

- Scheduled Offering ID
- Class title
- Learning Item ID
- Affected user ID
- Scheduled Offering status
- Registration dates
- Enrollment status
- Capacity information
- Instructor details where relevant
- Expected behavior
- Actual behavior
- Error messages
- Recent configuration changes
- Test results

---

## Source Type

Expert Resolution Playbook

## Knowledge Sources

- Internal LMS incident-resolution experience
- SAP SuccessFactors Learning documentation
- SAP Knowledge Base Articles