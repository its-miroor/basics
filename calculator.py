"""Simple calculator module for learning TDD."""


def add(a, b):
    """Add two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The sum of a and b
        
    Raises:
        TypeError: If either argument is not a number
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a + b


def subtract(a, b):
    """Subtract b from a.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The difference (a - b)
        
    Raises:
        TypeError: If either argument is not a number
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a - b


def multiply(a, b):
    """Multiply two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The product (a * b)
        
    Raises:
        TypeError: If either argument is not a number
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a * b


def divide(a, b):
    """Divide a by b.
    
    Args:
        a: Dividend (numerator)
        b: Divisor (denominator)
        
    Returns:
        The quotient (a / b)
        
    Raises:
        TypeError: If either argument is not a number
        ZeroDivisionError: If b is zero
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
