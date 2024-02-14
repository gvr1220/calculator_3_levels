class Calculation:
    def __init__(x,y, operation):
        self.x = x
        self.y = y
        self.operation = operation
    
    def get_results():
        return self.operation(self.x, self.y)