# Admin Console — Feature Spec

## Purpose

Admins manage the course catalog, approve published courses, and monitor enrollment-level analytics. Publishing and unpublishing are specified in catalog_spec.md. This feature covers AC-10. It is delivered in Sprint 3.

## Actors

- Admin (manages the catalog, approves published courses, and views enrollment analytics)
- Learner and Instructor do not use this feature.

## User Stories

- As an admin, I want to manage the course catalog, so that the published courses are the right ones.
- As an admin, I want to approve published courses, so that the catalog is reviewed by an admin.
- As an admin, I want to see enrollment-level analytics, so that I can monitor how learners are enrolling.

## Acceptance Criteria

### AC-10 Admin can manage course catalog, approve published courses, and monitor enrollment-level analytics

- Given a course in PUBLISHED state, When an admin approves it, Then the approval is recorded for that course.
- Given a course in DRAFT state, When an admin tries to approve it, Then the request is rejected and no approval is recorded.
- Given a PUBLISHED course with 3 enrollments, When an admin views enrollment analytics for that course, Then the enrollment count shown is 3. (AC-10)
- Given I am signed in as a learner, When I request enrollment-level analytics, Then the request is rejected. (NFR-04)
- Given I am not signed in, When I request enrollment-level analytics, Then the request is rejected. (NFR-04)
- Given enrollment-level analytics are shown, When an admin views them, Then no enrollment record is changed. (NFR-02, DR-9)
- Given courses exist in the catalog, When an admin opens the admin catalog view, Then each course is listed with its lifecycle state. (AC-10)
- Given I am signed in as a learner or instructor, When I open the admin catalog view, Then the request is rejected. (NFR-04)
- Given a course in UNPUBLISHED or ARCHIVED state, When an admin tries to approve it, Then the request is rejected and no approval is recorded. (AC-10)
- Given I am signed in as an instructor, When I try to approve a course, Then the request is rejected. (NFR-04)
- Given I am signed in as an instructor, When I request enrollment analytics, Then the request is rejected. (NFR-04)

## Business Rules

- Only an admin can approve published courses and view enrollment-level analytics. (AC-10, NFR-04)
- Approval applies only to a course in PUBLISHED state. (AC-10)
- Publishing and unpublishing are managed through the catalog and are specified in catalog_spec.md. (AC-04)
- Enrollment analytics read enrollment records and never change them. (NFR-02, DR-9)

## Applicable NFRs

- **NFR-02:** Enrollment records are append-only. Analytics only read them. (DR-9)
- **NFR-03:** Analytics never write learner personal data to logs in plain text. (DR-13)
- **NFR-04:** Approval and analytics are limited to admins, and the check happens at the controller layer.
- **NFR-08:** A published course cannot be changed without an unpublish transition. Whether approval counts as a change is an Open Question.

## Related User Journeys

- Admin Console (system function) — manage the course catalog, publish and unpublish courses, and monitor enrollment and engagement. Publishing and unpublishing are covered by catalog_spec.md. Approval and analytics are covered here.

## Out of Scope

- Publishing, unpublishing, and archiving courses (catalog_spec.md)
- Creating courses and modules (course-authoring_spec.md)
- Payments and paid courses (out of scope list)
- Certificates and certificate verification (out of scope list)

## Open Questions

- Doc silent — to be decided later: what approval means (record vs state).
