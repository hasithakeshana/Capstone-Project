# LearnLab — Requirements Traceability

Verification report. Gaps and their status are listed at the end.

Legend: ✅ present / covered · ⚠ partial, unexpected, or accepted deviation · ❌ missing or wrong

## Part A — Project structure

### A1 and A3. Files and folders (excluding .git)

| Path | Status | Note |
|---|---|---|
| README.md | ⚠ | Unexpected. Kept; replaced by the harness-generated README in sprint 1. |
| docs/business-case.md | ✅ | |
| docs/architecture.md | ✅ | v1 |
| docs/tdd.md | ✅ | v1 |
| docs/reference/AI Native Engineer Capstone - BC-011 LearnLab.pdf | ⚠ | Kept in the repo by the owner's decision. The repo holds a .md copy, not the local-only PDF, and it is tracked by git. |
| specs/app_spec.md | ✅ | |
| specs/course-authoring_spec.md | ✅ | |
| specs/catalog_spec.md | ✅ | |
| specs/enrollment_spec.md | ✅ | |
| specs/progress-tracker_spec.md | ✅ | |
| specs/instructor-workbench_spec.md | ✅ | |
| specs/quiz-engine_spec.md | ✅ | |
| specs/admin-console_spec.md | ✅ | |
| specs/requirements-traceability.md | ✅ | This report. |
| specs/sprints/sprint-1_prd.md | ✅ | |
| specs/sprints/sprint-2_prd.md | ✅ | Draft. Status line present. |
| specs/sprints/sprint-3_prd.md | ✅ | Draft. Status line present. |
| CLAUDE.md, AGENTS.md, .gitignore, pyproject.toml, package.json, .claude/, src/, tests/, frontend/, e2e/ | ✅ | None present. |
| Empty or placeholder-only files | ✅ | None found. |
| Wrong names or folders | ✅ | None found. |

### A4. Required top headings

| Document | Headings present | Status |
|---|---|---|
| docs/business-case.md | Problem, Target Users, Success Metrics, Domain Rules, Value Proposition, Out of Scope | ✅ |
| docs/architecture.md | 1 Overview & Technology Stack, 2 Layered Structure, 3 System Context, 4 Enrollment-to-Completion Flow, 5 Domain Rules, 6 Cross-Cutting Concerns, 7 Detailed Design | ✅ |
| docs/tdd.md | 1 Approach, 2 Commit Convention, 3 Test Naming, 4 Test Levels, 5 Coverage, 6 Worked Example: AC-05 | ✅ |
| specs/app_spec.md | 1 Purpose through 15 Technical Acceptance (all present) | ✅ |
| Each of the 7 feature specs | Purpose, Actors, User Stories, Acceptance Criteria, Business Rules, Applicable NFRs, Related User Journeys, Out of Scope, Open Questions | ✅ |
| sprint-1_prd.md | 1 Problem & Goal through 6 Acceptance / Done | ✅ |
| sprint-2_prd.md | 1 through 6 (with 3.1 and 3.2) | ✅ |
| sprint-3_prd.md | 1 through 6 (with 3.1 and 3.2) | ✅ |

## Part B — Requirements traceability

### B1. Functional acceptance criteria (capstone Section 5.1)

| Brief item | Short description | Covered in | Sprint | Status |
|---|---|---|---|---|
| AC-01 | Register and enroll once in a PUBLISHED course | enrollment_spec.md → AC-01; app_spec.md §5 | S1 | ✅ |
| AC-02 | Create a course with its fields; starts in DRAFT | course-authoring_spec.md → AC-02 | S1 | ✅ |
| AC-03 | Add modules and nested lessons to a draft course | course-authoring_spec.md → AC-03 | S2 | ✅ |
| AC-04 | Publish or unpublish a course; learners enroll only in PUBLISHED | catalog_spec.md → AC-04 | S1 | ✅ |
| AC-05 | MCQ and TRUE / FALSE; deterministic auto-grading | quiz-engine_spec.md → AC-05 | S3 | ✅ |
| AC-06 | Multiple attempts; best score; timestamped, append-only | quiz-engine_spec.md → AC-06 | S3 | ✅ |
| AC-07 | Mark lesson complete; progress = completed / total | progress-tracker_spec.md → AC-07 | S2 | ✅ |
| AC-08 | Lifecycle enforced; invalid transitions raise exception | catalog_spec.md → AC-08 | S1 | ✅ |
| AC-09 | Instructor sees learner progress in four bands | instructor-workbench_spec.md → AC-09 | S3 | ✅ |
| AC-10 | Admin manages catalog, approves courses, monitors analytics | admin-console_spec.md → AC-10 | S2 | ✅ |

### B2. Non-functional requirements (capstone Section 5.2)

