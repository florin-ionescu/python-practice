"""
pytest

What it does:
- Testing framework for Python.
- Used to write and run automated tests.
- Very important for QA Automation and Python development.
"""


def add_num(a, b):
    return a + b

def is_even(number):
    return number %  2 == 0

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")

    return a / b


# Basic test
def test_add_numbers():
    result = add_num(2, 3)
    assert result == 5

def test_is_even():
    assert is_even(4) is True
    assert is_even(5) is False

# Test exception
def test_divide_by_zero():
    import pytest
    with pytest.raises(ValueError):
        divide(10,0)

# Parametrized test
import pytest

@pytest.mark.parametrize(
    "a,b, expected",
    [
        (2,3,5),
        (10,5,15),
        (3, 6, 9)
    ]
)

def test_add_numbers_parametrized(a,b,expected):
    assert add_num(a,b) == expected