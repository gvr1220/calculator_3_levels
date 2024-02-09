'''Test Calculator'''
from calculator import add, subtract, multiply, divide

def test_addition():
    '''Test for addition function'''
    assert add(7,3) == 10

def test_subtraction():
    '''Test for subtraction function'''
    assert subtract(4,2) == 2

def test_multiplication():
    '''Test for multiplication function'''
    assert multiply(3,3) == 9

def test_division():
    ''''Test for division function'''
    assert divide(12,3) == 4
