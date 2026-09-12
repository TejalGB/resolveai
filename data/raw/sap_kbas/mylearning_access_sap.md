# SAP MyLearning Access - SF Knowledge

## Category

User Access and Learning Availability

## Product

SAP SuccessFactors Learning

## Source Type

SAP Official Documentation and Knowledge Base Articles

## SAP References

- SAP Help Portal - SAP SuccessFactors Learning Security Roles
- SAP Help Portal - Security Personas in SAP SuccessFactors Learning
- SAP Help Portal - Data Access in SAP SuccessFactors Learning
- SAP Help Portal - Placing Learning Users into Security Roles
- SAP Help Portal - Security Roles and Role Management

---

## Knowledge Area: Learning Access

Access to SAP SuccessFactors Learning depends on multiple access and security components.

A user may successfully authenticate into SAP SuccessFactors but still be unable to access specific Learning functionality.

Learning access can depend on:

- User account availability
- Learning user persona
- Role assignment
- User permissions
- Security configuration
- Role restrictions
- User synchronization
- Access configuration in the SAP SuccessFactors environment

Therefore, inability to access Learning should not automatically be treated as an authentication issue.

---

## Knowledge Area: Learning Personas

SAP SuccessFactors Learning supports different user personas.

The primary personas include:

- Learner
- Instructor
- Administrator

The Learner persona is used by employees who access learning activities, courses, online content, and other Learning functionality.

Instructor and Administrator personas provide access to different Learning functions.

A user may successfully log in to SAP SuccessFactors but have different available functionality depending on the assigned persona and permissions.

When investigating access issues, determine which Learning functionality the user is expected to access.

---

## Knowledge Area: User Role and Permissions

Security roles control the actions and functionality available to users in SAP SuccessFactors Learning.

A security role can include:

- Permissions
- Restrictions
- Security domains
- Access to specific Learning functionality

User roles determine what actions or areas of the Learning environment are available.

If a user cannot access expected Learning functionality, verify whether the appropriate user role and permissions are assigned.

Do not modify security roles without following the approved access and change management process.

---

## Knowledge Area: Security Roles

SAP SuccessFactors Learning uses security roles to control access to Learning functionality.

Security roles can define:

- What users can access
- What actions users can perform
- Which Learning features are available
- Which data or entities can be accessed

A user's available functionality may differ depending on the permissions assigned to the role.

Incorrect or missing role assignments may affect Learning access.

---

## Knowledge Area: Learning Access Versus Authentication

Authentication and Learning access should be investigated separately.

A user may experience different scenarios:

- Unable to log in to SAP SuccessFactors
- Successfully logged in but unable to access Learning
- Able to access Learning but unable to access a specific feature
- Able to access Learning but unable to view specific learning content

If the user cannot authenticate into SAP SuccessFactors:

→ Investigate authentication or identity-related issues.

If the user can authenticate but cannot access Learning:

→ Investigate Learning access, user role, permissions, and user account configuration.

This distinction prevents authentication issues from being incorrectly treated as Learning access issues.

---

## Knowledge Area: User Synchronization and Learning Access

User access to SAP SuccessFactors Learning may depend on successful user synchronization.

When users are integrated into Learning through User Connector processes, the user record and relevant role information may be created or updated through the integration process.

If the user does not exist in Learning or required user information is missing:

→ Investigate the User Connector or synchronization process.

If the user exists and is active in Learning but cannot access expected functionality:

→ Investigate role assignment and permissions.

User synchronization and Learning authorization should be treated as separate investigation areas.

---

## Knowledge Area: Role Assignment

User roles can be assigned through different approved processes depending on the system configuration.

Role assignment may be managed through:

- User configuration
- User synchronization
- Assignment Profiles
- Approved administrative processes

Assignment Profiles can be used to assign Learning security roles to groups of users based on configured criteria.

Changes to user attributes may affect role assignment where automated role assignment is configured.

When investigating access issues, verify whether the user has the expected role and whether recent user changes may have affected role assignment.

---

## Knowledge Area: Scope of the Access Issue

Determine whether the issue affects:

- One user
- Multiple users
- A specific user population
- A specific region
- All users

If one user is affected, investigate:

- User account status
- User role
- User permissions
- User synchronization
- User-specific configuration

If multiple users are affected, investigate:

- Shared role configuration
- Permission changes
- Security configuration
- User population rules
- System-wide access changes

The scope of the issue helps determine whether the problem is user-specific or configuration-related.

---

## Common Technical Investigation Points

When investigating MyLearning or Learning access issues, collect:

- User ID
- User status
- User population or region where applicable
- Expected Learning access
- Actual access behavior
- User role
- Assigned permissions
- Whether the user exists in Learning
- Whether the user is active
- Whether synchronization completed successfully
- Exact error message
- Screenshot where available
- Whether the issue affects one or multiple users
- Whether recent role or security changes occurred

---

## Resolution Logic

User reports inability to access MyLearning or Learning functionality

→ Confirm what Learning functionality the user is unable to access

→ Determine whether the user can successfully authenticate into SAP SuccessFactors

If NO:

→ Investigate authentication separately

If YES:

→ Verify whether the user exists and is active in SAP SuccessFactors Learning

If user does not exist or information is incorrect:

→ Investigate user synchronization

If user exists and is active:

→ Check expected Learning access

→ Verify user role and permissions

→ Check whether role assignment is correct

→ Check whether recent user or role changes occurred

→ Determine whether the issue affects one or multiple users

If one user:

→ Investigate user-specific role, permissions, and account configuration

If multiple users:

→ Investigate shared security, role, or access configuration

If access configuration appears correct but the issue continues:

→ Collect relevant evidence

→ Escalate according to the approved support process

---

## Important Considerations

- MyLearning access should be distinguished from authentication issues.
- Successful login does not automatically guarantee access to all Learning functionality.
- Learning access can depend on user roles and security permissions.
- User synchronization issues should be investigated separately from authorization issues.
- Security roles can control access to Learning features and functionality.
- Role assignments may be affected by automated processes or Assignment Profiles.
- Determine whether the issue affects one user or multiple users before identifying the cause.
- Do not modify user roles or security permissions without following approved access management procedures.
- Regional or organization-specific access rules should be maintained separately from general SAP Learning access knowledge.

---

## SAP References

SAP SuccessFactors Learning documentation explains that Learning access is controlled through user personas, security roles, permissions, restrictions, and security domains.

SAP documentation distinguishes between authentication into the SuccessFactors environment and authorization to access specific Learning functionality.

SAP Learning users may receive role assignments through configured processes, including user synchronization and Assignment Profiles.

For official SAP documentation, refer to the SAP Help Portal and SAP Support Knowledge Base.