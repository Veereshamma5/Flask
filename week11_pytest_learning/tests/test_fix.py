import pytest


# fixture text method

@pytest.fixture()
def setup():
    print("Precondition statement")

    # postcondition statement

    yield

    print("Postcondition")


# actual test method

def test_fixture(setup):
    print("Actual test scenario")

# A test fixture is an environment
# used to consistently test some item, device or piece of software
