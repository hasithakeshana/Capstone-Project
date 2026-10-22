# LearnLab — Business Case

## Problem

An online learning platform wants to launch a lightweight learning management system. It needs a course catalog, lesson delivery, enrollments, progress tracking, and quizzes. Video streaming and payments are not part of this project, so they are stubbed.

The project has one hard constraint: every line of production code is written by Claude Code agents under human supervision. Nobody writes the product code by hand. This means the specifications, business rules, and acceptance criteria must be clear and testable enough for agents to build the product and for reviewers to check it.

## Target Users

| Role | Who they are | Main needs | Key journeys |
|---|---|---|---|
| Learner | Role that registers and enrolls in published courses (AC-01) | Find published courses, enroll once, work through lessons, take quizzes, see own progress | Browse, Enroll, Learn, Assess, Progress (user journeys) |
| Instructor | Role that authors courses (AC-02, AC-03) | Build draft courses with modules, lessons, and quiz questions; see learner progress per course | Instructor Workbench (internal function) |
| Admin | Role that manages the catalog and publication (AC-04, AC-10) | Publish and unpublish courses, approve published courses, watch enrollment and engagement | Admin Console (internal function) |

## Success Metrics

*Derived from the capstone doc requirements. Each metric is taken from a statement in the capstone doc. No new numbers are added.*

1. Learners can enroll only in PUBLISHED courses, and a second enrollment in the same course
   is always rejected — yes/no — [AC-01, AC-04]
2. Learners can see their own progress percentage and quiz scores across enrolled courses,
   and never another learner's progress — yes/no — [AC-07, NFR-08]
3. Every quiz attempt is kept (append-only, timestamped) and the best score is retained;
   scores are whole percentages with no floating-point calculation — yes/no — [AC-06, NFR-01, NFR-02]
4. Instructors can see learner progress per course in the four bands
   (0–25%, 25–50%, 50–75%, 75–100%) — yes/no — [AC-09]
5. Admins can manage the catalog, approve published courses and monitor enrollment
   analytics — yes/no — [AC-10]
6. Every acceptance criterion has at least one test that names its AC id — 10 of 10 ACs — [AC-01 to AC-10]
7. The platform runs locally with a single command and seed data, and the health endpoint
   returns 200 within 1 second of startup — yes/no — [NFR-07]

## Domain Rules

- **DR-1:** Every course starts in DRAFT and moves only DRAFT → PUBLISHED → UNPUBLISHED → ARCHIVED; any other move is invalid and raises InvalidCourseStateException. [AC-02, AC-08]
- **DR-2:** Modules and lessons can be added only to a DRAFT course. [AC-03]
- **DR-3:** A learner can enroll only in a PUBLISHED course. [AC-01, AC-04]
- **DR-4:** A learner can have only one enrollment per course. [AC-01]
- **DR-5:** Course progress is completed lessons divided by total lessons. [AC-07]
- **DR-6:** Quiz scores are integer percentages, with no floating-point math. [NFR-01]
- **DR-7:** Quiz grading is deterministic: MCQ questions have one correct answer, and TRUE/FALSE questions are supported. [AC-05]
- **DR-8:** A learner can attempt a quiz many times; each attempt is timestamped and the best score is kept. [AC-06]
- **DR-9:** Quiz attempts, lesson completions, and enrollments are append-only records. [NFR-02]
- **DR-10:** Learner, instructor, and admin roles are separated, and the boundary is enforced at the controller layer. [NFR-04]
- **DR-11:** A learner cannot access another learner's progress. Instructors see only aggregated band counts (AC-09); admins see enrollment analytics (AC-10). [NFR-08]
- **DR-12:** Instructors cannot grade their own courses' learners. [NFR-08]
- **DR-13:** Learner personal data is never written to logs in plain text. [NFR-03]

*NFR-05 (append-only migrations) and NFR-06 (structured JSON logs) are technical rules defined in specs/app_spec.md → Non-Functional Requirements.*

## Value Proposition

- **Learners:** one place to browse published courses by category and difficulty, enroll once, and work through lessons and quizzes.
- **Learners:** see their own progress percentage and quiz scores across enrolled courses.
- **Instructors:** build courses in DRAFT, with modules, lessons, and quiz questions, before they are published.
- **Instructors:** see learner progress by course, grouped into progress bands.
- **Admins:** decide which courses learners can see by publishing and unpublishing them, and monitor enrollment analytics.
- **Platform:** course progress is computed and snapshotted for each learner; quiz scores are repeatable and attempt history is kept, because grading is deterministic and records are append-only.

## Out of Scope

- Real video streaming or CDN integration
- Real payment gateway or paid courses
- Live virtual classes (WebRTC)
- Real proctoring or anti-cheat technology
- Certification generation and external verification
- Production deployment, secret management, and multi-region setup
