import pytest


@pytest.fixture
def input_value():
    input = 3
    return input


def test_multiply_with_11(input_value):
    assert input_value * 11 == 33


def test_multiply_with_10(input_value):
    assert input_value * 8 == 24
