Status: DRAFT — refresh against the specs before running /sprint

# PRD: LearnLab Sprint 3 — Quiz Engine & Instructor Workbench

## 1. Problem & Goal

Learners need to test what they have learned with quizzes, and their best score must be kept. Instructors need to write quiz questions and see how their learners are progressing.

Sprint 3 builds on sprints 1 and 2: quizzes and quiz questions, auto-grading, quiz attempts, quiz scores in the learner's progress view, and the instructor progress bands.

Goal: a learner can attempt a quiz several times and see a best score, and an instructor can write quiz questions and see progress bands for a course.

## 2. Users & Jobs-to-be-done

- **Learner:** When I finish a module, I want to take its quiz as many times as I need, so that I can see my best score.
- **Instructor:** When I write a course, I want to add MCQ and TRUE / FALSE questions to its module quizzes, and see how learners are spread across progress bands, so that I can follow how the course is going.
- **Admin:** No new job in this sprint.

## 3. Functional Requirements

### 3.1 Carried forward (unchanged)

- **FR-1** (AC-02) An instructor can create a course with a title, description, category, and difficulty. (carried from sprint 1)
- **FR-2** (AC-02) A newly created course is stored in DRAFT state. (carried from sprint 1)
- **FR-3** (AC-02) Only an instructor can create a course; a learner's or an admin's request is rejected. (carried from sprint 1)
- **FR-4** (AC-02) The instructor who creates a course is stored as its owner. (carried from sprint 1)
- **FR-5** (AC-02) The web UI lets an instructor create a course and shows it with state DRAFT. (carried from sprint 1)
- **FR-6** (AC-08) Only an admin can change a course's state, including UNPUBLISHED → ARCHIVED. (carried from sprint 1)
- **FR-7** (AC-08) A course state can change only from DRAFT to PUBLISHED, from PUBLISHED to UNPUBLISHED, or from UNPUBLISHED to ARCHIVED. (carried from sprint 1)
- **FR-8** (AC-08) Any other course state change is rejected with InvalidCourseStateException, and the course state stays unchanged. (carried from sprint 1)
- **FR-9** (AC-04) An admin can publish a DRAFT course. (carried from sprint 1)
- **FR-10** (AC-04) An admin can unpublish a PUBLISHED course. (carried from sprint 1)
- **FR-11** (AC-04) Only an admin can publish or unpublish a course. (carried from sprint 1)
- **FR-12** (AC-04) The web UI lets an admin publish a DRAFT course and unpublish a PUBLISHED course, and shows the new state. (carried from sprint 1)
- **FR-13** (AC-01) A visitor can register an account, and the account gets the learner role. (carried from sprint 1)
- **FR-14** (AC-01) The web UI has a register page and a login page. (carried from sprint 1)
- **FR-15** (AC-01) A learner can enroll in a PUBLISHED course. (carried from sprint 1)
- **FR-16** (AC-01, NFR-04) Only a learner can enroll; an instructor's or an admin's enrollment request is rejected. (carried from sprint 1)
- **FR-17** (AC-01) A second enrollment by the same learner in the same course is rejected. (carried from sprint 1)
- **FR-18** (AC-01) An enrollment request for a course that is not PUBLISHED is rejected. (carried from sprint 1)
- **FR-19** (AC-01) A login with a correct email and password returns a token that carries the user's role. (carried from sprint 1)
- **FR-20** (AC-01) A login with a wrong password is rejected, and no token is returned. (carried from sprint 1)
- **FR-21** (AC-01) A request to a protected endpoint with no token, or with an invalid token, is rejected. (carried from sprint 1)
- **FR-22** (AC-01) On a PUBLISHED course in the catalog page, a learner can enroll with one action; the page then shows the course as enrolled, and a second enroll shows an error. (carried from sprint 1)
- **FR-23** (Browse) A learner can search published courses by category. (carried from sprint 1)
- **FR-24** (Browse) A learner can filter published courses by difficulty. (carried from sprint 1)
- **FR-25** (Browse) Courses in DRAFT, UNPUBLISHED, or ARCHIVED state are not listed to learners. (carried from sprint 1)
- **FR-26** (Browse) The web UI has a catalog page that lists PUBLISHED courses with category and difficulty filters. (carried from sprint 1)
- **FR-27** (Seed data) The seed data contains one admin account. (carried from sprint 1)
- **FR-28** (Seed data) The seed data contains two instructor accounts. (carried from sprint 1)
- **FR-29** (Seed data) The seed data contains three learner accounts. (carried from sprint 1)
- **FR-30** (Seed data) The seed data contains at least one course in each lifecycle state: DRAFT, PUBLISHED, UNPUBLISHED, and ARCHIVED. (carried from sprint 1)
- **FR-31** (Run) One command starts the app locally and loads the seed data. (carried from sprint 1)
- **FR-32** (AC-03) An instructor can add a module to a DRAFT course. (carried from sprint 2)
- **FR-33** (AC-03) An instructor can add a lesson to a module of a DRAFT course, giving the course → modules → lessons hierarchy. (carried from sprint 2)
- **FR-34** (AC-03, NFR-08) Adding a module or lesson to a PUBLISHED or UNPUBLISHED course is rejected, and the course structure is unchanged. (carried from sprint 2)
- **FR-35** (AC-03, NFR-04) A learner's request to add a module or lesson is rejected. (carried from sprint 2)
- **FR-36** (AC-07) A learner can mark a lesson complete in a course they are enrolled in. (carried from sprint 2)
- **FR-37** (AC-07) Course progress percentage equals completed lessons divided by total lessons. (carried from sprint 2)
- **FR-38** (AC-07, NFR-04) A learner who is not enrolled in the course, or is not signed in, cannot mark its lesson complete; the request is rejected and no completion is saved. (carried from sprint 2)
- **FR-39** (AC-10) An admin can view the admin catalog, which lists each course with its lifecycle state. (carried from sprint 2)
- **FR-40** (AC-10) An admin can approve a PUBLISHED course, and the approval is recorded for that course. (carried from sprint 2)
- **FR-41** (AC-10) An approval request for a DRAFT, UNPUBLISHED, or ARCHIVED course is rejected, and no approval is recorded. (carried from sprint 2)
- **FR-42** (AC-10) An admin can view enrollment-level analytics for a course, and the enrollment count shown equals the number of stored enrollments for that course. (carried from sprint 2)
- **FR-43** (AC-10) An admin can view engagement for a course, and the lesson completion count shown equals the number of stored lesson completions for that course. (carried from sprint 2)
- **FR-44** (AC-10, NFR-04) A learner's or an instructor's request for the admin catalog view or for enrollment analytics is rejected. (carried from sprint 2)
- **FR-45** (AC-10, NFR-04) Only an admin can approve a course; an instructor's or a learner's approval request is rejected. (carried from sprint 2)
- **FR-46** (Learn) A learner moves through the modules and lessons of a course sequentially. (carried from sprint 2)
- **FR-47** (Progress) A learner can view their own progress percentage for each course they are enrolled in. (carried from sprint 2)
- **FR-48** (Progress Tracker) The system computes and snapshots each learner's course progress. (carried from sprint 2)
- **FR-49** (AC-03) The web UI lets an instructor add modules and lessons to a DRAFT course, and shows them in the course. (carried from sprint 2)
- **FR-50** (Learn) The web UI course page lists the course's modules and lessons in order, with a mark-complete action for each lesson. (carried from sprint 2)
- **FR-51** (Progress) The web UI progress page shows a progress percentage for each enrolled course. (carried from sprint 2)
- **FR-52** (AC-10) The web UI admin console page shows the catalog with each course's state, an approve action for PUBLISHED courses, and enrollment and engagement counts. (carried from sprint 2)

