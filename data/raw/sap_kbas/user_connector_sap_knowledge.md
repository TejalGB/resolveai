# SAP User Connector - SF Knowledge

## Category

User Connector and User Synchronization

## Product

SAP SuccessFactors Learning

## Source Type

SAP Official Documentation and Knowledge Base Articles

## SAP References

- SAP KBA 2375919 - Scheduled jobs in SuccessFactors Provisioning for use with User Connector-SF
- SAP Help Portal - Initial Configuration for User Connector - SF
- SAP Help Portal - Field Mapping for User Connector - SF

---

## Knowledge Area: User Connector - SF

User Connector - SF is used to synchronize user information between SAP SuccessFactors Platform and SAP SuccessFactors Learning.

The connector can create new user records and update existing user information in Learning.

User synchronization depends on multiple components including:

- Source-system user data
- Field mapping
- Scheduled data feeds
- Connector configuration
- Connector execution
- User-specific data validation

A successful overall connector process does not always guarantee that every individual user record was processed successfully.

---

## Knowledge Area: Scheduled Synchronization

User data synchronization depends on scheduled jobs and connector execution.

When investigating a user who is missing from Learning or whose information is outdated, first determine:

- When the user was created or updated in the source system
- When the next synchronization cycle was expected
- Whether the scheduled export completed
- Whether the User Connector - SF executed after the export
- Whether the expected processing cycle has completed

Do not immediately treat a missing user as a connector failure if the expected synchronization cycle has not yet occurred.

---

## Knowledge Area: User Data Processing

User Connector - SF processes user information from the SuccessFactors Platform and maps the information into SAP SuccessFactors Learning.

Important user information may include:

- User ID
- User status
- Email address
- Manager information
- Organizational information
- Job-related attributes
- Hire date

Incorrect or missing source data may prevent successful processing of a user record.

---

## Knowledge Area: User Status Synchronization

The user status in the source system and Learning should be compared during troubleshooting.

A user may be:

- Active in the source system but inactive in Learning
- Inactive in the source system
- Recently hired
- Recently reactivated
- Recently updated

A status mismatch may indicate a synchronization issue or may require verification of the source data and connector processing.

---

## Knowledge Area: Field Mapping

User Connector - SF relies on field mappings between the SuccessFactors Platform and Learning.

Incorrect mapping or invalid source values may result in user processing issues.

When troubleshooting data synchronization problems, verify:

- Required user fields
- Source-system values
- Field mapping configuration
- Referenced values
- Organizational data
- User status information

Do not modify standard connector mappings without following the approved configuration process.

---

## Knowledge Area: Connector Troubleshooting

When a user is not created or updated correctly in Learning:

1. Verify the user information in the source system.
2. Confirm that the expected synchronization cycle has occurred.
3. Check whether the scheduled export completed.
4. Check whether the User Connector - SF job executed.
5. Review connector results or logs.
6. Determine whether the affected user was picked up.
7. Check for user-specific validation or processing errors.
8. Correct invalid source information where required.
9. Reprocess according to the approved support process.
10. Verify the user record in Learning.

---

## Common Technical Investigation Points

Investigate the following when User Connector - SF issues occur:

- Connector job failures
- Scheduled job failures
- Missing input data
- Incorrect field mappings
- Invalid source-system values
- Missing required attributes
- User-specific validation errors
- Incorrect organizational references
- User status mismatches
- Processing delays

---

## Resolution Logic

User synchronization issue reported

→ Verify source-system user data

→ Check whether the expected synchronization cycle occurred

→ Verify scheduled export

→ Verify User Connector - SF execution

→ Review connector results

→ Was the user picked up?

If NO:

→ Investigate source data and synchronization selection

If YES:

→ Check for user-specific validation errors

→ Correct source information if required

→ Reprocess according to approved procedures

→ Verify user status and information in Learning

---

## Important Considerations

- The source system should be treated as the system of record for integrated user data.
- Do not assume that every missing user is caused by an LMS defect.
- Check synchronization timing before escalating connector issues.
- A successful connector run may still contain user-specific processing errors.
- Compare source-system information with Learning information.
- Do not manually recreate users without following the approved process.
- Verify the result after synchronization or reprocessing.

---

## SAP References

SAP KBA 2375919 discusses scheduled jobs used for User Connector-SF synchronization between SuccessFactors HCM and SuccessFactors Learning.

SAP Help documentation explains that User Connector-SF configuration includes connector behavior, field mapping, data feed scheduling, testing, and troubleshooting.

For official SAP documentation, refer to the SAP Help Portal and SAP Support Knowledge Base.