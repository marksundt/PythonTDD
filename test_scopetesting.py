import pytest

@pytest.fixture(scope="session", autouse=True)
def setupSession():
    print("\nSetup Session")

@pytest.fixture(scope="module", autouse=True)
def setupModule():
    print("\nSetup Module")

@pytest.fixture(scope="function", autouse=True)
def setupFunction():
    print("\nSetup Function")

@pytest.fixture(scope="class", autouse=True)
def setupFunction():
    print("\nSetup Class")

def test1():
    print("Executing test1")
    assert True

def test2():
    print("Executing test2")
    assert True