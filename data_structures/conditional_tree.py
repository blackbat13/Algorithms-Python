from enum import Enum


class Operator(Enum):
    LESS = 0
    GREATER = 1
    LESSEQUAL = 2
    GREATEREQUAL = 3
    AND = 4
    OR = 5
    EQUAL = 6
    

class ConditionalTree:
    def __init__(self, left, operator: Operator, right):
        self._operator = operator
        self._left = left
        self._right = right
        
    def evaluate(self, values: dict) -> bool:
        left_value = self._value(self._left, values)
        right_value = self._value(self._right, values)
        if self._operator == Operator.LESS:
            return left_value < right_value
        if self._operator == Operator.GREATER:
            return left_value > right_value
        if self._operator == Operator.LESSEQUAL:
            return left_value <= right_value
        if self._operator == Operator.GREATEREQUAL:
            return left_value >= right_value
        if self._operator == Operator.AND:
            return left_value and right_value
        if self._operator == Operator.OR:
            return left_value or right_value
        
    @staticmethod
    def _value(var, values: dict):
        if type(var) is str:
            return values[var]
        elif type(var) is ConditionalTree:
            return var.evaluate(values)
        
        return var


if __name__ == "__main__":
    cond1 = ConditionalTree("x", Operator.LESS, 10)
    cond2 = ConditionalTree("y", Operator.LESS, 5)
    cond3 = ConditionalTree(cond1, Operator.AND, cond2)
    
    print(cond3.evaluate({"x": 3, "y": 2}))
    print(cond3.evaluate({"x": 13, "y": 2}))
    print(cond3.evaluate({"x": 3, "y": 22}))    