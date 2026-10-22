Status: DRAFT — refresh against the specs before running /sprint

# PRD: LearnLab Sprint 2 — Lessons, Progress & Admin Console

## 1. Problem & Goal

Instructors need to build the structure of a course: modules, and lessons inside them, on a draft course. Learners need to work through a course's lessons in order, mark them complete, and see how far they have come. Admins need to approve published courses and see enrollment and engagement counts.

Sprint 2 builds on sprint 1: course authoring of modules and lessons, lesson completion, course progress, the learner's own progress view, and the admin console.

Goal: an instructor can build a draft course's modules and lessons, an enrolled learner can complete lessons and see their own progress percentage, and an admin can approve published courses and see enrollment and engagement counts.

## 2. Users & Jobs-to-be-done

- **Learner:** When I am enrolled in a course, I want to work through its lessons in order and mark each one complete, so that I can see how far I have come.
- **Instructor:** When I am building a draft course, I want to add modules and lessons to it, so that learners get a clear structure.
- **Admin:** When a course is published, I want to approve it and see its enrollment and engagement counts, so that I can monitor the catalog.

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

### 3.2 New in this sprint

- **FR-32** (AC-03) An instructor can add a module to a DRAFT course.
- **FR-33** (AC-03) An instructor can add a lesson to a module of a DRAFT course, giving the course → modules → lessons hierarchy.
- **FR-34** (AC-03, NFR-08) Adding a module or lesson to a PUBLISHED or UNPUBLISHED course is rejected, and the course structure is unchanged.
- **FR-35** (AC-03, NFR-04) A learner's request to add a module or lesson is rejected.
- **FR-36** (AC-07) A learner can mark a lesson complete in a course they are enrolled in.
- **FR-37** (AC-07) Course progress percentage equals completed lessons divided by total lessons.
- **FR-38** (AC-07, NFR-04) A learner who is not enrolled in the course, or is not signed in, cannot mark its lesson complete; the request is rejected and no completion is saved.
- **FR-39** (AC-10) An admin can view the admin catalog, which lists each course with its lifecycle state.
- **FR-40** (AC-10) An admin can approve a PUBLISHED course, and the approval is recorded for that course.
- **FR-41** (AC-10) An approval request for a DRAFT, UNPUBLISHED, or ARCHIVED course is rejected, and no approval is recorded.
- **FR-42** (AC-10) An admin can view enrollment-level analytics for a course, and the enrollment count shown equals the number of stored enrollments for that course.
- **FR-43** (AC-10) An admin can view engagement for a course, and the lesson completion count shown equals the number of stored lesson completions for that course.
- **FR-44** (AC-10, NFR-04) A learner's or an instructor's request for the admin catalog view or for enrollment analytics is rejected.
- **FR-45** (AC-10, NFR-04) Only an admin can approve a course; an instructor's or a learner's approval request is rejected.
- **FR-46** (Learn) A learner moves through the modules and lessons of a course sequentially.
- **FR-47** (Progress) A learner can view their own progress percentage for each course they are enrolled in.
- **FR-48** (Progress Tracker) The system computes and snapshots each learner's course progress.
- **FR-49** (AC-03) The web UI lets an instructor add modules and lessons to a DRAFT course, and shows them in the course.
- **FR-50** (Learn) The web UI course page lists the course's modules and lessons in order, with a mark-complete action for each lesson.
- **FR-51** (Progress) The web UI progress page shows a progress percentage for each enrolled course.
- **FR-52** (AC-10) The web UI admin console page shows the catalog with each course's state, an approve action for PUBLISHED courses, and enrollment and engagement counts.

## 4. Non-Functional Requirements

- **NFR-1** (NFR-04) Role checks run at the controller layer, and the learner, instructor, and admin roles are kept separate. (carried from sprint 1)
- **NFR-2** (NFR-02) Enrollment records are append-only; they are never edited or deleted. (carried from sprint 1)
- **NFR-3** (NFR-03) Learner personal data, such as email, is never written to logs in plain text. (carried from sprint 1)
- **NFR-4** (NFR-05) Database migrations are only added; existing migration files are never edited. (carried from sprint 1)
- **NFR-5** (NFR-06) Logs are structured JSON, and every log line for one request carries the same correlation ID. (carried from sprint 1)
- **NFR-6** (NFR-07) The health endpoint returns 200 within 1 second of a successful startup. (carried from sprint 1)
- **NFR-7** (NFR-08, part) A published course cannot be changed without an unpublish transition first. (carried from sprint 1)
- **NFR-8** (Quality gate) Coverage is measured with pytest-cov for the backend and @vitest/coverage-v8 for the frontend, with a minimum of 80%; the artefacts are reports/coverage.xml and reports/lcov.info. (carried from sprint 1)
- **NFR-9** (Quality gate) End-to-end tests run with Playwright and include screenshot snapshots. (carried from sprint 1)
- **NFR-10** (Quality gate) Every test carries the literal id "AC-NN" (or "NFR-NN", or the journey name for behaviour without an AC id): pytest test names start with test_acNN_ and carry an ac marker with the id, with docstrings starting "AC-NN:"; Vitest and Playwright titles start with "AC-NN". (carried from sprint 1)
- **NFR-11** (Quality gate) The frontend layout works without horizontal scrolling at 375 px (mobile) and 1280 px (desktop) widths. (carried from sprint 1)
- **NFR-12** (Architecture rule) Controllers do not import repositories directly. (carried from sprint 1)
- **NFR-13** (Architecture rule) The domain layer does not import services, repositories, controllers, or web or database frameworks. (carried from sprint 1)
- **NFR-14** (Architecture rule) Imports flow one way only: controllers → services → repositories → domain, enforced by import-linter and tests in tests/architecture/. (carried from sprint 1)
- **NFR-15** (Synthetic-Data rule) Seed data uses fake names and @example.com emails only. (carried from sprint 1)
- **NFR-16** (NFR-02) Lesson completions are append-only; they are never edited or deleted.
- **NFR-17** (NFR-03) Learner performance data, such as progress and lesson completions, is never written to logs in plain text.
- **NFR-18** (NFR-08) A learner cannot access another learner's progress.

