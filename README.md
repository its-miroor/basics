# Basics - Test-Driven Development in Python

Learning Test-Driven Development (TDD) with Python and pytest.

## The TDD Cycle: Red-Green-Refactor

1. **Red** 🔴 - Write a failing test
2. **Green** 🟢 - Write minimal code to pass the test
3. **Refactor** 🔵 - Improve the code while keeping tests passing

## Project Structure

```
basics/
├── calculator.py          # Module with functions to test
├── test_calculator.py     # Test suite
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Getting Started

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Tests

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run a specific test file
pytest test_calculator.py

# Run a specific test class
pytest test_calculator.py::TestAdd

# Run a specific test
pytest test_calculator.py::TestAdd::test_add_positive_numbers
```

### 3. Watch Mode (Auto-run tests on file changes)

```bash
pytest-watch
# or
pytest --looponfail
```

## Example: The `add()` Function

### RED 🔴 - Write the Test First

```python
def test_add_with_invalid_input():
    with pytest.raises(TypeError):
        add("2", 3)
    with pytest.raises(TypeError):
        add(None, 5)
```

### GREEN 🟢 - Write Minimal Code to Pass

```python
def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a + b
```

### REFACTOR 🔵 - Improve While Keeping Tests Green

```python
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
```

## Key TDD Principles

✅ Write tests **before** writing code  
✅ Write the **minimum code** to pass tests  
✅ Keep tests **simple and focused**  
✅ Test **edge cases** and error conditions  
✅ Refactor with **confidence** - tests catch regressions  

## Next Steps

1. Add more functions to `calculator.py` (subtract, multiply, divide)
2. Write tests for each function following TDD
3. Explore pytest features (fixtures, parametrize, mocking)
4. Practice the red-green-refactor cycle!

Happy testing! 🚀
