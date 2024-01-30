import pytest

from week11_pytest_learning.myapp.code3_age_raise_error import verify_age


def test_verify_age():
    with pytest.raises(ValueError, match="Age cannot be less than 0"):
        verify_age(-1)


def test_verify_age_with_assert():
    with pytest.raises(ValueError) as ex:
        verify_age(-1)
    assert str(ex.value) == 'Age cannot be less than 0'
