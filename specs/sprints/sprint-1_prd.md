# PRD: LearnLab Sprint 1 — Catalog & Enrollment

## 1. Problem & Goal

Learners need to find published courses and enroll in each one once. Admins need to control which courses learners can see. Instructors need to create courses as drafts before they are published.

Sprint 1 builds that foundation: the course lifecycle, the catalog, learner self-registration, login, enrollment, seed data, and the architecture rules.

Goal: a running app where a learner can register, log in, browse published courses, and enroll once, with seed data and architecture rules in place for sprints 2 and 3.

## 2. Users & Jobs-to-be-done

- **Learner:** When I want to learn a topic, I want to find published courses by category and difficulty and enroll once, so that I can start learning.
- **Instructor:** When I plan a new course, I want to create it as a draft, so that I can build it before it is published.
- **Admin:** When a course is ready, I want to publish or unpublish it, so that learners only see the courses I release.

## 3. Functional Requirements

- **FR-1** (AC-02) An instructor can create a course with a title, description, category, and difficulty.
- **FR-2** (AC-02) A newly created course is stored in DRAFT state.
- **FR-3** (AC-02) A learner cannot create a course.
- **FR-4** (AC-08) A course state can change only from DRAFT to PUBLISHED, from PUBLISHED to UNPUBLISHED, or from UNPUBLISHED to ARCHIVED.
- **FR-5** (AC-08) Any other course state change is rejected with InvalidCourseStateException, and the course state stays unchanged.
- **FR-6** (AC-04) An admin can publish a DRAFT course.
- **FR-7** (AC-04) An admin can unpublish a PUBLISHED course.
- **FR-8** (AC-04) Only an admin can publish or unpublish a course.
- **FR-9** (AC-01) A visitor can register an account, and the account gets the learner role.
- **FR-10** (AC-01) A learner can enroll in a PUBLISHED course.
- **FR-11** (AC-01) A second enrollment by the same learner in the same course is rejected.
- **FR-12** (AC-01) An enrollment request for a course that is not PUBLISHED is rejected.
- **FR-13** (AC-01) A login with a correct email and password returns a token that carries the user's role.
- **FR-14** (AC-01) A login with a wrong password is rejected, and no token is returned.
- **FR-15** (AC-01) A request to a protected endpoint with no token, or with an invalid token, is rejected.
- **FR-16** (Browse — no AC id) A learner can search published courses by category.
- **FR-17** (Browse — no AC id) A learner can filter published courses by difficulty.
- **FR-18** (Browse — no AC id) Courses in DRAFT, UNPUBLISHED, or ARCHIVED state are not listed to learners.
- **FR-19** (Seed data — no AC id) The seed data contains one admin account.
- **FR-20** (Seed data — no AC id) The seed data contains two instructor accounts.
- **FR-21** (Seed data — no AC id) The seed data contains three learner accounts.
- **FR-22** (Seed data — no AC id) The seed data contains at least one course in each lifecycle state: DRAFT, PUBLISHED, UNPUBLISHED, and ARCHIVED.
- **FR-23** (Architecture — no AC id) Controllers do not import repositories directly.
- **FR-24** (Architecture — no AC id) The domain layer does not import services, repositories, controllers, or web or database frameworks.
- **FR-25** (Architecture — no AC id) Imports flow one way only: controllers → services → repositories → domain.
- **FR-26** (Run — no AC id) One command starts the app locally and loads the seed data.

## 4. Non-Functional Requirements

- **NFR-1** (NFR-04) Role checks run at the controller layer, and the learner, instructor, and admin roles are kept separate.
- **NFR-2** (NFR-02) Enrollment records are append-only; they are never edited or deleted.
- **NFR-3** (NFR-03) Learner personal data, such as email, is never written to logs in plain text.
- **NFR-4** (NFR-05) Database migrations are only added; existing migration files are never edited.
- **NFR-5** (NFR-06) Logs are structured JSON, and every log line for one request carries the same correlation ID.
- **NFR-6** (NFR-07) The health endpoint returns 200 within 1 second of a successful startup.
- **NFR-7** (NFR-08, part) A published course cannot be changed without an unpublish transition first.
- **NFR-8** (no NFR id — coverage) Coverage is measured with pytest-cov for the backend and @vitest/coverage-v8 for the frontend, with a minimum of 80%.
- **NFR-9** (no NFR id — end-to-end) End-to-end tests run with Playwright and include screenshot snapshots.
- **NFR-10** (no NFR id — test naming) Every test name carries its AC id, or the name of the user journey or NFR it covers when no AC id exists.
- **NFR-11** (no NFR id — frontend) The frontend layout is responsive.

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

- **FR-1** → a stored course record has the submitted title, description, category, and difficulty.
- **FR-2** → the stored state of a newly created course is DRAFT.
- **FR-3** → a create-course request sent by a learner is rejected, and no course record is stored.
- **FR-4** → a state change from DRAFT to PUBLISHED, from PUBLISHED to UNPUBLISHED, or from UNPUBLISHED to ARCHIVED is stored as the new state.
- **FR-5** → any other state change returns InvalidCourseStateException, and the stored state is unchanged.
- **FR-6** → after an admin publishes a DRAFT course, its stored state is PUBLISHED.
- **FR-7** → after an admin unpublishes a PUBLISHED course, its stored state is UNPUBLISHED.
- **FR-8** → a publish or unpublish request sent by an instructor or a learner is rejected, and the stored state is unchanged.
- **FR-9** → a registration request stores a new account whose role is learner.
- **FR-10** → an enrollment request for a PUBLISHED course stores one enrollment record for that learner and course.
- **FR-11** → a second enrollment request by the same learner for the same course is rejected, and the stored enrollment count for that pair stays at 1.
- **FR-12** → an enrollment request for a DRAFT, UNPUBLISHED, or ARCHIVED course is rejected, and no enrollment record is stored.
- **FR-13** → a login with a correct email and password returns a token, and the token carries the account's role.
- **FR-14** → a login with a wrong password returns a rejection, and the response contains no token.
- **FR-15** → a request to a protected endpoint with no token, or with an invalid token, is rejected, and no data is returned.
- **FR-16** → a browse request for category C returns only PUBLISHED courses in category C.
- **FR-17** → a browse request for difficulty D returns only PUBLISHED courses with difficulty D.
- **FR-18** → a browse result contains no course whose stored state is DRAFT, UNPUBLISHED, or ARCHIVED.
- **FR-19** → after seeding, the stored accounts include exactly one account with the admin role.
- **FR-20** → after seeding, the stored accounts include exactly two accounts with the instructor role.
- **FR-21** → after seeding, the stored accounts include exactly three accounts with the learner role.
- **FR-22** → after seeding, the stored courses include at least one course in each of DRAFT, PUBLISHED, UNPUBLISHED, and ARCHIVED states.
- **FR-23** → the architecture test that checks controllers do not import repositories passes.
- **FR-24** → the architecture test that checks the domain layer imports nothing from services, repositories, controllers, or web or database frameworks passes.
- **FR-25** → the architecture test that checks one-way imports, controllers → services → repositories → domain, passes.
- **FR-26** → after the single run command, the app responds to requests and the stored data contains the seed records from FR-19 to FR-22.
