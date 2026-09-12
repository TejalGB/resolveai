# SAP Assignment Profiles - SF Knowledge

## Category

Assignment Profiles and Learning Assignments

## Product

SAP SuccessFactors Learning

## Source Type

SAP Official Documentation and Knowledge Base Articles

## SAP References

- SAP Help Portal - SAP SuccessFactors Learning Assignment Profiles
- SAP Help Portal - Setting Up Assignment Profile Rules
- SAP Help Portal - Assigning Courses to Learners
- SAP Help Portal - Checking the Assignment Profiles that Assign a Learning Item
- SAP Help Portal - Checking the Assignment Profiles That Assign a Curriculum
- SAP Help Portal - Scheduling Assignment Profiles to Update Automatically
- SAP Help Portal - Learning Assignment Methods that do not Rely on Assignment Profiles

---

## Knowledge Area: Assignment Profiles

In SAP SuccessFactors Learning, Assignment Profiles are used to automatically assign learning based on employee or learner attributes.

Assignment Profiles use a set of rules to identify users who match specific criteria. The matching users are grouped into an Assignment Profile pool, and learning entities can then be assigned to those users.

Assignment Profiles can be used to assign entities such as:

- Learning Items
- Curricula
- Programs
- Libraries
- Recommended learning entities
- User roles

For example, an Assignment Profile can identify users based on attributes such as location, job code, organization, department, or other user attributes and assign the relevant learning automatically.

---

## Knowledge Area: Assignment Profile Rules

Assignment Profile rules determine which users belong to an Assignment Profile.

Each user is evaluated against the rules configured in the Assignment Profile.

When the configured rules evaluate as true, the user becomes a member of the Assignment Profile pool.

Rules can evaluate user attributes such as:

- Country or region
- Job code
- Organization
- Department
- Address-related attributes
- Security domain
- Custom user attributes
- Other available learner attributes

Assignment Profile rules can also contain groups of conditions.

Groups can be used to create more complex rule logic.

SAP recommends using Preview Users when creating or modifying Assignment Profile rules to verify which users are captured by the configured criteria.

---

## Knowledge Area: User Attribute Changes and Assignment Behavior

Assignment Profiles are dynamic.

As user attributes change, users may automatically enter or leave Assignment Profile membership when the Assignment Profile is processed.

For example:

- A user changes location
- A user changes job code
- A user changes department
- A user moves to another organization
- A relevant custom attribute changes

These changes may cause the user to meet or no longer meet Assignment Profile criteria.

As a result, learning assignments may also change.

When investigating an unexpected learning assignment, recent changes to user attributes should therefore be considered.

---

## Knowledge Area: Automatic Assignment Processing

Assignment Profiles require processing to update user pools and learning assignments.

The Assignment Profile Execute Updates process evaluates Assignment Profile rules and adjusts:

- Assignment Profile membership
- User pools
- Learning assignments

Assignment Profiles can be scheduled to update automatically.

The Assignment Profile Execute Updates process is available through:

System Administration
→ Automatic Processes
→ Assignment Profile Execute Updates

When the process runs, it evaluates the configured Assignment Profiles and updates users and assignments accordingly.

A change to an Assignment Profile may require the appropriate Execute Changes or update process before the new assignment behavior takes effect.

---

## Knowledge Area: Learning Assigned Through Assignment Profiles

Assignment Profiles can automatically assign learning to all users who match the configured rules.

The assignment process generally involves:

1. Defining Assignment Profile criteria.
2. Identifying users who match the criteria.
3. Creating the Assignment Profile user pool.
4. Associating learning entities with the Assignment Profile.
5. Executing changes or allowing the scheduled Assignment Profile update process to run.
6. Updating user learning assignments.

If a user matches the Assignment Profile criteria, the assignment may be expected.

---

## Knowledge Area: Checking Assignment Sources

SAP SuccessFactors Learning provides methods for identifying Assignment Profiles associated with learning entities.

For a Learning Item:

Learning Administration
→ Learning Activities
→ Items
→ Open the relevant Learning Item
→ Assignment Profiles

This can be used to identify Assignment Profiles that automatically assign the Learning Item.

For a Curriculum:

Learning Administration
→ Learning Activities
→ Curricula
→ Open the relevant Curriculum
→ Assignment Profiles

