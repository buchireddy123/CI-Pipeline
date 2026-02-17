# test_calculator.py

from calculator import add, sub

# Test addition function
def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0

# Test subtraction function
def test_sub():
    assert sub(5, 3) == 2
    assert sub(10, 5) == 5
    assert sub(0, 4) == -4
