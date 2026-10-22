# PRD: LearnLab Sprint 1 — Catalog & Enrollment

## 1. Problem & Goal

Learners need to find published courses and enroll in each one once. Admins need control over which courses learners can see. Instructors need to create courses as drafts before they are published.

Sprint 1 builds that foundation: the course lifecycle, the catalog, learner self-registration, login, enrollment, seed data, and the architecture rules.

Goal: a running app where a learner can register, log in, browse published courses, and enroll once, with seed data and architecture rules in place for sprints 2 and 3.

## 2. Users & Jobs-to-be-done

- **Learner:** When I want to learn a topic, I want to find published courses by category and difficulty and enroll once, so that I can start learning.
- **Instructor:** When I plan a new course, I want to create it as a draft, so that I can build it before it is published.
- **Admin:** When a course is ready, I want to publish or unpublish it, so that learners only see the courses I release.

## 3. Functional Requirements

- **FR-1** (AC-02) An instructor can create a course with a title, description, category, and difficulty.
- **FR-2** (AC-02) A newly created course is stored in DRAFT state.
- **FR-3** (AC-02) Only an instructor can create a course; a learner's or an admin's request is rejected.
- **FR-4** (AC-02) The instructor who creates a course is stored as its owner.
- **FR-5** (AC-02) The web UI lets an instructor create a course and shows it with state DRAFT.
- **FR-6** (AC-08) Only an admin can change a course's state, including UNPUBLISHED → ARCHIVED.
- **FR-7** (AC-08) A course state can change only from DRAFT to PUBLISHED, from PUBLISHED to UNPUBLISHED, or from UNPUBLISHED to ARCHIVED.
- **FR-8** (AC-08) Any other course state change is rejected with InvalidCourseStateException, and the course state stays unchanged.
- **FR-9** (AC-04) An admin can publish a DRAFT course.
- **FR-10** (AC-04) An admin can unpublish a PUBLISHED course.
- **FR-11** (AC-04) Only an admin can publish or unpublish a course.
- **FR-12** (AC-04) The web UI lets an admin publish a DRAFT course and unpublish a PUBLISHED course, and shows the new state.
- **FR-13** (AC-01) A visitor can register an account, and the account gets the learner role.
- **FR-14** (AC-01) The web UI has a register page and a login page.
- **FR-15** (AC-01) A learner can enroll in a PUBLISHED course.
- **FR-16** (AC-01, NFR-04) Only a learner can enroll; an instructor's or an admin's enrollment request is rejected.
- **FR-17** (AC-01) A second enrollment by the same learner in the same course is rejected.
- **FR-18** (AC-01) An enrollment request for a course that is not PUBLISHED is rejected.
- **FR-19** (AC-01) A login with a correct email and password returns a token that carries the user's role.
- **FR-20** (AC-01) A login with a wrong password is rejected, and no token is returned.
- **FR-21** (AC-01) A request to a protected endpoint with no token, or with an invalid token, is rejected.
- **FR-22** (AC-01) On a PUBLISHED course in the catalog page, a learner can enroll with one action; the page then shows the course as enrolled, and a second enroll shows an error.
- **FR-23** (Browse) A learner can search published courses by category.
- **FR-24** (Browse) A learner can filter published courses by difficulty.
- **FR-25** (Browse) Courses in DRAFT, UNPUBLISHED, or ARCHIVED state are not listed to learners.
- **FR-26** (Browse) The web UI has a catalog page that lists PUBLISHED courses with category and difficulty filters.
- **FR-27** (Seed data) The seed data contains one admin account.
- **FR-28** (Seed data) The seed data contains two instructor accounts.
- **FR-29** (Seed data) The seed data contains three learner accounts.
- **FR-30** (Seed data) The seed data contains at least one course in each lifecycle state: DRAFT, PUBLISHED, UNPUBLISHED, and ARCHIVED.
- **FR-31** (Run) One command starts the app locally and loads the seed data.

## 4. Non-Functional Requirements

- **NFR-1** (NFR-04) Role checks run at the controller layer, and the learner, instructor, and admin roles are kept separate.
- **NFR-2** (NFR-02) Enrollment records are append-only; they are never edited or deleted.
- **NFR-3** (NFR-03) Learner personal data, such as email, is never written to logs in plain text.
- **NFR-4** (NFR-05) Database migrations are only added; existing migration files are never edited.
- **NFR-5** (NFR-06) Logs are structured JSON, and every log line for one request carries the same correlation ID.
- **NFR-6** (NFR-07) The health endpoint returns 200 within 1 second of a successful startup.
- **NFR-7** (NFR-08, part) A published course cannot be changed without an unpublish transition first; a test in tests/architecture/ verifies this rule.
- **NFR-8** (Quality gate) Coverage is measured with pytest-cov for the backend and @vitest/coverage-v8 for the frontend, with a minimum of 80%; the artefacts are reports/coverage.xml and reports/lcov.info.
- **NFR-9** (Quality gate) End-to-end tests run with Playwright and include screenshot snapshots.
- **NFR-10** (Quality gate) Every test carries the literal id "AC-NN" (or "NFR-NN", or the journey name for behaviour without an AC id): pytest test names start with test_acNN_ and carry an ac marker with the id, with docstrings starting "AC-NN:"; Vitest and Playwright titles start with "AC-NN".
- **NFR-11** (Quality gate) The frontend layout works without horizontal scrolling at 375 px (mobile) and 1280 px (desktop) widths.
- **NFR-12** (Architecture rule) Controllers do not import repositories directly.
- **NFR-13** (Architecture rule) The domain layer does not import services, repositories, controllers, or web or database frameworks.
- **NFR-14** (Architecture rule) Imports flow one way only: controllers → services → repositories → domain, enforced by import-linter and tests in tests/architecture/.
- **NFR-15** (Synthetic-Data rule) Seed data uses fake names and @example.com emails only.

