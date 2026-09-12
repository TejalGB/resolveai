# SAP Curriculum and Retraining - SF Knowledge

## Category

Curricula and Retraining

## Product

SAP SuccessFactors Learning

## Source Type

SAP Official Documentation and Knowledge Base Articles

## SAP References

- SAP Help Portal - Retraining in SAP SuccessFactors Learning Curricula
- SAP Help Portal - Curriculum Content Settings
- SAP Help Portal - Retraining and Assignment in Curricula
- SAP Help Portal - Curriculum Retraining Period Time Units
- SAP Help Portal - User Curriculum Details Information
- SAP Help Portal - Walk Through of Event-Based Period Assignment in SAP SuccessFactors Learning Curricula

---

## Knowledge Area: Curricula and Learning Qualification

In SAP SuccessFactors Learning, curricula are used to organize learning items into structured qualification requirements.

A curriculum can contain learning items that users must complete to achieve or maintain qualification.

Retraining can be configured within curricula when users are required to periodically complete the same learning again.

For example, a user may be required to complete a course every year to maintain qualification.

Retraining is configured at the curriculum content level and determines how future learning requirements are calculated.

---

## Knowledge Area: Retraining Behavior

When retraining is configured for a learning item in a curriculum, the learning item can remain assigned to the user even after completion.

The system recalculates the next required date according to the retraining configuration.

From the learner's perspective, the learning item may appear to remain permanently assigned.

For example:

A user completes a course with annual retraining.

Instead of disappearing permanently from the user's assignments, the course remains associated with the curriculum and the next required date is calculated for the next retraining period.

Therefore, a completed course appearing again or remaining assigned does not automatically indicate an incorrect assignment.

---

## Knowledge Area: Initial Training and Retraining

Curriculum content can have separate configurations for:

- Initial training
- Retraining

The initial training configuration determines the first learning requirement.

The retraining configuration determines future recurring requirements after the initial assignment.

These should be investigated separately.

A learning item may have:

- Initial training without retraining
- Retraining requirements after initial completion
- Different initial and retraining periods

If retraining is not configured, the assignment may behave like a normal learning assignment and may no longer remain active after completion.

---

## Knowledge Area: Retraining Number and Period

SAP SuccessFactors Learning uses the Retraining Number together with the Retraining Period to determine the frequency of retraining.

For example:

- 365 Days
- 12 Months
- 1 Year

These values determine the cadence at which users are required to complete the learning again.

The available time units can include:

- Days
- Weeks
- Quarters
- Years

The configured number and period should always be reviewed when investigating recurring learning assignments.

---

## Knowledge Area: Event-Based Retraining

Event-based retraining calculates the next training period based on an event.

For initial assignments, the event can be the date when the curriculum or learning item is assigned.

For retraining, the relevant event is generally the user's completion of the learning item.

For example:

If retraining is configured as Event-based with a period of 365 days, the user's completion event is used to calculate the next retraining requirement.

Different users may therefore have different required dates depending on when they completed the learning.

When investigating unexpected required dates, the relevant completion or assignment event should be checked.

---

## Knowledge Area: Calendar-Based Retraining

Calendar-based retraining uses a fixed calendar structure to determine training periods and required dates.

All users can therefore follow the same defined training period.

A Basis Date is used when Calendar is selected as the retraining basis.

The Basis Date establishes the calendar periods used to calculate required dates.

Depending on when users receive the assignment, users may have different amounts of time available before the next common required date.

When investigating calendar-based retraining, verify:

- Retraining basis
- Basis Date
- Retraining number
- Retraining period
- Applicable calendar period

---

## Knowledge Area: Required Date Calculation

The Required Date represents the next date by which the user must complete the learning requirement.

SAP SuccessFactors Learning calculates required dates using the curriculum configuration.

Relevant configuration can include:

- Initial Number
- Initial Period
- Initial Basis
- Retraining Number
- Retraining Period
- Retraining Basis
- Required Date Basis
- Basis Date

The Required Date should be compared with:

- Assignment date
- Previous completion date
- Current completion status
- Retraining configuration

This helps determine whether a recurring assignment is expected.

---

## Knowledge Area: Required Date Basis

The Required Date Basis determines the starting point used for required date calculations.

Depending on the configuration, the system may use:

- Assignment Date
- Hire Date

When Assignment Date is used, calculations are based on when the curriculum was assigned to the user.

When Hire Date is used, calculations are based on the user's hire date.