### 3.2 New in this sprint

- **FR-53** (AC-05) An instructor can create one quiz for a module of a DRAFT course (a module-end quiz).
- **FR-54** (AC-05) An instructor can add an MCQ question with options and exactly one correct option to a quiz.
- **FR-55** (AC-05) An instructor can add a TRUE / FALSE question with its correct answer to a quiz.
- **FR-56** (AC-05) An MCQ question with zero correct options, or with more than one correct option, is rejected.
- **FR-57** (AC-05) A question of any type other than MCQ or TRUE / FALSE is rejected.
- **FR-58** (AC-05, NFR-04) A learner's request to add a quiz question is rejected.
- **FR-59** (AC-05, NFR-08) An add or change of a quiz question in a PUBLISHED course is rejected, and the quiz is unchanged.
- **FR-60** (AC-05) An MCQ answer scores as correct only when the learner selects the single correct option; any other selected option scores as incorrect.
- **FR-61** (AC-05) A TRUE / FALSE answer scores as correct only when it matches the correct answer.
- **FR-62** (AC-05) An attempt's score is the number of correct answers divided by the number of questions, expressed as an integer percentage.
- **FR-63** (AC-05) The same answers always produce the same score.
- **FR-64** (AC-05, NFR-04) An attempt submitted by a learner who is not signed in, or who is not enrolled in the course, is rejected, and nothing is recorded.
- **FR-65** (AC-05) A learner can attempt a quiz only in a course they are enrolled in.
- **FR-66** (AC-06) A learner can attempt the same quiz more than once.
- **FR-67** (AC-06) The learner's best score is the highest score among their attempts on the quiz.
- **FR-68** (AC-06) Each attempt is stored with a timestamp.
- **FR-69** (AC-06, NFR-02) A stored attempt cannot be edited or deleted; the request is rejected and the record is unchanged.
- **FR-70** (AC-06, NFR-08) A learner's request to view another learner's attempts or quiz scores is rejected.
- **FR-71** (Progress) The learner's progress view shows the quiz scores for each enrolled course.
- **FR-72** (AC-09) An instructor can view learner progress for a course, counted in four bands: 0–25%, 25–50%, 50–75%, and 75–100%.
- **FR-73** (AC-09) The instructor's view shows only aggregated band counts, never an individual learner's progress.
- **FR-74** (AC-09, NFR-08) An instructor's request to set or change a learner's quiz score or attempt in the instructor's own course is rejected, and the score is unchanged.
- **FR-75** (AC-09, NFR-04) A learner's request to view progress band counts is rejected.
- **FR-76** (Seed data) The seed data contains one sample quiz with an MCQ question and a TRUE / FALSE question.
- **FR-77** (AC-05) The web UI lets an instructor add MCQ and TRUE / FALSE questions to a module's quiz.
- **FR-78** (AC-06) The web UI lets a learner take a quiz and shows the score and the best score.
- **FR-79** (Progress) The web UI progress page shows the quiz scores for each enrolled course.
- **FR-80** (AC-09) The web UI instructor page shows the four band counts for a course.

