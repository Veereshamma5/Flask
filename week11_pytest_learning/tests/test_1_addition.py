from week11_pytest_learning.myapp.code1_addition import add


def test_add_num():
    assert add(4, 5) == 9


def test_add_string():
    assert add("veer", "k") == "veerk"


class TestSample:
    def test_add_num(self):
        assert add(1,2) == 3

    def test_add_str(self):
        assert add("a", "b")== "ab"