| Brief item | Short description | Covered in | Sprint | Status |
|---|---|---|---|---|
| NFR-01 | Integer percentage quiz scores, no floating point | app_spec.md §6; quiz-engine_spec.md | S3 (NFR-19) | ✅ |
| NFR-02 | Attempts, completions, enrollments append-only | app_spec.md §6; PRDs | S1 (NFR-2), S2 (NFR-16), S3 (NFR-20) | ✅ |
| NFR-03 | No learner PII in plain-text logs | app_spec.md §6; enrollment_spec.md | S1 (NFR-3), S2 (NFR-17) | ✅ |
| NFR-04 | Authentication at controller layer; roles separated | app_spec.md §6; architecture.md §6 | S1 (NFR-1) | ✅ |
| NFR-05 | Migrations append-only | app_spec.md §6; architecture.md §6 | S1 (NFR-4) | ✅ |
| NFR-06 | Structured JSON logs with correlation IDs | app_spec.md §6; architecture.md §6 | S1 (NFR-5) | ✅ |
| NFR-07 | /health returns 200 within 1 s | app_spec.md §6 and §15; architecture.md §6 | S1 (NFR-6) | ✅ |
| NFR-08 | Architecture rules enforced as tests (grading, progress access, published immutability) | app_spec.md §15; architecture.md §2; tdd.md §4; the PRD lines NFR-7 (S1), NFR-18 (S2), NFR-21 (S3) each name an architecture test in tests/architecture/ | S1 (NFR-7); S2 (NFR-18); S3 (NFR-21) | ✅ |

### B3. User journeys (capstone Section 6.1)

| Brief item | Short description | Covered in | Sprint | Status |
|---|---|---|---|---|
| Browse | Search published courses by category and difficulty | catalog_spec.md → Browse; app_spec.md §9 | S1 (FR-23 to FR-26) | ✅ |
| Enroll | Enroll once per learner-course pair | enrollment_spec.md; app_spec.md §9 | S1 (FR-15 to FR-18) | ✅ |
| Learn | Move through lessons sequentially; mark complete | progress-tracker_spec.md; app_spec.md §9 | S2 (FR-36, FR-46, FR-50) | ✅ |
| Assess | Module-end quizzes; multiple attempts; best kept | quiz-engine_spec.md; app_spec.md §9 | S3 (FR-53, FR-66, FR-67) | ✅ |
| Progress | Own progress % and quiz scores | progress-tracker_spec.md; app_spec.md §9 | S2 (FR-47, FR-51); S3 (FR-71, FR-79) | ✅ |

### B4. Internal functions (capstone Section 6.2)

| Brief item | Short description | Covered in | Sprint | Status |
|---|---|---|---|---|
| Instructor Workbench | Author courses; view progress by course | instructor-workbench_spec.md; course-authoring_spec.md | S2 (FR-32, FR-33, FR-49); S3 (FR-72 to FR-75, FR-80) | ✅ |
| Admin Console | Manage catalog; publish or unpublish; monitor analytics | admin-console_spec.md; catalog_spec.md | S1 (FR-6 to FR-12); S2 (FR-39 to FR-45, FR-52) | ✅ |
| Quiz Engine | Auto-grade; persist attempt history | quiz-engine_spec.md | S3 (FR-60 to FR-63, FR-66 to FR-69) | ✅ |
| Progress Tracker | Compute and snapshot progress | progress-tracker_spec.md | S2 (FR-37, FR-41, FR-48) | ✅ |

### B5. Out of scope (capstone Section 6.3)

| Brief item | Short description | Covered in | Status |
|---|---|---|---|
| Video | Real video streaming or CDN | app_spec.md §9; business-case.md; all three PRDs | ✅ |
| Payments | Real payment gateway or paid courses | app_spec.md §9; business-case.md; all three PRDs | ✅ |
| Live classes | Live virtual classes (WebRTC) | app_spec.md §9; business-case.md; all three PRDs | ✅ |
| Proctoring | Real proctoring or anti-cheat | app_spec.md §9; business-case.md; all three PRDs | ✅ |
| Certificates | Certificate generation and verification | app_spec.md §9; business-case.md; all three PRDs | ✅ |
| Deployment | Production deployment, secret management, multi-region | app_spec.md §9; business-case.md; all three PRDs | ✅ |

No out-of-scope item appears as in scope in any document.

### B6. Applicable rules (capstone Section 3.4)

| Brief item | Short description | Covered in | Status |
|---|---|---|---|
| No-Hand-Coding Rule | Production code generated by agents | app_spec.md §8 | ✅ |
| Spec-Is-Truth Rule | Spec wins over code | app_spec.md §8 | ✅ |
| PR-Only Merge Rule | No direct commits to main | app_spec.md §8 | ✅ |
| Synthetic-Data Rule | Dummy data only | app_spec.md §8; sprint PRDs (NFR-15) | ✅ |

