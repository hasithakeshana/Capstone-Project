# Context

Domain glossary for LearnLab. Source: `specs/app_spec.md` and the feature specs in `specs/`. Add new terms with a `### Term` heading.

## Terms

### Learner
A user with the learner role. Registers, enrolls in PUBLISHED courses, completes lessons, and attempts quizzes. Sees only their own progress.

### Instructor
A user with the instructor role. Creates DRAFT courses, adds modules, lessons and quiz questions, and sees aggregated learner progress per course. Cannot grade their own courses' learners.

### Admin
A user with the admin role. Publishes and unpublishes courses, approves published courses, and views enrollment analytics. Only an admin can change a course's state.

### Course
A learning offer with a title, description, category, difficulty, owner (the instructor who created it) and a lifecycle state. Contains modules.

### Module
A part of one course. Belongs to exactly one course and contains lessons.

### Lesson
A unit of learning inside one module. A learner can mark it complete. Not the same as a module.

### Quiz
A set of questions. Module-end quizzes per the Assess journey. Doc silent on how a quiz attaches to a module (see `specs/quiz-engine_spec.md` Open Questions). Not the same as a quiz attempt.

### Question
A question in a quiz. Two types: MCQ (one correct answer) and TRUE/FALSE.

### Enrollment
The link between one learner and one course. One enrollment per learner and course. Different from a lesson completion.

### Lesson Completion
A record that a learner completed one lesson.

### Quiz Attempt
One timestamped try at a quiz by a learner, with its score. A learner can have many attempts. Not the same as the best score.

### Best Score
The highest score among a learner's attempts on one quiz. Kept when a new attempt is made.

### Progress %
Course progress for one learner: completed lessons divided by total lessons, as an integer percentage. Quiz scores are shown separately and are not part of Progress %.

### Progress Band
A bucket of Progress % used for instructor views: 0–25%, 25–50%, 50–75%, 75–100%.

### DRAFT
Course state. Every new course starts here. Modules and lessons can be added only in DRAFT.

### PUBLISHED
Course state. Learners can see and enroll in the course.

### UNPUBLISHED
Course state. Reached by unpublishing a PUBLISHED course. Learners cannot enroll. Effects on existing enrollments are an open question in `specs/catalog_spec.md`.

### ARCHIVED
Course state. Reached from UNPUBLISHED. No allowed transition leaves ARCHIVED.

### Approve
Admin action on a PUBLISHED course (AC-10). Doc silent on what approval means beyond this (see `specs/catalog_spec.md` Open Questions). Not a state.

## Invariants

- INV-1 (AC-08, DR-1): A course changes state only through DRAFT → PUBLISHED → UNPUBLISHED → ARCHIVED; any other move raises InvalidCourseStateException.
- INV-2 (NFR-08): A PUBLISHED course cannot be changed unless it goes through an unpublish transition.
- INV-3 (AC-01, AC-04, DR-3): A learner can enroll only in a PUBLISHED course.
- INV-4 (AC-01, DR-4): A learner has at most one enrollment per course.
- INV-5 (NFR-01, DR-6): Quiz scores are integer percentages; no floating-point math.
- INV-6 (NFR-02, DR-9): Quiz attempts, lesson completions, and enrollments are never edited or deleted.
- INV-7 (AC-06, DR-8): The best quiz score is kept, and each attempt keeps its timestamp.
- INV-8 (NFR-03): Learner PII is never written to logs in plain text.
- INV-9 (NFR-08, DR-11): A learner cannot access another learner's progress; instructors see only aggregated band counts (AC-09); admins see enrollment analytics (AC-10).
- INV-10 (NFR-08, DR-12): An instructor cannot grade their own courses' learners.
- INV-11 (NFR-04, DR-10): Each role is checked at the controller layer.
- INV-12 (NFR-05): Database migrations are append-only.

## Out of Scope Terms

- Payment, paid course: payments are stubbed; no paid courses.
- Certificate: certificate generation and external verification are out of scope.
- Live class, WebRTC: live virtual classes are out of scope.
- Video streaming, CDN: video delivery is stubbed.
- Proctoring, anti-cheat: quiz monitoring is out of scope.
- Production deployment, secret management, multi-region: out of scope for this project.