Changes to a user's hire date can affect required date calculations when Hire Date is configured as the Required Date Basis.

---

## Knowledge Area: Previous Completions

When a curriculum is assigned, SAP SuccessFactors Learning can evaluate the user's Learning History for previous completions.

A previous completion may affect:

- Current completion status
- Curriculum requirements
- Next retraining required date

The system can also be configured to ignore previous completions older than a specified period.

This prevents very old completion records from incorrectly affecting current curriculum requirements.

When investigating a curriculum issue involving historical completions, check:

- Previous completion date
- Learning History
- Ignore Previous Completions configuration
- Retraining configuration

Do not assume that every historical completion automatically satisfies the current curriculum requirement.

---

## Knowledge Area: Curriculum Content Changes and Effective Dates

Changes to curriculum content can affect users depending on the effective date of the change.

For example, when a new learning item is added to a curriculum:

- A future effective date may delay when the new requirement affects users.
- A past or current effective date may cause the requirement to affect users immediately.

Effective dates should therefore be reviewed when users report unexpected new assignments or changes to curriculum completion status.

---

## Knowledge Area: Reassignments and Curriculum Assignments

SAP SuccessFactors Learning treats learning items assigned through a curriculum as part of the curriculum assignment structure.

When retraining is configured, repeated requirements can be treated as part of the same curriculum assignment.

Removing an individual learning item may not always be the correct resolution when the item is required through a curriculum.

The underlying curriculum assignment should be investigated before manually removing learning assignments.

Depending on the situation, the issue may require investigation of:

- The curriculum assignment
- Curriculum content
- Retraining configuration
- Assignment source

---

## Common Technical Investigation Points

When investigating curriculum and retraining issues, review:

- Curriculum ID
- Learning Item ID
- Affected user
- Current assignment status
- Completion status
- Learning History
- Previous completion date
- Initial training configuration
- Retraining Number
- Retraining Period
- Retraining Basis
- Event or Calendar configuration
- Basis Date
- Required Date
- Required Date Basis
- Assignment Date
- Hire Date where applicable
- Ignore Previous Completions configuration
- Curriculum effective dates
- Recent curriculum changes

---

## Resolution Logic

User reports that a completed course remains assigned or appears again

→ Identify the Learning Item and Curriculum

→ Verify whether the item is part of a curriculum

→ Check whether retraining is configured

→ Determine whether the current requirement is Initial Training or Retraining

→ Check Retraining Number and Period

→ Identify whether the Retraining Basis is Event or Calendar

If Event:

→ Check the relevant assignment or completion event date

If Calendar:

→ Check the Basis Date and applicable calendar period

→ Review the Required Date

→ Compare the Required Date with the completion date and retraining configuration

→ Check previous completion records where relevant

→ Review Ignore Previous Completions configuration if historical completions are involved

→ Check for recent curriculum content changes and effective dates

If the configuration explains the assignment:

→ The assignment is expected

If the assignment does not match the configuration:

→ Investigate curriculum configuration or assignment behavior further

Before manually removing the learning item:

→ Confirm whether the requirement is generated by the curriculum

---

## Important Considerations

- Retraining requires users to periodically complete learning to maintain qualification.
- A completed learning item may remain assigned when retraining is configured.
- Initial training and retraining can have separate configurations.
- Retraining Number and Period determine the retraining cadence.
- Event-based retraining uses relevant events such as completion dates.
- Calendar-based retraining uses defined calendar periods and a Basis Date.
- Required dates are calculated according to curriculum configuration.
- Previous completions can affect current curriculum status and retraining calculations.
- Historical completions may be ignored depending on configuration.
- Curriculum content changes can affect users based on effective dates.
- Do not manually remove a recurring assignment before identifying the curriculum and retraining configuration.
- A course appearing again after completion may be expected system behavior.

---

## SAP References

SAP Help documentation explains that retraining in SAP SuccessFactors Learning requires users to periodically complete learning to maintain qualification.

SAP documentation confirms that when retraining is configured, a learning item can remain assigned after completion while the system recalculates the next required date.

SAP Help documentation describes Initial and Retraining configuration, including the Number, Period, Basis, Basis Date, Required Date Basis, and Previous Completion settings used for curriculum calculations.

SAP documentation distinguishes Event-based and Calendar-based retraining and explains how completion events, assignment dates, and calendar periods affect future required dates.

For official SAP documentation, refer to the SAP Help Portal and SAP Support Knowledge Base.