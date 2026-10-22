# Instructor Workbench — Feature Spec

## Purpose

Instructors see learner progress for a course, aggregated into four progress bands. The workbench also covers the instructor side of course authoring, which is specified in course-authoring_spec.md and quiz-engine_spec.md. This feature covers AC-09. It is delivered in Sprint 3.

## Actors

- Instructor (views aggregated progress and authors courses)
- Learner and Admin do not use this feature. Admin analytics are covered by admin-console_spec.md.

## User Stories

- As an instructor, I want to see how learners are spread across progress bands in a course, so that I can see how the course is going.
- As an instructor, I want to see aggregated progress only, so that I do not see any single learner's progress.

## Acceptance Criteria

### AC-09 Instructor can view learner progress aggregated by course (count by progress band: 0–25%, 25–50%, 50–75%, 75–100%)

- Given I am signed in as an instructor and a course has two enrolled learners, one at 10% progress and one at 60% progress, When I view progress for that course, Then the 0–25% band count is 1, the 50–75% band count is 1, and the other two band counts are 0.
- Given I am signed in as an instructor, When I view progress for a course, Then I see a count for each of the four bands: 0–25%, 25–50%, 50–75%, and 75–100%.
- Given I am signed in as an instructor, When I view progress for a course, Then I see only aggregated band counts and no individual learner's progress. (AC-09, DR-11)
- Given I am the instructor of a course, When I try to set or change a learner's quiz score or attempt in that course, Then the request is rejected and the score is unchanged. (NFR-08, DR-12)
- Given I am signed in as a learner, When I request progress band counts for a course, Then the request is rejected. (NFR-04)
- Given I am not signed in, When I request progress band counts for a course, Then the request is rejected. (NFR-04)

## Business Rules

- The four progress bands are 0–25%, 25–50%, 50–75%, and 75–100%. (AC-09)
- Band counts are based on course progress, which is completed lessons divided by total lessons. (AC-07, DR-5)
- Instructors see only aggregated band counts, never an individual learner's progress. (AC-09, DR-11)
- Instructors cannot grade their own courses' learners. (NFR-08, DR-12)
- Instructors author courses and quiz questions. Course authoring is specified in course-authoring_spec.md. Quiz questions are specified in quiz-engine_spec.md (AC-05).

## Applicable NFRs

- **NFR-04:** Viewing band counts is limited to instructors, and the check happens at the controller layer. Learner and admin roles are separated.
- **NFR-08:** Instructors cannot grade their own courses' learners. (DR-12)

## Related User Journeys

- Instructor Workbench (system function) — author courses with modules, lessons, and quiz questions, and view learner progress aggregated by course. Authoring is covered by course-authoring_spec.md and quiz-engine_spec.md. Progress viewing is covered here.

## Out of Scope

- Publishing, unpublishing, and archiving courses (catalog_spec.md)
- Approving published courses and enrollment analytics for admins (admin-console_spec.md, AC-10)
- Individual progress detail — AC-09 gives aggregated counts only
- Quiz grading (quiz-engine_spec.md)
- Live virtual classes and certificates (out of scope list)

## Open Questions

- Doc silent — to be decided later: how a course is tied to an instructor (ownership).
- Doc silent — to be decided later: band boundary at exactly 25%, 50% and 75%.
