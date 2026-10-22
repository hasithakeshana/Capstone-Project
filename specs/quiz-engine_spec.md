# Quiz Engine — Feature Spec

## Purpose

Learners attempt quizzes made of MCQ (single correct answer) and TRUE / FALSE questions. The system grades each attempt automatically with a fixed rule, records the score as an integer percentage, keeps every attempt with its timestamp, and keeps the best score. This feature covers AC-05 and AC-06, plus the Quiz Engine function in the capstone doc. It is delivered in Sprint 3.

## Actors

- Learner (attempts quizzes)
- Instructor (authors quiz questions; question authoring is specified in this spec)
- The system (grades attempts and keeps attempt history)

## User Stories

- As a learner, I want to attempt a quiz more than once, so that I can improve my score.
- As a learner, I want my best score kept, so that my result reflects my best attempt.
- As a learner, I want each attempt graded with the same rule every time, so that the score is predictable.
- As an instructor, I want to add MCQ and TRUE / FALSE questions to a quiz, so that the quiz can be graded automatically.

## Acceptance Criteria

### AC-05 Quiz supports MCQ (single correct) and TRUE / FALSE question types; quizzes are auto-graded by a deterministic rule

- Given a quiz with 4 questions of MCQ or TRUE / FALSE type, and I answer 3 of them correctly, When I submit the attempt, Then the score is 75%.
- Given a quiz with 4 questions and I answer none of them correctly, When I submit the attempt, Then the score is 0%.
- Given a quiz with 4 questions and I answer all of them correctly, When I submit the attempt, Then the score is 100%.
- Given an MCQ question with one correct option, When I select the correct option, Then the question is scored as correct.
- Given an MCQ question with one correct option, When I select any other option, Then the question is scored as incorrect.
- Given a TRUE / FALSE question whose correct answer is TRUE, When I answer FALSE, Then the question is scored as incorrect.
- Given the same answers are submitted in two attempts, When both attempts are graded, Then both get the same score. (DR-7)
- Given I am not signed in, When I submit an attempt, Then the request is rejected and nothing is recorded. (NFR-04)
- Given I am not enrolled in the course that contains the quiz, When I submit an attempt, Then the request is rejected and nothing is recorded. (Assess user journey, after Enroll; AC-01)
- Given I am the instructor and a course in DRAFT state, When I add an MCQ question with options and exactly one correct option, Then the question is saved to the quiz.
- Given I am the instructor, When I add a TRUE / FALSE question with its correct answer, Then the question is saved.
- Given I add an MCQ question with zero or more than one correct option, Then it is rejected. (AC-05 — single correct)
- Given I add a question of any other type, Then it is rejected. (AC-05)
- Given a course in PUBLISHED state, When the instructor tries to add or change a quiz question, Then it is rejected and the quiz is unchanged. (NFR-08)
- Given I am signed in as a learner, When I try to add a question, Then it is rejected. (NFR-04)

### AC-06 Learner can attempt a quiz multiple times; best score is recorded; each attempt is timestamped and append-only

- Given I have one attempt with a score of 50%, When I attempt the same quiz again with a score of 75%, Then both attempts are kept and my best score is 75%. (DR-8)
- Given my best score is 75% and I attempt the quiz again with a score of 50%, When the attempt is graded, Then my best score stays 75% and the new attempt is still recorded. (DR-8)
- Given I submit an attempt, When the attempt is recorded, Then it carries a timestamp. (AC-06, DR-8)
- Given an attempt has been recorded, When anyone tries to edit or delete it, Then the change is rejected and the record is unchanged. (NFR-02, DR-9)
- Given I am not signed in, When I request my attempt history, Then the request is rejected. (NFR-04)
- Given I am a learner, When I request another learner's attempts or quiz scores, Then the request is rejected. (NFR-08, DR-11)
- Given I submit an attempt, When the request is logged, Then the log does not contain my score or identity in plain text. (NFR-03, DR-13)

## Business Rules

- A quiz question is either MCQ with a single correct answer or TRUE / FALSE. (AC-05)
- Every attempt is graded automatically by a deterministic rule. (AC-05, DR-7)
- A quiz score is an integer percentage; no floating-point calculation is used. (NFR-01, DR-6)
- A learner can attempt a quiz many times, and the best score is kept. (AC-06, DR-8)
- Each attempt is timestamped, and attempts are append-only records. (AC-06, NFR-02, DR-9)
- Quiz scores are shown separately from course progress. (Progress Tracker)
- Instructors author quiz questions through the Instructor Workbench. Question authoring is specified in this spec. (AC-05)

## Applicable NFRs

- **NFR-01:** Quiz scores are whole-number percentages, with no floating-point math. (DR-6)
- **NFR-02:** Quiz attempts are only added, never edited or deleted. (DR-9)
- **NFR-03:** Quiz scores are learner performance data and are never written to logs in plain text. (DR-13)
- **NFR-04:** Submitting attempts and viewing attempt history are checked at the controller layer.
- **NFR-08:** An instructor cannot grade their own course's learners. Grading in this feature is automatic. See Open Questions for manual grading.

## Related User Journeys

- Assess (user journey) — attempt module-end quizzes, with multiple attempts and the best score kept.
- Quiz Engine (system function) — auto-grade MCQ and TRUE / FALSE attempts deterministically, and keep attempt history.
- Instructor Workbench (system function) — author quiz questions as part of a course. Covered in this spec (AC-05).

## Out of Scope

- Real proctoring and anti-cheat technology (out of scope list)
- Certificates tied to quiz results (out of scope list)
- Course progress percentage and lesson completion (Progress Tracker feature)
- Instructor view of learner progress bands (Instructor Workbench, AC-09 in instructor-workbench_spec.md)

## Open Questions

- Doc silent — to be decided later: rounding of integer percentages (floor or round).
- Doc silent — to be decided later: where a quiz sits in a course (module-end).
- Doc silent — to be decided later: partial credit.