## 4. Non-Functional Requirements

- **NFR-1** (NFR-04) Role checks run at the controller layer, and the learner, instructor, and admin roles are kept separate. (carried from sprint 1)
- **NFR-2** (NFR-02) Enrollment records are append-only; they are never edited or deleted. (carried from sprint 1)
- **NFR-3** (NFR-03) Learner personal data, such as email, is never written to logs in plain text. (carried from sprint 1)
- **NFR-4** (NFR-05) Database migrations are only added; existing migration files are never edited. (carried from sprint 1)
- **NFR-5** (NFR-06) Logs are structured JSON, and every log line for one request carries the same correlation ID. (carried from sprint 1)
- **NFR-6** (NFR-07) The health endpoint returns 200 within 1 second of a successful startup. (carried from sprint 1)
- **NFR-7** (NFR-08, part) A published course cannot be changed without an unpublish transition first; a test in tests/architecture/ verifies this rule. (carried from sprint 1)
- **NFR-8** (Quality gate) Coverage is measured with pytest-cov for the backend and @vitest/coverage-v8 for the frontend, with a minimum of 80%; the artefacts are reports/coverage.xml and reports/lcov.info. (carried from sprint 1)
- **NFR-9** (Quality gate) End-to-end tests run with Playwright and include screenshot snapshots. (carried from sprint 1)
- **NFR-10** (Quality gate) Every test carries the literal id "AC-NN" (or "NFR-NN", or the journey name for behaviour without an AC id): pytest test names start with test_acNN_ and carry an ac marker with the id, with docstrings starting "AC-NN:"; Vitest and Playwright titles start with "AC-NN". (carried from sprint 1)
- **NFR-11** (Quality gate) The frontend layout works without horizontal scrolling at 375 px (mobile) and 1280 px (desktop) widths. (carried from sprint 1)
- **NFR-12** (Architecture rule) Controllers do not import repositories directly. (carried from sprint 1)
- **NFR-13** (Architecture rule) The domain layer does not import services, repositories, controllers, or web or database frameworks. (carried from sprint 1)
- **NFR-14** (Architecture rule) Imports flow one way only: controllers → services → repositories → domain, enforced by import-linter and tests in tests/architecture/. (carried from sprint 1)
- **NFR-15** (Synthetic-Data rule) Seed data uses fake names and @example.com emails only. (carried from sprint 1)
- **NFR-16** (NFR-02) Lesson completions are append-only; they are never edited or deleted. (carried from sprint 2)
- **NFR-17** (NFR-03) Learner performance data, such as progress and lesson completions, is never written to logs in plain text. (carried from sprint 2)
- **NFR-18** (NFR-08) A learner cannot access another learner's progress; a test in tests/architecture/ verifies this rule. (carried from sprint 2)
- **NFR-19** (NFR-01) Quiz scores are integer percentages; no floating-point calculation is used.
- **NFR-20** (NFR-02) Quiz attempts are append-only; they are never edited or deleted.
- **NFR-21** (NFR-08) An instructor cannot grade their own courses' learners; a test in tests/architecture/ verifies this rule.

