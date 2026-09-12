# Class and Enrollment Issues

## Category
Instructor-Led Training and Class Enrollment

## Product
SAP SuccessFactors Learning

## Incident

A user reports that they cannot register for a class, cannot find an expected class, cannot enroll in a scheduled offering, or encounters an error while attempting to register.

Administrators may also report issues related to class configuration, enrollment, instructors, or scheduled offerings.

---

## Problem Understanding

Instructor-Led Training (ILT) in SAP SuccessFactors Learning involves learning items, classes, scheduled offerings, enrollment rules, instructors, locations, and potentially costs or chargebacks.

An enrollment issue should therefore be investigated by identifying:

- The learning item
- The specific class/scheduled offering
- The user's eligibility
- Registration settings
- Availability/capacity
- Enrollment restrictions
- Required approvals
- Cost or chargeback configuration
- Whether the issue affects one user or multiple users

---

## Common Scenarios

### 1. User Cannot Register for a Class

Possible causes include:

- Self-registration is disabled.
- The class is not available to the user.
- The learning item is not available in the user's Library.
- The class is full.
- Registration dates have passed.
- The user does not meet enrollment requirements.
- An approval process is required.
- A configuration issue prevents registration.

### 2. User Cannot Find the Class

Check:

- Learning item availability.
- Library availability.
- Class/scheduled offering status.
- Registration period.
- User access.
- User eligibility.

A class may exist in LMS but still not be available to a particular user.

### 3. Self-Enrollment Is Not Available

For self-registration, verify:

- The learning item is configured to allow self-registration.
- The learning item is available to the user.
- The relevant class is available.
- The user has access to the required Library.
- Any prerequisites or restrictions are satisfied.

### 4. Class Registration Error

If the user receives an error during registration:

- Capture the exact error message.
- Identify the affected class.
- Determine whether the issue affects one user or multiple users.
- Check class configuration.
- Check enrollment settings.
- Check cost/chargeback configuration if applicable.

### 5. Cost or Chargeback-Related Registration Issue

Some instructor-led classes may have cost or chargeback information associated with them.

If registration is blocked because additional administrative configuration is required, check whether the relevant cost center, chargeback, or financial configuration is correctly maintained.

Do not modify financial configuration without following the organization's approved process.

### 6. User Wants to Register for Another Class/Cohort

A user may be prevented from registering for another class of the same learning item.

Check whether the learning item has restrictions on multiple class registrations within a defined period.

---

## Troubleshooting Steps

### 1. Identify the Learning Item

Record:

- Learning item ID
- Learning item name
- Class/scheduled offering ID
- Class date
- Location
- Instructor, if relevant

### 2. Identify the User

Record:

- User ID
- Active status
- Relevant eligibility information
- Organization/location/job information if applicable

### 3. Check Class Status

Verify:

- Class exists.
- Class is active/available.
- Registration period is open.
- Seats are available.
- The class has not been cancelled or closed.

### 4. Check Learning Item Availability

Confirm that the user can access the learning item.

Check:

- Library availability
- User eligibility
- Assignment/availability configuration

### 5. Check Registration Configuration

Verify:

- Self-registration setting
- Enrollment restrictions
- Approval requirements
- Prerequisites
- Registration deadlines
- Capacity restrictions

### 6. Check Multiple Class Registration Restrictions

If the user is trying to register for another cohort of the same learning item, check whether the learning item has a configured restriction preventing multiple class registrations within a specified interval.

### 7. Check Cost/Chargeback Configuration

If the error indicates that administrator action is required before registration can occur, investigate the relevant cost or chargeback configuration.

### 8. Reproduce the Issue

If possible:

- Test with the affected user.
- Test with another eligible user.
- Compare available classes.
- Attempt registration through the same process.

This helps determine whether the problem is user-specific or class/configuration-specific.

### 9. Determine Expected vs. Incorrect Behavior

If the user is not eligible:

→ Explain the eligibility requirement.

If the class is full/closed:

→ Provide available alternatives where appropriate.

If registration is blocked by configuration:

→ Correct the configuration through the approved administration process.

If the configuration appears correct but registration still fails:

→ Collect evidence and escalate.

---

## Decision Flow

User cannot enroll
→ Identify learning item and class
→ Check class status
→ Check registration period
→ Check capacity
→ Check user eligibility
→ Check Library/access
→ Check self-registration
→ Check prerequisites/approval
→ Check multiple registration restrictions
→ Check cost/chargeback configuration

If expected restriction:
→ Explain to user

If configuration issue:
→ Correct through approved process

If configuration appears correct:
→ Reproduce and escalate

---

## Important Considerations

- A learning item being visible does not necessarily mean every class is available for registration.
- Class availability can depend on the user's access, eligibility, registration settings, capacity, and dates.
- Self-registration requires the relevant configuration and availability.
- A registration problem can be caused by financial/chargeback configuration.
- Always distinguish between a **learning item issue** and a **specific scheduled offering/class issue**.
- Do not change financial, enrollment, or administrative configuration without confirming the business requirement.
- If only one user is affected, investigate user-specific eligibility/access before changing the class configuration.

---

## Common Resolution

If the user is not eligible or the class is unavailable, explain the applicable restriction and provide an alternative where appropriate.

If self-registration or class configuration is incorrect, update the configuration through the appropriate administration process.

If the issue is related to cost/chargeback configuration, follow the approved financial administration process.

If the issue persists despite correct configuration, collect the relevant details and escalate.

---

## Escalation Information

Provide:

- User ID
- Learning item ID
- Class/scheduled offering ID
- Class date
- Exact error message
- Registration attempt date/time
- User eligibility information
- Registration configuration
- Capacity/availability
- Cost/chargeback information, if relevant
- Screenshots
- Steps to reproduce
- Whether other users are affected

---

## Knowledge Sources

- Internal LMS incident-resolution experience
- SAP SuccessFactors Learning documentation
- SAP Knowledge Base Articles
- Instructor-Led Training and enrollment documentation