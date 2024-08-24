import pytest
import unittest

class Test_TestStuff(unittest.TestCase):
    def test_canAssertTrue():
        print("Hello world")
        assert True

if __name__ == '__main__':
    unittest.main()