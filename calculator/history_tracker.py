from typing import List

class HistoryTracker:
    _history: List[str] = []

    @classmethod
    def add_history(cls, a: float, b: float, operation: str, result: float):
        cls._history.append(f"{a} {operation} {b} = {result}")

    @classmethod
    def get_history(cls) -> List[str]:
        return cls._history

    @classmethod
    def clear_history(cls):
        cls._history = []
