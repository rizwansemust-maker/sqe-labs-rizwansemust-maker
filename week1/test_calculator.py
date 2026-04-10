import pytest

# The functions to test
def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Tests
def test_multiply_negative_numbers():
    assert multiply(-3, -4) == 12

def test_divide_even():
    assert divide(10, 2) == 5.0

def test_divide_float_result():
    assert divide(7, 2) == 3.5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)          # ← This MUST be indented (4 spaces)