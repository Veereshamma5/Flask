from datetime import datetime

import pytest

from fixtures.sample_fixtures_custom import Student


@pytest.fixture
# Creating a custom fixture
def dummy_student(scope = "function"):
    student = Student("Shanvika", datetime(1995, 12, 2), "CSE")
    return student


def test_student_age_credits(dummy_student):
    dummy_student.add_credits(5)
    assert dummy_student.get_credits() == 5


def test_student_get_cred(dummy_student):
    assert dummy_student.get_credits() == 0

