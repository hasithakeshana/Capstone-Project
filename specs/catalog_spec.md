# Catalog — Feature Spec

## Purpose

Admins publish and unpublish courses, and the system enforces the course lifecycle so that learners can only see and enroll in published courses. Learners browse and search published courses by category and difficulty. This feature covers AC-04 and AC-08, plus the browse and search user journey (Browse, no AC id).

## Actors

- Admin (publishes and unpublishes courses)
- Learner (browses and searches published courses)
- The system (enforces the lifecycle)

## User Stories

- As an admin, I want to publish a draft course, so that learners can enroll in it.
- As an admin, I want to unpublish a published course, so that learners can no longer enroll in it.
- As a learner, I want to search published courses by category and difficulty, so that I can find a course that fits me.

## Acceptance Criteria

### AC-04 Admin can publish (DRAFT → PUBLISHED) or unpublish (PUBLISHED → UNPUBLISHED) a course; learners can only enroll in PUBLISHED courses

- Given a course in DRAFT state and I am signed in as an admin, When I publish it, Then its state is PUBLISHED.
- Given a course in PUBLISHED state and I am signed in as an admin, When I unpublish it, Then its state is UNPUBLISHED.
- Given a course in DRAFT state and I am signed in as an instructor, When I try to publish it, Then the request is rejected and its state stays DRAFT. (NFR-04)
- Given a course in UNPUBLISHED state, When a learner tries to enroll in it, Then the enrollment is rejected. (Enrollment feature, AC-01)
- Given a course in PUBLISHED state, When anyone tries to change its title, description, category, difficulty, modules, or lessons, Then the change is rejected and the course is unchanged. (NFR-08)

### AC-08 Course lifecycle states DRAFT → PUBLISHED → UNPUBLISHED → ARCHIVED are enforced; invalid transitions raise InvalidCourseStateException

- Given a course in DRAFT state, When an admin moves it to PUBLISHED, Then its state is PUBLISHED.
- Given a course in UNPUBLISHED state, When the course is moved to ARCHIVED, Then its state is ARCHIVED.
- Given a course in UNPUBLISHED state, When an admin tries to move it to PUBLISHED, Then the request is rejected with InvalidCourseStateException and its state stays UNPUBLISHED.
- Given a course in DRAFT state, When the course is moved to ARCHIVED, Then InvalidCourseStateException is raised and its state stays DRAFT.
- Given a course in PUBLISHED state, When it is moved directly to ARCHIVED, Then InvalidCourseStateException is raised and the state stays PUBLISHED.
- Given a course in ARCHIVED state, When an admin tries to move it to any other state, Then the request is rejected with InvalidCourseStateException and its state stays ARCHIVED.
- Given a course in UNPUBLISHED state and I am signed in as an instructor, When I try to archive it, Then the request is rejected and its state stays UNPUBLISHED. (NFR-04)

### Browse (user journey — no AC id)

- Given a course in DRAFT state, When a learner searches the catalog for its category, Then the course is not listed.
- Given a course in PUBLISHED state with category C, When a learner searches by category C, Then the course is listed.
- Given PUBLISHED courses with difficulty D, When a learner filters by difficulty D, Then only PUBLISHED courses with difficulty D are listed.
- Given a course in UNPUBLISHED or ARCHIVED state, When a learner searches, Then it is not listed.

## Business Rules

- The only allowed lifecycle moves are DRAFT → PUBLISHED, PUBLISHED → UNPUBLISHED, and UNPUBLISHED → ARCHIVED. Any other move raises InvalidCourseStateException. (AC-08, DR-1)
- Only an admin can change a course's state, including UNPUBLISHED → ARCHIVED. (AC-04, AC-08, NFR-04)
- Learners can enroll only in PUBLISHED courses. (AC-04, DR-3)
- A published course cannot be changed without an unpublish transition. (NFR-08)
- Browse and search cover PUBLISHED courses only, and filter by category and difficulty. (Browse, user journey — no AC id)

## Applicable NFRs

- **NFR-04:** Only an admin can publish or unpublish a course. The check happens at the controller layer.
- **NFR-08:** A published course cannot be changed (mutated) without an unpublish transition first.

## Related User Journeys

- Browse (user journey — no AC id) — search published courses by category and difficulty.
- Admin Console — manage the course catalog, publish and unpublish courses.

## Out of Scope

- Approving published courses and monitoring enrollment analytics (Admin Console, AC-10)
- Creating courses and adding modules and lessons (Course Authoring, AC-02 and AC-03)
- Enrolling in a course (Enrollment, AC-01)
- Paid courses and payments (out of scope list)

## Open Questions

- Doc silent — to be decided later: what approval (AC-10) means.