### B7. Sprint assignment (capstone Section 8.2-14)

| Brief item | Short description | Covered in | Status |
|---|---|---|---|
| AC-01 | New in S1; carried in S2 and S3 | sprint-1_prd.md; sprint-2_prd.md; sprint-3_prd.md | ✅ |
| AC-02 | New in S1; carried in S2 and S3 | same | ✅ |
| AC-03 | New in S2; carried in S3 | same | ✅ |
| AC-04 | New in S1; carried in S2 and S3 | same | ✅ |
| AC-05 | New in S3 | sprint-3_prd.md | ✅ |
| AC-06 | New in S3 | sprint-3_prd.md | ✅ |
| AC-07 | New in S2; carried in S3 | sprint-2_prd.md; sprint-3_prd.md | ✅ |
| AC-08 | New in S1; carried in S2 and S3 | same | ✅ |
| AC-09 | New in S3 | sprint-3_prd.md | ✅ |
| AC-10 | New in S2; carried in S3. Agreed plan (app_spec §13). | sprint-2_prd.md; sprint-3_prd.md; app_spec.md §13 | ✅ |
| Sprint names | S1 "Catalog & Enrollment" and S3 "Quiz Engine & Instructor Workbench" match capstone Section 8.2-14. S2 "Lessons, Progress & Admin Console" is accepted: S2 still covers lessons and progress. | sprint PRD titles | ✅ |

## Part C — Marking compliance

| Requirement | Where satisfied | Status | Fix |
|---|---|---|---|
| C1. Section 7.1: app_spec.md and a <feature>_spec.md per feature, each with an "Acceptance Criteria" section | app_spec.md §5; all seven feature specs have an "Acceptance Criteria" heading | ✅ | None |
| C2. Section 8.1 item 3: specs for course-authoring, catalog, enrollment, quiz-engine, progress-tracker, instructor-workbench (plus admin-console) | Seven feature specs, plus app_spec.md §14 index | ✅ | None |
| C3. Section 7.2 and 8.1 item 2: business case with problem, users, metrics, rules, value proposition, in own words | docs/business-case.md (all headings present; Out of Scope reworded in own words) | ✅ | Fixed |
| C4. Section 7.2: testable acceptance (Given-When-Then or AC-NN) for at least 4 specs | Seven feature specs have both the AC-NN ids and Given-When-Then bullets | ✅ | None |
| C5. Section 7.2: at least 4 rule files under src/domain/, planned and named | docs/architecture.md §5 names five planned rules | ✅ | None |
| C6. Section 7.2: frontend with at least one responsive layout | architecture.md §1; sprint-1_prd.md NFR-11 | ✅ | None |
| C7. Section 7.4: architecture diagram and layered structure | architecture.md §2 (layer table) and §3 (Mermaid diagram) | ✅ | None |
| C8. Section 8.2-11: C4 context or enrollment-to-completion sequence diagram; tdd.md with red–green–refactor and an AC-05 example | architecture.md §3 and §4; tdd.md §1 and §6 | ✅ | None |
| C9. Section 7.3: TDD document at docs/tdd.md | docs/tdd.md | ✅ | None |
| C10. Section 5.1 note: each AC has a test referencing its AC-NN id | tdd.md §3 (naming rule) | ✅ | None |
| C11. Section 8.1 item 1: seed data and single-command run | app_spec.md §10 (seed) and §11 (run) | ✅ | None |
| C12. Section 3.4: the four applicable rules | app_spec.md §8 | ✅ | None |

## Summary

| Part | ✅ | ⚠ | ❌ |
|---|---|---|---|
| A — Project structure (rows) | 18 | 2 | 0 |
| A4 — Headings (documents checked) | 14 | 0 | 0 |
| B — Traceability (rows) | 48 | 0 | 0 |
| C — Marking compliance (rows) | 12 | 0 | 0 |

## Gaps and status

1. **Capstone file (⚠, accepted).** The capstone is kept in the repo by the owner's decision. It is a .md copy, not the local-only PDF, and it is tracked by git.
2. **README.md (⚠, accepted).** Kept; replaced by the harness-generated README in sprint 1.
3. **AC-10 sprint (✅, accepted).** AC-10 in S2 is the agreed plan (app_spec §13).
4. **Sprint 2 title (✅, accepted).** S2 still covers lessons and progress, so the title difference is accepted.
5. **NFR-08 as tests (✅, fixed).** Each NFR-08 rule now names an architecture test in tests/architecture/: NFR-7 (S1, carried in S2 and S3), NFR-18 (S2, carried in S3), NFR-21 (S3).
6. **Business case wording (✅, fixed).** The six Out of Scope items are reworded in own words.
7. **Report file (resolved).** `specs/requirements-traceability.md` was missing before the first check. It has been created.
