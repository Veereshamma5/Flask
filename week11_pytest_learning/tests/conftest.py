from datetime import datetime

import pytest

from week11_pytest_learning.tests.sample_fixtures_custom import Student


@pytest.fixture
def input_value():
   input = 3
   return input


@pytest.fixture
def dummy_student():
    return Student("nikhil", datetime(2000, 1, 1), "coe", 20)


@pytest.fixture
def make_dummy_student():
    def _make_dummy_student(name, credits):
        return Student(name, datetime(2000, 1, 1), "coe", credits)

    return _make_dummy_student