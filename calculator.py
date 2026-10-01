"""Simple calculator module - TDD Example."""


def _check_numeric(*values):
    """Raise TypeError if any value is not an int or float."""
    for v in values:
        if not isinstance(v, (int, float)) or isinstance(v, bool):
            raise TypeError(f"Expected numeric type, got {type(v).__name__}")


def add(a, b):
    """Return the sum of two numbers."""
    _check_numeric(a, b)
    return a + b


def subtract(a, b):
    """Return the difference of two numbers."""
    _check_numeric(a, b)
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    _check_numeric(a, b)
    return a * b


def divide(a, b):
    """Return the quotient of two numbers."""
    _check_numeric(a, b)
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
