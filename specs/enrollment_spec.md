# Enrollment — Feature Spec

## Purpose

Learners register themselves and enroll in a published course. A learner can enroll only once in the same course. This feature covers AC-01, including learner registration.

## Actors

- Learner (registers and enrolls)
- Instructor and Admin accounts are seeded, not self-registered (see app_spec.md → Seed Data). They do not enroll in courses.

## User Stories

- As a visitor, I want to register as a learner, so that I can enroll in courses.
- As a learner, I want to enroll in a published course, so that I can learn from it.
- As a learner, I want to know that I am already enrolled in a course, so that I do not enroll twice.

## Acceptance Criteria

### AC-01 Learner can register and enroll in any PUBLISHED course; a learner cannot enroll twice in the same course

- Given I am a visitor with no account, When I register as a learner, Then a learner account is created.
- Given I am a registered learner and a course in PUBLISHED state, When I enroll in the course, Then one enrollment linking me to the course is saved.
- Given I am a learner with an enrollment in a course, When I enroll in the same course again, Then the request is rejected and only one enrollment exists for that learner and course.
- Given I am a registered learner and a course in DRAFT state, When I enroll in it, Then the request is rejected and no enrollment is saved. (AC-04)
- Given I am a registered learner and a course in UNPUBLISHED state, When I enroll in it, Then the request is rejected and no enrollment is saved. (AC-04)
- Given I am not signed in, When I try to enroll in a course, Then the request is rejected and no enrollment is saved. (NFR-04)
- Given I am signed in as an instructor, When I try to enroll in a course, Then the request is rejected and no enrollment is saved. (NFR-04)
- Given a course in ARCHIVED state, When a learner enrolls in it, Then the request is rejected and no enrollment is saved. (AC-04, AC-08)
- Given I am signed in as an admin, When I try to enroll in a course, Then the request is rejected and no enrollment is saved. (NFR-04)
- Given a learner sends the same enrollment request twice (a retry), When both requests are processed, Then exactly one enrollment exists for that learner and course and the second request is rejected. (AC-01 — duplicate enrollment under retry)
- Given an enrollment exists, When anyone tries to edit or delete it, Then the change is rejected and the record is unchanged. (NFR-02)
- Given a visitor registers with an email, When the request is logged, Then the log does not contain the email in plain text. (NFR-03, DR-13)
- Given a registered user with a correct email and password, When they log in, Then they receive a token that carries their role. (AC-01, NFR-04)
- Given a wrong password, When they log in, Then the request is rejected and no token is returned. (AC-01, NFR-04)
- Given a request with no token or an invalid token, When it calls a protected endpoint, Then it is rejected. (AC-01, NFR-04)

## Business Rules

- Learners register themselves. Instructor and Admin accounts are not self-registered. (AC-01, app_spec.md → Seed Data)
- A learner can enroll only in a course in PUBLISHED state. (AC-01, AC-04, DR-3)
- A learner can have only one enrollment per course. (AC-01, DR-4)
- Enrollment records are append-only. (NFR-02, DR-9)
- Login returns a token that carries the user's role. This is a project decision, not stated in the capstone doc. (NFR-04, app_spec.md → Roles & Permissions)

## Applicable NFRs

- **NFR-02:** Enrollment records are only added, never edited or deleted.
- **NFR-03:** Learner personal data entered at registration (for example email) is never written to logs in plain text. (DR-13)
- **NFR-04:** Registration and enrollment requests are checked at the controller layer. Learner, instructor, and admin roles stay separate.

## Related User Journeys

- Enroll (user journey) — enroll in a course, one enrollment per learner and course pair.
- Browse (user journey) leads to Enroll. The browse rules are in the Catalog feature spec.

## Out of Scope

- Browsing and searching courses (Catalog feature)
- Lesson completion and course progress (Progress Tracker feature, AC-07)
- Paid enrollment or payments (out of scope list)
- Certificates tied to enrollment (out of scope list)

## Open Questions

None
