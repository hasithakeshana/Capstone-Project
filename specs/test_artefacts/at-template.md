# Acceptance Test Template

Use this shape for every acceptance test. Write it in plain business language.

**Test name:** `test_acNN_<behaviour>` (for example `test_ac01_learner_cannot_enroll_twice`)
**Tag:** `@pytest.mark.ac("AC-NN")`
**Docstring:** starts with `AC-NN (E1-S1-ACn):`

## Example: AC-01

- **Given** Ada is a registered learner
  and the course "Intro to Python" is PUBLISHED
- **When** Ada enrolls in "Intro to Python" for the first time
  and then enrolls in it again
- **Then** the second request is rejected
  and Ada has exactly 1 enrollment for "Intro to Python"

## Rules

- Use concrete dummy data only (synthetic names, `@example.com` emails).
- One behaviour per test.
- Name the business outcome in Then, not the code path.

## Code example

```python
import pytest

# Names below are set in the sprint 1 design; keep this shape.
from services.enrollment_service import DuplicateEnrollmentError, enroll_learner


class FakeEnrollmentStore:  # in-memory adapter for the enrollment port
    def __init__(self) -> None:
        self.rows: list[tuple[str, str]] = []

    def save(self, learner_id: str, course_id: str) -> None:
        self.rows.append((learner_id, course_id))

    def count(self, learner_id: str, course_id: str) -> int:
        return self.rows.count((learner_id, course_id))


@pytest.mark.ac("AC-01")
def test_ac01_learner_cannot_enroll_twice() -> None:
    """AC-01 (E1-S1-ACn): a learner cannot enroll twice in the same course."""
    # GIVEN learner "learner-ada" and the PUBLISHED course "course-intro-python"
    store = FakeEnrollmentStore()
    enroll_learner("learner-ada", "course-intro-python", store=store)

    # WHEN she enrolls in the same course again
    with pytest.raises(DuplicateEnrollmentError):
        enroll_learner("learner-ada", "course-intro-python", store=store)

    # THEN exactly one enrollment exists
    assert store.count("learner-ada", "course-intro-python") == 1
```

Rules: assert a named domain error, never bare `Exception`; import from the service layer; use ids, not emails; one behaviour per test.
