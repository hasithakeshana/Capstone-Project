# LearnLab — Application Specification

## 1. Purpose

LearnLab is a lightweight learning management system. It lets learners find and enroll in published courses, learn through lessons, and take quizzes. It lets instructors author courses and see learner progress. It lets admins control what is published and watch enrollment activity. This document is the root specification for the whole application. The feature specs add detail for each area.

## 2. Roles & Permissions

| Action | Learner | Instructor | Admin |
|---|---|---|---|
| Register as a learner (AC-01) | ✓ | ✗ | ✗ |
| Enroll in a PUBLISHED course (AC-01) | ✓ | ✗ | ✗ |
| Browse and search published courses (Browse, user journey) | ✓ | ✗ | ✗ |
| Create a DRAFT course (AC-02) | ✗ | ✓ | ✗ |
| Add modules and lessons to a DRAFT course (AC-03) | ✗ | ✓ | ✗ |
| Author quiz questions (Instructor Workbench) | ✗ | ✓ | ✗ |
| Publish or unpublish a course (AC-04) | ✗ | ✗ | ✓ |
| Approve published courses (AC-10) | ✗ | ✗ | ✓ |
| Mark a lesson complete (AC-07) | ✓ | ✗ | ✗ |
| Attempt a quiz (AC-06) | ✓ | ✗ | ✗ |
| View own progress and quiz scores (Progress, user journey) | ✓ | ✗ | ✗ |
| View learner progress aggregated by course (AC-09) | ✗ | ✓ | ✗ |
| Monitor enrollment-level analytics (AC-10) | ✗ | ✗ | ✓ |
| View another learner's progress (NFR-08) | ✗ | ✗ | ✗ |
| Grade own course's learners (NFR-08) | ✗ | ✗ | ✗ |

## 3. Domain Model

- **User:** has one role: learner, instructor, or admin.
- **Course:** has a title, description, category, and difficulty. It has a lifecycle state (see Section 4). Each course contains modules.
- **Module:** belongs to one course and contains lessons. Lessons are in a module.
- **Lesson:** belongs to one module. A learner can mark a lesson complete.
- **Quiz:** a set of questions. Per the Assess user journey, quizzes are module-end quizzes. *Doc silent — to be decided later: exactly how a quiz attaches to a module.*
- **Question:** belongs to a quiz. Two types exist: MCQ with a single correct answer, and TRUE/FALSE.
- **Enrollment:** links one learner to one course. Only one enrollment exists per learner and course pair.
- **LessonCompletion:** records that a learner completed a lesson.
- **QuizAttempt:** records one attempt by a learner on a quiz, with its score and timestamp.

## 4. Course Lifecycle

Allowed transitions, as stated in AC-08:

| From | To | Allowed |
|---|---|---|
| DRAFT | PUBLISHED | ✓ |
| PUBLISHED | UNPUBLISHED | ✓ |
| UNPUBLISHED | ARCHIVED | ✓ |
| Any other move (for example UNPUBLISHED → PUBLISHED) | — | ✗ raises InvalidCourseStateException |

- Every new course starts in DRAFT (AC-02).
- The instructor who creates a course is stored as its owner (AC-02).
- Only an admin can change a course's state, including UNPUBLISHED → ARCHIVED (AC-08).
## 5. Acceptance Criteria

*Each AC must have at least one test referencing its AC-NN identifier.*

- **AC-01:** Learner can register and enroll in any PUBLISHED course; a learner cannot enroll twice in the same course. Detail: specs/enrollment_spec.md (registration included)
- **AC-02:** Instructor can create a course with title, description, category, and difficulty; courses start in DRAFT state. Detail: specs/course-authoring_spec.md
- **AC-03:** Instructor can add modules and nested lessons to a draft course (course → modules → lessons hierarchy). Detail: specs/course-authoring_spec.md
- **AC-04:** Admin can publish (DRAFT → PUBLISHED) or unpublish (PUBLISHED → UNPUBLISHED) a course; learners can only enroll in PUBLISHED courses. Detail: specs/catalog_spec.md
- **AC-05:** Quiz supports MCQ (single correct) and TRUE / FALSE question types; quizzes are auto-graded by a deterministic rule. Detail: specs/quiz-engine_spec.md
- **AC-06:** Learner can attempt a quiz multiple times; best score is recorded; each attempt is timestamped and append-only. Detail: specs/quiz-engine_spec.md
- **AC-07:** Learner can mark a lesson complete; course progress percentage is computed as completed_lessons / total_lessons. Detail: specs/progress-tracker_spec.md
- **AC-08:** Course lifecycle states DRAFT → PUBLISHED → UNPUBLISHED → ARCHIVED are enforced; invalid transitions raise InvalidCourseStateException. Detail: specs/catalog_spec.md
- **AC-09:** Instructor can view learner progress aggregated by course (count by progress band: 0–25%, 25–50%, 50–75%, 75–100%). Detail: specs/instructor-workbench_spec.md
- **AC-10:** Admin can manage course catalog, approve published courses, and monitor enrollment-level analytics. Detail: specs/admin-console_spec.md

