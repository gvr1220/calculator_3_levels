"""
Tests for the calculation module.
"""

from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

@pytest.mark.parametrize(
    "operand_a, operand_b, operation, expected",
    [
        (Decimal('10'), Decimal('5'), add, Decimal('15')),
        (Decimal('10'), Decimal('5'), subtract, Decimal('5')),
        (Decimal('10'), Decimal('5'), multiply, Decimal('50')),
        (Decimal('10'), Decimal('2'), divide, Decimal('5')),
        (Decimal('10.5'), Decimal('0.5'), add, Decimal('11.0')),
        (Decimal('10.5'), Decimal('0.5'), subtract, Decimal('10.0')),
        (Decimal('10.5'), Decimal('2'), multiply, Decimal('21.0')),
        (Decimal('10'), Decimal('0.5'), divide, Decimal('20')),
    ]
)
def test_calculation_operations(operand_a, operand_b, operation, expected):
    """
    Test arithmetic operations on decimal numbers.
    """
    calc = Calculation(operand_a, operand_b, operation)
    assert calc.perform() == expected, (
        f"Failed {operation.__name__} operation with {operand_a} and {operand_b}"
    )

def test_calculation_repr():
    """
    Test the Calculation class instance.
    """
    calc = Calculation(Decimal('10'), Decimal('5'), add)
    expected_repr = "Calculation(10, 5, add)"
    assert repr(calc) == expected_repr, (
        "The __repr__ method output does not match the expected string."
    )

def test_divide_by_zero():
    """
    Test division by zero.
    """
    calc = Calculation(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.perform()
