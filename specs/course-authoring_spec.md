# Course Authoring — Feature Spec

## Purpose

Instructors create a new course in the DRAFT state and build its structure from modules and nested lessons. This feature covers AC-02 and AC-03 only.

## Actors

- Instructor (creates courses and adds modules and lessons)
- Learner and Admin do not use this feature.

## User Stories

- As an instructor, I want to create a course with its title, description, category, and difficulty, so that I can start building it.
- As an instructor, I want to add modules and lessons to a draft course, so that the course has a clear structure learners can follow.

## Acceptance Criteria

### AC-02 Instructor can create a course with title, description, category, and difficulty; courses start in DRAFT state

- Given I am signed in as an instructor, When I create a course with a title, description, category, and difficulty, Then the course is saved and its state is DRAFT.
- Given I am signed in as a learner, When I try to create a course, Then the request is rejected and no course is saved.
- Given I am not signed in, When I try to create a course, Then the request is rejected and no course is saved. (NFR-04)

### AC-03 Instructor can add modules and nested lessons to a draft course (course → modules → lessons hierarchy)

- Given a course in DRAFT state, When the instructor adds a module to it, Then the module is saved under that course.
- Given a module in a DRAFT course, When the instructor adds a lesson to that module, Then the lesson is saved under that module, so the hierarchy is course → module → lesson.
- Given a course in PUBLISHED state, When the instructor tries to add a module to it, Then the request is rejected and the course structure is unchanged. (NFR-08, DR-2)
- Given a course in UNPUBLISHED state, When the instructor tries to add a module or lesson, Then the request is rejected and the course structure is unchanged. (AC-03 — modules/lessons only on a DRAFT course)
- Given a course in DRAFT state, When a learner tries to add a module to it, Then the request is rejected and the course structure is unchanged. (NFR-04)

## Business Rules

- Every new course starts in DRAFT state. (AC-02, DR-1)
- A course has a title, description, category, and difficulty. (AC-02)
- Modules and lessons can be added only to a DRAFT course. (AC-03, DR-2)
- The course → modules → lessons hierarchy is fixed by AC-03. (AC-03)
- A published course cannot be changed unless it goes through an unpublish transition. (NFR-08)
- Course state changes are owned by the Catalog feature (AC-04, AC-08); this feature does not change state. (AC-08)

## Applicable NFRs

- **NFR-04:** Only an instructor may create courses or add modules and lessons. The check happens at the controller layer.
- **NFR-08:** A published course (including its modules and lessons) cannot be changed (mutated) without an unpublish transition first.

## Related User Journeys

- Instructor Workbench — author courses with modules, lessons, and quiz questions. Quiz question authoring is covered by AC-05 in the Quiz Engine feature (specs/quiz-engine_spec.md).

## Out of Scope

- Publishing, unpublishing, and archiving courses (Catalog feature, AC-04 and AC-08)
- Approving published courses and the admin view of the catalog (Admin Console, AC-10)
- Lesson content delivery and video streaming (the out of scope list excludes real video streaming)
- Learner progress and quiz grading (Progress Tracker and Quiz Engine features)

## Open Questions

None