## 6. Non-Functional Requirements

- **NFR-01:** Quiz scores are computed deterministically in integer percentage; calculations never use floating-point.
- **NFR-02:** Quiz attempts, lesson completions, and enrollment records are append-only.
- **NFR-03:** Learner PII (email, phone, performance data) is never written to logs in plaintext.
- **NFR-04:** Authentication boundary at controller layer; learner / instructor / admin roles are separated.
- **NFR-05:** Database migrations are append-only.
- **NFR-06:** Structured JSON logs with request correlation IDs.
- **NFR-07:** Health endpoint returns 200 within 1 second of a successful startup.
- **NFR-08:** Architecture rules enforced as tests — instructors cannot grade their own courses' learners; a learner cannot access another learner's progress; published courses cannot be mutated without an unpublish transition.

## 7. Invariants

These rules must never break. They come from the NFRs and the domain rules in the business case. They are the base for the harness constitution later.

- **INV-1:** A course changes state only through the allowed transitions in Section 4 (AC-08, DR-1).
- **INV-2:** A published course cannot be changed unless it goes through an unpublish transition (NFR-08).
- **INV-3:** A learner can enroll only in a PUBLISHED course (AC-01, AC-04, DR-3).
- **INV-4:** A learner has at most one enrollment per course (AC-01, DR-4).
- **INV-5:** Quiz scores are integer percentages (NFR-01, DR-6).
- **INV-6:** Quiz attempts, lesson completions, and enrollments are never edited or deleted (NFR-02, DR-9).
- **INV-7:** The best quiz score is kept, and each attempt keeps its timestamp (AC-06, DR-8).
- **INV-8:** Learner PII is never written to logs in plain text (NFR-03).
- **INV-9:** A learner cannot access another learner's progress. Instructors see only aggregated band counts (AC-09); admins see enrollment analytics (AC-10). (NFR-08, DR-11)
- **INV-10:** An instructor cannot grade their own courses' learners (NFR-08, DR-12).
- **INV-11:** Each role is checked at the controller layer (NFR-04, DR-10).
- **INV-12:** Database migrations are append-only (NFR-05).

## 8. Project Rules

- **No-Hand-Coding Rule:** All production code, tests, and migrations are generated by Claude Code agents. Hand edits are limited to specs, CLAUDE.md, agent definitions, hooks, skills, and other substrate files.
- **Spec-Is-Truth Rule:** When a spec and the code disagree, the spec wins; update the spec on purpose, then regenerate the code.
- **PR-Only Merge Rule:** No direct commits to main; all changes go through agent-reviewed pull requests.
- **Synthetic-Data Rule:** Use only dummy data. No Virtusa confidential or customer-sensitive data.

## 9. Scope & Out of Scope

**In scope — user journeys:**
- Browse: search published courses by category and difficulty.
- Enroll: enroll in a course, one enrollment per learner and course pair.
- Learn: move through modules and lessons, and mark lessons complete.
- Assess: attempt module-end quizzes, with multiple attempts and the best score kept.
- Progress: view own progress percentage and quiz scores across enrolled courses.

**In scope — internal functions:**
- Instructor Workbench: author courses with modules, lessons, and quiz questions; view learner progress by course.
- Admin Console: manage the course catalog, publish and unpublish courses, monitor enrollment and engagement.
- Quiz Engine: auto-grade MCQ and TRUE/FALSE attempts deterministically; keep attempt history.
- Progress Tracker: compute and snapshot course progress for each learner.

