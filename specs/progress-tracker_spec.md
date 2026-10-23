# Progress Tracker — Feature Spec

## Purpose

Learners mark lessons complete inside a course they are enrolled in. The system computes course progress as completed lessons divided by total lessons, and keeps a snapshot of progress for each learner. Learners can view their own progress percentage. This feature covers AC-07, plus the Learn and Progress user journeys and the Progress Tracker system function.

## Actors

- Learner (marks lessons complete and views own progress)
- The system (computes and snapshots progress)

## User Stories

- As a learner, I want to mark a lesson complete, so that my progress is recorded.
- As a learner, I want to see my progress percentage in a course, so that I know how far I have come.
- As a learner, I want to move through the modules and lessons of a course in order, so that I learn the material in the intended sequence.

## Acceptance Criteria

### AC-07 Learner can mark a lesson complete; course progress percentage is computed as completed_lessons / total_lessons

- Given I am enrolled in a course and a lesson belongs to that course, When I mark the lesson complete, Then the completion is saved and the course progress is recalculated.
- Given a course with 4 lessons and I have completed 1 of them, When I view my progress for that course, Then the progress is 25%.
- Given a course with 4 lessons and I have completed none of them, When I view my progress for that course, Then the progress is 0%.
- Given a course with 4 lessons and I have completed all 4 of them, When I view my progress for that course, Then the progress is 100%.
- Given a course with 0 lessons, When I view my progress, Then it is 0%.
- Given a course with 3 lessons and I have completed 1 of them, When I view my progress for that course, Then the progress is 33%.
- Given a lesson completion exists, When anyone tries to edit or delete it, Then the change is rejected and the record is unchanged. (NFR-02)
- Given I mark a lesson complete, When the request is logged, Then the log does not contain my progress or identity in plain text. (NFR-03, DR-13)
- Given I am not enrolled in a course, When I mark one of its lessons complete, Then the request is rejected and no completion is saved.
- Given I am not signed in, When I mark a lesson complete, Then the request is rejected and no completion is saved. (NFR-04)
- Given I am a learner, When I request the progress of another learner, Then the request is rejected and no progress is shown. (NFR-08)

### Progress view (user journey — no AC id)

- Given I am enrolled in two courses, When I open my progress view, Then I see a progress percentage for each enrolled course and nothing for courses I am not enrolled in.

Quiz scores in this view are added by the Quiz Engine feature in sprint 3.

## Business Rules

- Course progress percentage is completed lessons divided by total lessons. (AC-07, DR-5)
- A learner can mark lessons complete only in a course they are enrolled in. (Learn user journey, after Enroll; AC-01)
- Lesson completion records are append-only. (NFR-02, DR-9)
- A learner cannot access another learner's progress. Instructors see only aggregated band counts (AC-09); admins see enrollment analytics (AC-10). (NFR-08, DR-11)
- Quiz scores are shown separately from course progress, not combined into it. (Progress user journey)
- Learners move through modules and lessons sequentially. (Learn user journey).
- The system computes and snapshots course progress for each learner. (Progress Tracker system function).
- A course with no lessons shows 0% progress. (project decision; doc silent)
- Percentages round down (integer division: x * 100 // total). Project decision; doc silent. (AC-07)

## Applicable NFRs

- **NFR-02:** Lesson completion records are only added, never edited or deleted.
- **NFR-03:** Learner performance data (progress, completions) is never written to logs in plain text. (DR-13)
- **NFR-04:** Marking a lesson complete and viewing progress are checked at the controller layer. A learner can see only their own individual progress; instructor band counts (AC-09) and admin analytics (AC-10) are covered in their own specs.
- **NFR-08:** A learner cannot read another learner's progress.

## Related User Journeys

- Learn (user journey) — move through modules and lessons sequentially and mark lessons complete.
- Progress (user journey) — view own progress percentage and quiz scores across enrolled courses. The quiz score part is covered by the Quiz Engine feature.
- Progress Tracker (system function) — compute and snapshot course progress for each learner.

## Out of Scope

- Quiz attempts, grading, and quiz score calculation (Quiz Engine feature, AC-05 and AC-06)
- Instructor view of learner progress by band (Instructor Workbench, AC-09)
- Certificates tied to completion (out of scope list)
- Video watch tracking (the out of scope list excludes video streaming)

## Open Questions

None
