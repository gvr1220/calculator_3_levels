from typing import Callable
from history_tracker import HistoryTracker

class Calculator:

    @staticmethod
    def _calculate(a: float, b: float, operation: str, result: float) -> float:
        HistoryTracker.add_history(a, b, operation, result)
        return result

    @staticmethod
    def add(a: float, b: float) -> float:
        return Calculator._calculate(a, b, "add", a + b)

    @staticmethod
    def subtract(a: float, b: float) -> float:
        return Calculator._calculate(a, b, "subtract", a - b)

    @staticmethod
    def multiply(a: float, b: float) -> float:
        return Calculator._calculate(a, b, "multiply", a * b)

    @staticmethod
    def divide(a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return Calculator._calculate(a, b, "divide", a / b)