**Out of scope (out of scope list):** real video streaming or CDN; real payments or paid courses; live virtual classes (WebRTC); real proctoring or anti-cheat; certificate generation and external verification; production deployment, secret management, and multi-region setup.

## 10. Seed Data

Seed data is synthetic only: fake names and @example.com emails. It supports the demo and the tests.

- **Admin:** a seeded admin account (Sprint 1).
- **Instructors:** 2 seeded instructor accounts (Sprint 1).
- **Learners:** 3 seeded learner accounts (Sprint 1), in addition to self-registration.
- **Courses:** at least one seeded course in each lifecycle state: DRAFT, PUBLISHED, UNPUBLISHED, ARCHIVED (Sprint 1).
- **Modules and lessons:** seeded under the seeded courses (Sprint 2).
- **Sample quiz:** one seeded sample quiz with an MCQ question and a TRUE / FALSE question (Sprint 3).

## 11. Run

The application starts locally with one command, and loads the seed data. The command is defined in the design. The README quick-start is generated with the app.

## 12. Technology & Layers

- **Backend:** Python 3.12 with FastAPI. Code lives at the repository root in src/, tests/, and migrations/.
- **Frontend:** React with Vite and TypeScript, styled with Tailwind. Code lives in frontend/.
- **Database:** SQLite, accessed through SQLAlchemy, with schema changes made through Alembic migrations.
- **End-to-end tests:** Playwright, using the Playwright MCP server. Code lives in e2e/.
- **Layers:** controllers → services → repositories → domain. Configuration and logging live in core.
- **CI:** GitHub Actions with Claude Code Action (allowed by the capstone doc's Technology Stack section). A GitLab CI variant may be added later.
- **Architecture rules:** import-linter, with tests in tests/architecture/.

## 13. Sprint Plan

| Sprint | ACs | Main features |
|---|---|---|
| S1 | AC-01, AC-02, AC-04, AC-08 | Learner registration and login; course creation in DRAFT; publish and unpublish; lifecycle rules; browse and search; enrollment; seed data; architecture rules (import-linter, tests/architecture/), /health, JSON logs with correlation id |
| S2 | AC-03, AC-07, AC-10 | Modules and lessons; lesson completion; course progress; admin console |
| S3 | AC-05, AC-06, AC-09 | Quiz engine with auto-grading and attempts; instructor workbench |

## 14. Feature Specs Index

| File | ACs covered |
|---|---|
| specs/course-authoring_spec.md | AC-02, AC-03 |
| specs/catalog_spec.md | AC-04, AC-08, Browse (user journey, no AC id) |
| specs/enrollment_spec.md | AC-01 (incl. registration) |
| specs/progress-tracker_spec.md | AC-07, Progress view (no AC id) |
| specs/quiz-engine_spec.md | AC-05, AC-06 (incl. quiz question authoring) |
| specs/instructor-workbench_spec.md | AC-09 |
| specs/admin-console_spec.md | AC-10 |

## 15. Technical Acceptance

- **NFR-07:** Given the app has started, When GET /health is called, Then it returns 200 within 1 second.
- **NFR-06:** Given any API request, When it is logged, Then the log line is JSON and contains a correlation id, and every line for that request carries the same id.
- **NFR-05:** Given an existing migration, When a schema change is needed, Then a new migration is added and existing migration files are never edited.
- **Architecture — controllers:** Given the codebase, When the architecture tests run, Then controllers do not import repositories directly (import-linter and tests/architecture/).
- **Architecture — domain:** Given the codebase, When the architecture tests run, Then domain does not import services, repositories, controllers, or web or database frameworks.
- **Architecture — one-way flow:** Given the codebase, When the architecture tests run, Then imports flow one way only: controllers → services → repositories → domain.
- **NFR-08 tests:** Each NFR-08 rule is covered by a test: an instructor cannot grade their own course's learners; a learner cannot access another learner's progress; a published course cannot be changed without an unpublish transition.

## 16. Project Decisions

Decisions the project made where the capstone doc is silent.

- **Rounding:** percentages round down. Percent = completed × 100 // total (integer division, no float). Applies to course progress (AC-07) and quiz scores (AC-05). Examples: 1 of 3 → 33%.
- **Band boundaries (AC-09):** 0 ≤ p < 25, 25 ≤ p < 50, 50 ≤ p < 75, 75 ≤ p ≤ 100. A learner at 100% is in the top band.
