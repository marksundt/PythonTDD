import pytest

@pytest.fixture()
def setup():
    print("\nSetup")

# uses the setup fixture to run prior to the method
def test1(setup):
    print("Executing test1")
    assert True


def test2():
    print("Executing test2")
    assert True
