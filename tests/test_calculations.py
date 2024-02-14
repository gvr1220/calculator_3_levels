"""
Unit tests for the calculator application.
"""

from decimal import Decimal

from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract


def test_add_calculation():
    """
    Test adding a calculation to the history.
    """
    Calculations.clear_history()
    calc = Calculation(Decimal('2'), Decimal('2'), add)
    Calculations.add_calculation(calc)
    assert Calculations.get_latest() == calc, \
        "Failed to add the calculation to the history"


def test_get_history():
    """
    Test getting the history of calculations.
    """
    Calculations.clear_history()
    Calculations.add_calculation(Calculation(Decimal('10'), Decimal('5'), add))
    Calculations.add_calculation(Calculation(Decimal('20'), Decimal('3'), subtract))

    history = Calculations.get_history()
    assert len(history) == 2, "History does not contain the expected number of calculations"


def test_clear_history():
    """
    Test clearing the history of calculations.
    """
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0, "History was not cleared"


def test_get_latest():
    """
    Test getting the latest calculation.
    """
    Calculations.clear_history()
    Calculations.add_calculation(Calculation(Decimal('10'), Decimal('5'), add))
    Calculations.add_calculation(Calculation(Decimal('20'), Decimal('3'), subtract))

    latest = Calculations.get_latest()
    assert latest.a == Decimal('20') and latest.b == Decimal('3'), \
        "Did not get the correct latest calculation"


def test_find_by_operation():
    """
    Test finding calculations by operation.
    """
    Calculations.clear_history()
    Calculations.add_calculation(Calculation(Decimal('10'), Decimal('5'), add))
    Calculations.add_calculation(Calculation(Decimal('20'), Decimal('3'), subtract))

    add_operations = Calculations.find_by_operation("add")
    assert len(add_operations) == 1, \
        "Did not find the correct number of calculations with add operation"
    subtract_operations = Calculations.find_by_operation("subtract")
    assert len(subtract_operations) == 1, \
        "Did not find the correct number of calculations with subtract operation"


def test_get_latest_with_empty_history():
    """
    Test getting the latest calculation with an empty history.
    """
    Calculations.clear_history()
    assert Calculations.get_latest() is None, \
        "Expected None for latest calculation with empty history"