## 5. Out of Scope

- The system must not provide quiz questions, quiz attempts, or quiz auto-grading (AC-05, AC-06, Sprint 3).
- The system must not show quiz scores in the learner's progress view (Sprint 3).
- The system must not show instructor progress bands (AC-09, Sprint 3).
- The seed data must not include sample quizzes (Sprint 3).
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
- **FR-32** → after an instructor adds a module to a DRAFT course, the stored course contains that module.
- **FR-33** → after an instructor adds a lesson to a module of a DRAFT course, the stored module contains that lesson.
- **FR-34** → an add-module or add-lesson request for a PUBLISHED or UNPUBLISHED course is rejected, and the stored course structure is unchanged.
- **FR-35** → an add-module or add-lesson request from a learner is rejected, and the stored course structure is unchanged.
- **FR-36** → after an enrolled learner marks a lesson complete, a completion record for that learner and lesson is stored.
- **FR-37** → after a learner completes 1 of 4 lessons in a course, the stored progress percentage for that learner and course is 25%.
- **FR-38** → a lesson-completion request from a learner who is not enrolled, or who is not signed in, is rejected, and no completion record is stored.
- **FR-39** → the admin catalog view lists each stored course with its stored lifecycle state.
- **FR-40** → after an admin approves a PUBLISHED course, a stored approval record exists for that course.
- **FR-41** → an approval request for a DRAFT, UNPUBLISHED, or ARCHIVED course is rejected, and no approval record is stored.
- **FR-42** → for a PUBLISHED course with 3 stored enrollments, the enrollment count shown in the admin's analytics is 3.
- **FR-43** → for a course with 5 stored lesson completions, the lesson completion count shown in the admin's engagement view is 5.
- **FR-44** → a request by a learner or an instructor for the admin catalog view or for enrollment analytics is rejected.
- **FR-45** → an approval request from an instructor or a learner is rejected, and no approval record is stored.
- **FR-46** → the lesson list returned to an enrolled learner follows the module order and the lesson order within each module.
- **FR-47** → the learner's progress view shows one progress percentage for each course the learner is enrolled in, and no entry for any other course.
- **FR-48** → after progress is calculated, a stored progress snapshot exists for each enrolled learner and course.
- **FR-49** → after an instructor adds a module and a lesson to a DRAFT course in the web UI, the course page lists both.
- **FR-50** → the course page for an enrolled learner lists modules and lessons in order, and each lesson has a mark-complete action; after the learner marks a lesson complete, the page shows it as complete.
- **FR-51** → the progress page shows one percentage for each enrolled course; after a learner completes 1 of 4 lessons, the page shows 25% for that course.
- **FR-52** → the admin console page lists each course with its state, shows an approve action for each PUBLISHED course, and shows the enrollment and engagement counts for each course.
- **NFR-1** → a request for an action outside the caller's role is rejected at the controller, and nothing is stored. (carried)
- **NFR-2** → after an enrollment is stored, an edit or delete request for it is rejected, and the stored record is unchanged. (carried)
- **NFR-3** → after a registration request, the log output contains no plain-text copy of the email. (carried)
- **NFR-5** → every log line for one request is a JSON object that carries the same correlation ID. (carried)
- **NFR-6** → the health endpoint returns 200 within 1 second of a successful startup. (carried)
- **NFR-8** → the coverage run reports at least 80%, and reports/coverage.xml and reports/lcov.info exist. (carried)
- **NFR-9** → the end-to-end run passes, and its screenshot snapshot files exist. (carried)
- **NFR-11** → the catalog page at 375 px and at 1280 px width has no horizontal scrolling. (carried)
- **NFR-12** → the architecture test that checks controllers do not import repositories passes. (carried)
- **NFR-13** → the architecture test that checks the domain layer's imports passes. (carried)
- **NFR-14** → the architecture test that checks one-way imports, controllers → services → repositories → domain, passes. (carried)
- **NFR-16** → after a lesson completion is stored, an edit or delete request for it is rejected, and the stored record is unchanged.
- **NFR-17** → after a lesson completion or a progress calculation, the log output contains no plain-text progress or completion data for the learner.
- **NFR-18** → a request by one learner for another learner's progress is rejected, and no progress is returned.
