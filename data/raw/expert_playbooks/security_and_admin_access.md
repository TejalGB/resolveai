# Security Domain and Administrator Access Issues

## Category
Security Domain and Administrator Access

## Product
SAP SuccessFactors Learning

## Incident

An administrator reports that they cannot view, access, edit, or perform an action on a particular LMS entity such as a class, learning item, user, instructor record, or report.

## Problem Understanding

Administrator access in SAP SuccessFactors Learning is controlled through a combination of:

- Security Domains
- Security Domain Groups
- Administrator Roles
- Permissions
- Entity and functional restrictions

Major LMS entities such as users, learning items, classes, curricula, and content objects can have an associated Security Domain.

If an administrator does not have access to the Security Domain associated with an entity, they may be unable to view or perform actions on that entity.

Therefore, an administrator access issue should not automatically be treated as a system defect.

---

## Common Scenarios

### 1. Administrator Cannot Access a Class

An administrator may report that they cannot view or access a particular class or scheduled offering.

The class may belong to a Security Domain that is not included in the administrator's permitted domains.

For instructor-led training, also consider whether the administrator has the appropriate role and permissions for accessing classes.

### 2. Administrator Cannot View or Run Reports

An administrator may report that they cannot see or run a particular report.

Report access can depend on:

- Report availability/publication
- Administrator permissions
- Security Domain access
- Run Report permission

A report may therefore be visible to one administrator but unavailable to another.

### 3. Administrator Cannot View a Learning Item

An administrator may be unable to access a particular learning item because the learning item belongs to a Security Domain outside the administrator's access.

### 4. Administrator Cannot Access Other LMS Entities

Similar access issues may occur with:

- Users
- Curricula
- Content
- Classes
- Learning items
- Instructor-related records
- Reports

---

## Troubleshooting Steps

### 1. Understand the Access Issue

Identify:

- What entity is the administrator trying to access?
- What action are they trying to perform?
- Can they access similar records?
- Is the issue affecting only one administrator or multiple administrators?

### 2. Identify the Entity

Determine the specific LMS object involved.

Examples:

- Class / Scheduled Offering
- Learning Item
- User
- Curriculum
- Content
- Report
- Instructor

### 3. Check the Security Domain

Check the Security Domain associated with the relevant entity.

Compare it with the Security Domains available to the administrator.

If the entity belongs to a domain outside the administrator's permitted access, the access restriction may be expected.

### 4. Check Administrator Role and Permissions

If the Security Domain appears appropriate, check whether the administrator's assigned role provides the required permission.

The administrator may have access to the relevant domain but still lack the permission required to perform the requested action.

### 5. Check Security Domain Group / Restrictions

Check whether the administrator's role or security configuration restricts access to specific Security Domains.

An administrator may have multiple roles, and the effective access can depend on the combination of those roles.

### 6. Check Report-Specific Access

For report-related issues, verify:

- Whether the report is published/available
- Whether the administrator has access to the report's Security Domain
- Whether the administrator has the relevant Run Report permission

### 7. Determine Expected vs. Incorrect Access

If the administrator does not have access to the required Security Domain or permission, determine whether this restriction is intentional.

If access should be provided, follow the organization's approved process for updating the administrator's role/security configuration.

### 8. Escalate When Required

If the administrator should have access but the configuration appears correct, collect the relevant details and escalate for further investigation.

---

## Decision Flow

Administrator reports access issue
→ Identify affected entity
→ Identify requested action
→ Check entity Security Domain
→ Check administrator's permitted Security Domains
→ Check administrator role
→ Check required permission

If Security Domain is not accessible:
→ Access restriction may be expected
→ Follow approved process if access should be granted

If Security Domain is accessible but action is unavailable:
→ Check required permission / role restriction

For reports:
→ Check report availability
→ Check Security Domain
→ Check Run Report permission

If configuration appears correct:
→ Investigate further / escalate

---

## Important Considerations

- Security Domain and administrator permissions are related but are not the same thing.
- Having access to a Security Domain does not automatically mean the administrator can perform every action on an entity.
- The administrator's role determines the permissions and restrictions available to them.
- An administrator may have multiple roles, which can affect their effective access.
- The PUBLIC Security Domain is available to all administrators, subject to the applicable permissions.
- Do not change Security Domains or administrator permissions without confirming that the administrator should have the requested access.
- Avoid granting broader access than required.

---

## Common Resolution

If the administrator does not have access to the Security Domain associated with the required entity, the issue may be resolved by following the organization's approved security/role process to provide the appropriate access.

If the administrator has the correct Security Domain but lacks the required action, review the administrator's role and permissions.

If the issue involves a report, verify both the report's Security Domain access and the relevant Run Report permission.

---

## Escalation Information

When escalating, provide:

- Administrator/user ID
- Affected entity
- Entity ID, if available
- Security Domain of the entity
- Administrator role
- Relevant permission
- Description of the requested action
- Whether other administrators can access the same entity

---

## Source Type

Expert Resolution Playbook

## Knowledge Sources

- Internal LMS incident-resolution experience
- SAP SuccessFactors Learning documentation
- SAP Knowledge Base Articles (to be added)