## 5. Out of Scope

- The system must not allow instructors or admins to register themselves; their accounts come from the seed data only.
- The system must not let anyone add modules or lessons to a course (AC-03, Sprint 2).
- The system must not record lesson completions or calculate course progress (AC-07, Sprint 2).
- The system must not provide admin approval of published courses or enrollment and engagement analytics (AC-10, Sprint 2).
- The system must not provide quiz questions, quiz attempts, or quiz auto-grading (AC-05, AC-06, Sprint 3).
- The system must not show instructor progress bands (AC-09, Sprint 3).
- The seed data must not include sample quizzes (Sprint 3).
- The system must not provide real video streaming or CDN integration (out of scope list in the capstone doc).
- The system must not provide a payment gateway or paid courses (out of scope list in the capstone doc).
- The system must not provide live virtual classes (out of scope list in the capstone doc).
- The system must not provide real proctoring or anti-cheat technology (out of scope list in the capstone doc).
- The system must not generate or verify certificates (out of scope list in the capstone doc).
- The system must not provide production deployment, secret management, or multi-region setup (out of scope list in the capstone doc).

## 6. Acceptance / Done

- **FR-1** → a stored course record holds the submitted title, description, category, and difficulty.
- **FR-2** → the stored state of a newly created course is DRAFT.
- **FR-3** → a create-course request from a learner or an admin is rejected, and no course record is stored.
- **FR-4** → the stored course record's owner is the instructor who created it.
- **FR-5** → after an instructor creates a course in the web UI, the page shows the course with state DRAFT.
- **FR-6** → a state-change request from an instructor or a learner is rejected, and the stored state is unchanged.
- **FR-7** → a state change from DRAFT to PUBLISHED, from PUBLISHED to UNPUBLISHED, or from UNPUBLISHED to ARCHIVED is stored as the new state.
- **FR-8** → any other state change returns InvalidCourseStateException, and the stored state is unchanged.
- **FR-9** → after an admin publishes a DRAFT course, its stored state is PUBLISHED.
- **FR-10** → after an admin unpublishes a PUBLISHED course, its stored state is UNPUBLISHED.
- **FR-11** → a publish or unpublish request from an instructor or a learner is rejected, and the stored state is unchanged.
- **FR-12** → after an admin publishes or unpublishes a course in the web UI, the page shows the new state.
- **FR-13** → a registration request stores a new account whose role is learner.
- **FR-14** → the web UI serves a register page and a login page.
- **FR-15** → an enrollment request by a learner for a PUBLISHED course stores one enrollment record for that learner and course.
- **FR-16** → an enrollment request from an instructor or an admin is rejected, and no enrollment record is stored.
- **FR-17** → a second enrollment request by the same learner for the same course is rejected, and the stored enrollment count for that pair stays at 1.
- **FR-18** → an enrollment request for a DRAFT, UNPUBLISHED, or ARCHIVED course is rejected, and no enrollment record is stored.
- **FR-19** → a login with a correct email and password returns a token, and the token carries the account's role.
- **FR-20** → a login with a wrong password returns a rejection, and the response contains no token.
- **FR-21** → a request to a protected endpoint with no token, or with an invalid token, is rejected, and no data is returned.
- **FR-22** → after a learner clicks enroll on a PUBLISHED course in the catalog page, the page shows the course as Enrolled; a second click shows an error.
- **FR-23** → a search by category returns only PUBLISHED courses in that category.
- **FR-24** → a filter by difficulty returns only PUBLISHED courses with that difficulty.
- **FR-25** → a browse result contains no course whose stored state is DRAFT, UNPUBLISHED, or ARCHIVED.
- **FR-26** → the catalog page lists PUBLISHED courses and shows category and difficulty filters.
- **FR-27** → after seeding, exactly one stored account has the admin role.
- **FR-28** → after seeding, exactly two stored accounts have the instructor role.
- **FR-29** → after seeding, exactly three stored accounts have the learner role.
- **FR-30** → after seeding, the stored courses include at least one course in each of DRAFT, PUBLISHED, UNPUBLISHED, and ARCHIVED states.
- **FR-31** → after the single run command, the app responds to requests, and the stored data contains the seed records from FR-27 to FR-30.
- **NFR-1** → a request for an action outside the caller's role is rejected at the controller, and nothing is stored.
- **NFR-2** → after an enrollment is stored, an edit or delete request for it is rejected, and the stored record is unchanged.
- **NFR-3** → after a registration request, the log output contains no plain-text copy of the email.
- **NFR-5** → every log line for one request is a JSON object that carries the same correlation ID.
- **NFR-6** → the health endpoint returns 200 within 1 second of a successful startup.
- **NFR-7** → the architecture test for published-course immutability passes, and a change request to a PUBLISHED course is rejected with the course unchanged.
- **NFR-8** → the coverage run reports at least 80%, and reports/coverage.xml and reports/lcov.info exist.
- **NFR-9** → the end-to-end run passes, and its screenshot snapshot files exist.
- **NFR-11** → the catalog page at 375 px and at 1280 px width has no horizontal scrolling.
- **NFR-12** → the architecture test that checks controllers do not import repositories passes.
- **NFR-13** → the architecture test that checks the domain layer's imports passes.
- **NFR-14** → the architecture test that checks one-way imports, controllers → services → repositories → domain, passes.
