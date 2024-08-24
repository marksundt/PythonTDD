import pytest

class TestClass:

    @classmethod 
    def setup_class(cls):
        print("Setup TestClass")

    @classmethod 
    def teardown_class(cls):
        print("Teardown TestClass!")

    def setup_method(self, function):
        if function == self.test1:
            print("\nSetting up test1 method!")
        elif function == self.test2:
            print("\nSetting up test2! method")
        else:
            print("\nSetting up unknown test!")

    def teardown_method(self, function):
        if function == self.test1:
            print("\nTearing down test1! method")
        elif function == self.test2:
            print("\nTearing down test2! method")
        else:
            print("\nTearing down unknow test!")

    def setup_function(function):
            if function == test1:
                print("\nSetting up test1!")
            elif function == test2:
                print("\nSetting up test2!")
            else:
                print("\nSetting up unknow test!")


    def teardown_function(function):
        if function == test1:
            print("\nTearing down test1!")
        elif function == test2:
            print("\nTearing down test2!")
        else:
            print("\nTearing down unknow test!")


    def test1(self):
        print("Executing test1!")
        assert True

    def test2(self):
        print("Executing test2!")
        assert True