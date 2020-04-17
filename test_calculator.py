import pytest
from calculator import Calculator, CalculatorError

def test_add():
    calculator = Calculator()
    result = calculator.add(2, 3)
    assert result == 5

def test_add_raise():
    calculator = Calculator()
    with pytest.raises(CalculatorError) as context:
        result = calculator.add("abc", "d")
    # (str(context.value))

def test_subtract():
    calculator = Calculator()
    result = calculator.subtract(2, 3)
    assert result == -1

def test_multiply():
    calculator = Calculator()
    result = calculator.multiply(2, 3)
    assert result == 6
    
def test_divide():
    calculator = Calculator()
    result = calculator.divide(9, 3)
    assert result == 3

def test_divide_by_zero():
    calculator = Calculator()
    with pytest.raises(CalculatorError) as context:
        result = calculator.divide(9, 0)
    