This can be used to identify Assignment Profiles that automatically assign the Curriculum.

When troubleshooting an unexpected assignment, administrators should identify the Assignment Profile associated with the learning entity before modifying the assignment.

---

## Knowledge Area: Previewing Assignment Profile Users

Assignment Profile rules should be validated before changes are executed.

The Preview Users functionality can be used to identify the users captured by the configured Assignment Profile rules.

This helps administrators verify:

- Which users match the Assignment Profile
- Whether the intended population is included
- Whether unintended users are included
- Whether user attributes are producing the expected result

Previewing users is particularly important when Assignment Profile rules are changed.

---

## Knowledge Area: Multiple Learning Assignment Methods

Although Assignment Profiles are commonly used for automatic learning assignments, learning can also be assigned through other methods.

Possible assignment methods include:

- Assignment Profiles
- Curriculum assignments
- Learning job codes
- Administrator direct assignment
- Bulk assignment
- Self-assignment
- Manager or peer assignment
- Learning recommendations
- Other configured learning processes

Therefore, the presence of a learning assignment does not automatically mean that it was created by an Assignment Profile.

The assignment source should be identified before making configuration changes.

---

## Knowledge Area: Assignment Profile Status and Changes

Assignment Profiles can actively affect large numbers of users and learning assignments.

Changes to Assignment Profile rules or associated learning entities can therefore have a broad impact.

Before executing Assignment Profile changes:

- Review the configured rules
- Preview affected users
- Verify the learning entities associated with the profile
- Confirm the intended business requirement
- Verify that unintended users are not included

Assignment Profile changes should follow the organization's approved configuration and change management process.

---

## Common Technical Investigation Points

When investigating unexpected learning assignments, review:

- Learning Item or Curriculum ID
- Affected user
- Assignment Profile associated with the learning entity
- Assignment Profile rules
- User attributes used in the rules
- Recent changes to user information
- Assignment Profile user pool
- Preview Users results
- Assignment Profile processing status
- Assignment Profile Execute Updates process
- Other Assignment Profiles that may assign the same learning
- Alternative assignment methods
- Curriculum or job code assignment behavior

---

## Resolution Logic

Unexpected learning assignment reported

→ Identify the Learning Item, Curriculum, or Program

→ Identify the affected user

→ Check the learning entity for associated Assignment Profiles

→ Review Assignment Profile rules

→ Compare user attributes with the configured criteria

→ Check whether the user belongs to the Assignment Profile pool

→ Review recent user attribute changes

→ Check whether Assignment Profile updates were processed

→ Check for multiple Assignment Profiles

→ Check for alternative assignment methods

If Assignment Profile criteria match:

→ Assignment may be expected

If Assignment Profile criteria do not match:

→ Investigate user data, rule configuration, or processing behavior

If another assignment method is identified:

→ Investigate the applicable assignment source

Before modifying or removing an assignment:

→ Identify the underlying assignment mechanism

→ Follow the approved configuration process

---

## Important Considerations

- Assignment Profiles are based on user attributes and configured rules.
- User attribute changes can affect Assignment Profile membership.
- Assignment Profiles can automatically add or remove users from assignment pools when processed.
- Assignment Profile Execute Updates controls the automatic update of pools and assignments.
- Preview Users should be used to validate Assignment Profile rules.
- A learning assignment may originate from mechanisms other than Assignment Profiles.
- Multiple Assignment Profiles may potentially affect the same user or learning entity.
- Assignment sources should be identified before manually removing learning assignments.
- Changes to Assignment Profiles can affect a large user population.
- Assignment Profile modifications should follow approved configuration and change management procedures.

---

## SAP References

SAP Help documentation describes Assignment Profiles as a mechanism for assigning learning based on employee attributes and rule-based user pools.

SAP documentation explains that Assignment Profile rules determine user membership and that changes to relevant user attributes can automatically affect membership and learning assignments.

SAP Help documentation provides functionality to identify Assignment Profiles associated with Learning Items and Curricula.

SAP documentation also explains that Assignment Profile Execute Updates processes user pools and assignment changes on a scheduled or manually triggered basis.

For official SAP documentation, refer to the SAP Help Portal and SAP Support Knowledge Base.