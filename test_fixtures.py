import pytest

@pytest.fixture()
def setup():
    print("\nSetup1")
    #Tear down 
    yield
    print("\nTeardown 1")

@pytest.fixture(autouse=True)
def setup2():
    print("\nSetup2")

# uses the setup fixture to run prior to the method
def test1(setup):
    print("Executing test1")
    assert True

@pytest.mark.usefixtures("setup")
def test2():
    print("Executing test2")
    assert True
