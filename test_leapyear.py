import pytest

def leapyear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False

# Can Call LeapYear
def test_canAsswertTrue():
    leapyear(1)
    assert True

# Returns false for not divisible by 4
def test_returnFalseNotDivBy4():
    ret_val = leapyear(1995)
    assert ret_val == False
    
# Returns true for divisible by 4 but not 100 
def test_returnTrueDivisibileBy4Not100():
    ret_val = leapyear(1996)
    assert ret_val == True

# Returns false for divisible by 4 but is divisible by 100 but not 400, and divisible by 400    
def test_returnsFalseForDiv4ButIsDivBy100Not400():
    ret_val = leapyear(2100)
    assert ret_val == False

# Returns true for divisible by 4, divisible by 100, and divisible by 400
def test_returnsTrueForDiv4ButIsDivBy100Not400():
    ret_val = leapyear(2000)
    assert ret_val == True