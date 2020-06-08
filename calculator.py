import numbers
import sys
import json


class CalculatorError(Exception):
    """ Raise Exceptions """


class Calculator:
    """ Calculator Methods """

    def add(self, a, b):
        self._check_operand(a)
        self._check_operand(b)
        return a + b

    def subtract(self, a, b):
        self._check_operand(a)
        self._check_operand(b)
        return a - b

    def multiply(self, a, b):
        self._check_operand(a)
        self._check_operand(b)
        return a * b

    def divide(self, a, b):
        self._check_operand(a)
        self._check_operand(b)
        try:
            return a / b
        except ZeroDivisionError:
            raise CalculatorError("Cant divide by zero.")

    def _check_operand(self, operand):
        if not isinstance(operand, numbers.Number):
            raise CalculatorError(f'"{operand}" is not a number')

    def read_json(self, some_file_path):
        with open(some_file_path, "r") as f:
            return json.load(f)


if __name__ == "__main__":
    print("Lets calculate")
    calculator = Calculator()
    operations = [
        calculator.add,
        calculator.subtract,
        calculator.multiply,
        calculator.divide,
    ]
    while True:
        for i, operation in enumerate(operations, start=1):
            print(f"{i}: {operation.__name__}")
        print(f"q: Quit ")

        operand = input("pick a operation: ")
        if operand == "q":
            sys.exit()
        op = int(operand)
        a = float(input("what is a? "))
        b = float(input("what is b? "))

        try:
            res = operations[op - 1](a, b)
            print(f" {a} {operations[op-1].__name__} {b} = {res}")
        except CalculatorError as ex:
            print(ex)
