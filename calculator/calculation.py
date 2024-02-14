class Calculation:
    def __init__(self, a: float, b: float, operation: callable):
        self.a = a
        self.b = b
        self.operation = operation

    def get_result(self) -> float:
        return self.operation(self.a, self.b)
