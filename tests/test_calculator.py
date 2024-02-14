"""My Calculator Test"""
from calculator import Calculator


def test_addition():
    """Test that addition function works """
    assert Calculator.add(2, 2) == 4


def test_subtraction():
    """Test that subtraction function works"""
    assert Calculator.subtract(6, 3) == 3


def test_multiplication():
    """Test that multiplication function"""
    assert Calculator.multiply(3, 4) == 12


def test_division():
    """Test that division function"""
    assert Calculator.divide(12, 3) == 4
