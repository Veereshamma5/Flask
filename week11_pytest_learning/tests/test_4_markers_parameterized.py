import sys

import pytest

from week11_pytest_learning.myapp import add


@pytest.mark.skip
def test_add_num():
    assert add(4, 5) == 9


@pytest.mark.skip(reason="Just wanna to skip")
def test_add_string():
    assert add("veer", "k") == "veerk"


@pytest.mark.skipif(sys.version_info > (3, 8), reason="Skip if the python version is less than 3.8")
def test_add_string_if_version_greater():
    assert add("veer", "k") == "veerk"


@pytest.mark.xfail
def test_add_decimal():
    assert add(10.5, 11.5) == 23.0


@pytest.mark.skip
class TestSample:
    def test_add_num(self):
        assert add(1, 2) == 3

    def test_add_str(self):
        assert add("a", "b") == "ab"


# Example for xpass

@pytest.mark.xfail
def test_v_xpass():
    assert 1 == 1


# Example for xfail, report won't display in the report


@pytest.mark.xfail
def test_xfail():
    assert 1 == 3


@pytest.mark.xfail(sys.platform == "win32", reason="don't run on windows 32")
def test_add_list_xfail():
    assert add([1], [2]) == [1, 2]
    raise Exception


@pytest.mark.parametrize("a, b, c", [(1, 2, 3), ("a", "b", "ab"), ([1], [2], [1, 2])], ids=["num", "str", "list"])
def test_verify_parameterized(a, b, c):
    assert add(a, b) == c


# Unit test will throw an exception,
# if the xfail condition is not fulfilled then xfail will fail, and it will show in the report

"""
Skip: Are not executed at all
xfail: Expected to fail, it will run the test while running but won't show as fail in the report
xpass: When a test passes despite being expected to fail (marked with pytest. mark. xfail ), it's an xpass and will be reported in the test summary
"""
