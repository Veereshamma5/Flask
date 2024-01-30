# Grouping using mark

from tut1.myapp.mathfuncs import Algebra, Geometry
from week11_pytest_learning.myapp.code2_mathfunctions import Algebra, Geometry
import pytest


@pytest.mark.algebra
def test_square():
    assert Algebra.square(40) == 1600
    assert Algebra.square(5) == 25


@pytest.mark.algebra
def test_cube():
    assert Algebra.cube(40) == 64000
    assert Algebra.cube(5) == 125


@pytest.mark.geometry
def test_is_triangle():
    assert Geometry.is_triangle(120, 40, 20) == True
    assert Geometry.is_triangle(45, 67, 99) == False


@pytest.mark.geometry
def test_is_quadrilateral():
    assert Geometry.is_quadrilateral(350, 5, 5, 0) == True
    assert Geometry.is_quadrilateral(11, 22, 33, 44) == False

# Run only one class### $ pytest file_name -m marker_name


# Grouping using class


class Test_Algebra:  # making a class for testing the two tests belonging to the Algebra class
    def test_square(self):
        assert Algebra.square(40) == 1600
        assert Algebra.square(5) == 25

    def test_cube(self):
        assert Algebra.cube(40) == 64000
        assert Algebra.cube(5) == 125


class Test_Geometry:  # making a class for testing the two tests belonging to the Geometry class
    def test_is_triangle(self):
        assert Geometry.is_triangle(120, 40, 20) == True
        assert Geometry.is_triangle(45, 67, 99) == False

    def test_is_quadrilateral(self):
        assert Geometry.is_quadrilateral(350, 5, 5, 0) == True
        assert Geometry.is_quadrilateral(11, 22, 33, 44) == False

# Run only one class### pytest tut1/tests/test_mathfuncs_class.py::Test_Algebra -v

# Group in a separate file


class Test_Algebra:
    def test_square(self):
        assert Algebra.square(40) == 1600
        assert Algebra.square(5) == 25

    def test_cube(self):
        assert Algebra.cube(40) == 64000
        assert Algebra.cube(5) == 125