## 5. Out of Scope

- The system must not allow instructors or admins to register themselves; their accounts come from the seed data only.
- The system must not provide real video streaming or CDN integration (out of scope list in the capstone doc).
- The system must not provide a payment gateway or paid courses (out of scope list in the capstone doc).
- The system must not provide live virtual classes (out of scope list in the capstone doc).
- The system must not provide real proctoring or anti-cheat technology (out of scope list in the capstone doc).
- The system must not generate or verify certificates (out of scope list in the capstone doc).
- The system must not provide production deployment, secret management, or multi-region setup (out of scope list in the capstone doc).

## 6. Acceptance / Done

- **FR-1** → a stored course record holds the submitted title, description, category, and difficulty. (carried)
- **FR-2** → the stored state of a newly created course is DRAFT. (carried)
- **FR-3** → a create-course request from a learner or an admin is rejected, and no course record is stored. (carried)
- **FR-4** → the stored course record's owner is the instructor who created it. (carried)
- **FR-5** → after an instructor creates a course in the web UI, the page shows the course with state DRAFT. (carried)
- **FR-6** → a state-change request from an instructor or a learner is rejected, and the stored state is unchanged. (carried)
- **FR-7** → a state change from DRAFT to PUBLISHED, from PUBLISHED to UNPUBLISHED, or from UNPUBLISHED to ARCHIVED is stored as the new state. (carried)
- **FR-8** → any other state change returns InvalidCourseStateException, and the stored state is unchanged. (carried)
- **FR-9** → after an admin publishes a DRAFT course, its stored state is PUBLISHED. (carried)
- **FR-10** → after an admin unpublishes a PUBLISHED course, its stored state is UNPUBLISHED. (carried)
- **FR-11** → a publish or unpublish request from an instructor or a learner is rejected, and the stored state is unchanged. (carried)
- **FR-12** → after an admin publishes or unpublishes a course in the web UI, the page shows the new state. (carried)
- **FR-13** → a registration request stores a new account whose role is learner. (carried)
- **FR-14** → the web UI serves a register page and a login page. (carried)
- **FR-15** → an enrollment request by a learner for a PUBLISHED course stores one enrollment record for that learner and course. (carried)
- **FR-16** → an enrollment request from an instructor or an admin is rejected, and no enrollment record is stored. (carried)
- **FR-17** → a second enrollment request by the same learner for the same course is rejected, and the stored enrollment count for that pair stays at 1. (carried)
- **FR-18** → an enrollment request for a DRAFT, UNPUBLISHED, or ARCHIVED course is rejected, and no enrollment record is stored. (carried)
- **FR-19** → a login with a correct email and password returns a token, and the token carries the account's role. (carried)
- **FR-20** → a login with a wrong password returns a rejection, and the response contains no token. (carried)
- **FR-21** → a request to a protected endpoint with no token, or with an invalid token, is rejected, and no data is returned. (carried)
- **FR-22** → after a learner clicks enroll on a PUBLISHED course in the catalog page, the page shows the course as Enrolled; a second click shows an error. (carried)
- **FR-23** → a search by category returns only PUBLISHED courses in that category. (carried)
- **FR-24** → a filter by difficulty returns only PUBLISHED courses with that difficulty. (carried)
- **FR-25** → a browse result contains no course whose stored state is DRAFT, UNPUBLISHED, or ARCHIVED. (carried)
- **FR-26** → the catalog page lists PUBLISHED courses and shows category and difficulty filters. (carried)
- **FR-27** → after seeding, exactly one stored account has the admin role. (carried)
- **FR-28** → after seeding, exactly two stored accounts have the instructor role. (carried)
- **FR-29** → after seeding, exactly three stored accounts have the learner role. (carried)
- **FR-30** → after seeding, the stored courses include at least one course in each of DRAFT, PUBLISHED, UNPUBLISHED, and ARCHIVED states. (carried)
- **FR-31** → after the single run command, the app responds to requests, and the stored data contains the seed records from FR-27 to FR-30. (carried)
- **FR-32** → after an instructor adds a module to a DRAFT course, the stored course contains that module. (carried)
- **FR-33** → after an instructor adds a lesson to a module of a DRAFT course, the stored module contains that lesson. (carried)
- **FR-34** → an add-module or add-lesson request for a PUBLISHED or UNPUBLISHED course is rejected, and the stored course structure is unchanged. (carried)
- **FR-35** → an add-module or add-lesson request from a learner is rejected, and the stored course structure is unchanged. (carried)
- **FR-36** → after an enrolled learner marks a lesson complete, a completion record for that learner and lesson is stored. (carried)
- **FR-37** → after a learner completes 1 of 4 lessons in a course, the stored progress percentage for that learner and course is 25%. (carried)
- **FR-38** → a lesson-completion request from a learner who is not enrolled, or who is not signed in, is rejected, and no completion record is stored. (carried)
- **FR-39** → the admin catalog view lists each stored course with its stored lifecycle state. (carried)
- **FR-40** → after an admin approves a PUBLISHED course, a stored approval record exists for that course. (carried)
- **FR-41** → an approval request for a DRAFT, UNPUBLISHED, or ARCHIVED course is rejected, and no approval record is stored. (carried)
- **FR-42** → for a PUBLISHED course with 3 stored enrollments, the enrollment count shown in the admin's analytics is 3. (carried)
- **FR-43** → for a course with 5 stored lesson completions, the lesson completion count shown in the admin's engagement view is 5. (carried)
- **FR-44** → a request by a learner or an instructor for the admin catalog view or for enrollment analytics is rejected. (carried)
- **FR-45** → an approval request from an instructor or a learner is rejected, and no approval record is stored. (carried)
- **FR-46** → the lesson list returned to an enrolled learner follows the module order and the lesson order within each module. (carried)
- **FR-47** → the learner's progress view shows one progress percentage for each course the learner is enrolled in, and no entry for any other course. (carried)
- **FR-48** → after progress is calculated, a stored progress snapshot exists for each enrolled learner and course. (carried)
- **FR-49** → after an instructor adds a module and a lesson to a DRAFT course in the web UI, the course page lists both. (carried)
- **FR-50** → the course page for an enrolled learner lists modules and lessons in order, and each lesson has a mark-complete action; after the learner marks a lesson complete, the page shows it as complete. (carried)
- **FR-51** → the progress page shows one percentage for each enrolled course; after a learner completes 1 of 4 lessons, the page shows 25% for that course. (carried)
- **FR-52** → the admin console page lists each course with its state, shows an approve action for each PUBLISHED course, and shows the enrollment and engagement counts for each course. (carried)
- **FR-53** → after an instructor creates a quiz for a module of a DRAFT course, the stored module holds that quiz.
- **FR-54** → after an instructor adds an MCQ question with exactly one correct option to a quiz, the stored quiz contains that question.
- **FR-55** → after an instructor adds a TRUE / FALSE question with its correct answer to a quiz, the stored quiz contains that question.
- **FR-56** → an MCQ question with zero correct options, or with more than one, is rejected, and the stored quiz is unchanged.
- **FR-57** → a question of a type other than MCQ or TRUE / FALSE is rejected, and the stored quiz is unchanged.
- **FR-58** → a question-add request from a learner is rejected, and the stored quiz is unchanged.
- **FR-59** → an add or change of a quiz question in a PUBLISHED course is rejected, and the stored quiz is unchanged.
- **FR-60** → for a submitted MCQ answer, the stored result is correct only when the selected option is the single correct option.
- **FR-61** → for a submitted TRUE / FALSE answer, the stored result is correct only when the answer matches the correct answer.
- **FR-62** → an attempt with 3 correct answers out of 4 questions stores a score of 75%.
- **FR-63** → submitting the same answers in two attempts stores the same score for both.
- **FR-64** → an attempt from a learner who is not signed in, or who is not enrolled in the course, is rejected, and no attempt record is stored.
- **FR-65** → an attempt by an enrolled learner on a quiz in that course is stored; an attempt by a learner not enrolled in the course is rejected.
- **FR-66** → a second attempt by the same learner on the same quiz is stored, and both attempts are kept.
- **FR-67** → after attempts scoring 50% and then 75%, the stored best score is 75%; after a later attempt scoring 50%, the stored best score stays 75%.
- **FR-68** → every stored attempt record has a timestamp.
- **FR-69** → an edit or delete request for a stored attempt is rejected, and the stored record is unchanged.
- **FR-70** → a request by a learner for another learner's attempts or quiz scores is rejected.
- **FR-71** → the progress view lists the quiz score for each quiz in each enrolled course.
- **FR-72** → for a course with 2 learners at 10% and 60% progress, the band counts are 1 for 0–25%, 1 for 50–75%, and 0 for the other two bands.
- **FR-73** → the instructor's progress view for a course contains only band counts and no individual learner's progress.
- **FR-74** → a request by an instructor to set or change a learner's quiz score or attempt in the instructor's own course is rejected, and the stored score is unchanged.
- **FR-75** → a learner's request for progress band counts is rejected.
- **FR-76** → after seeding, the stored quizzes include one sample quiz that holds an MCQ question and a TRUE / FALSE question.
- **FR-77** → after an instructor adds an MCQ and a TRUE / FALSE question to a module's quiz in the web UI, the quiz page lists both questions.
- **FR-78** → after a learner submits a quiz in the web UI with 3 of 4 answers correct, the page shows a score of 75% and the best score for that quiz.
- **FR-79** → the progress page shows a quiz score for each quiz in each enrolled course.
- **FR-80** → the instructor page for a course shows four band counts, labelled 0–25%, 25–50%, 50–75%, and 75–100%.
- **NFR-1** → a request for an action outside the caller's role is rejected at the controller, and nothing is stored. (carried)
- **NFR-2** → after an enrollment is stored, an edit or delete request for it is rejected, and the stored record is unchanged. (carried)
- **NFR-3** → after a registration request, the log output contains no plain-text copy of the email. (carried)
- **NFR-5** → every log line for one request is a JSON object that carries the same correlation ID. (carried)
- **NFR-6** → the health endpoint returns 200 within 1 second of a successful startup. (carried)
- **NFR-7** → the architecture test for published-course immutability passes, and a change request to a PUBLISHED course is rejected with the course unchanged. (carried)
- **NFR-8** → the coverage run reports at least 80%, and reports/coverage.xml and reports/lcov.info exist. (carried)
- **NFR-9** → the end-to-end run passes, and its screenshot snapshot files exist. (carried)
- **NFR-11** → the catalog page at 375 px and at 1280 px width has no horizontal scrolling. (carried)
- **NFR-12** → the architecture test that checks controllers do not import repositories passes. (carried)
- **NFR-13** → the architecture test that checks the domain layer's imports passes. (carried)
- **NFR-14** → the architecture test that checks one-way imports, controllers → services → repositories → domain, passes. (carried)
- **NFR-16** → after a lesson completion is stored, an edit or delete request for it is rejected, and the stored record is unchanged. (carried)
- **NFR-17** → after a lesson completion or a progress calculation, the log output contains no plain-text progress or completion data for the learner. (carried)
- **NFR-18** → a request by one learner for another learner's progress is rejected, no progress is returned, and the architecture test for learner progress access passes. (carried)
- **NFR-19** → every stored quiz score is an integer percentage, and no floating-point value is stored or returned as a score.
- **NFR-20** → after a quiz attempt is stored, an edit or delete request for it is rejected, and the stored record is unchanged.
- **NFR-21** → a request by an instructor to grade a learner in the instructor's own course is rejected, no score is stored, and the architecture test for instructor grading passes.

<!-- To decide at refresh:
- Quiz placement: where a quiz sits in a course beyond one quiz per module, and how many quizzes a module can have.
- Partial credit: whether a question or a quiz can earn partial credit.
- Rounding: whether integer percentages are rounded down or to the nearest integer.
- Band boundary: which band takes a progress of exactly 25%, 50%, or 75%.
-->
