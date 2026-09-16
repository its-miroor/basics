"""Tests for calculator module - TDD Example."""

import pytest
from calculator import add, subtract, multiply, divide


class TestAdd:
    """Test cases for the add function."""
    
    # RED -> GREEN -> REFACTOR Cycle Example
    
    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        assert add(2, 3) == 5
    
    def test_add_negative_numbers(self):
        """Test adding negative numbers."""
        assert add(-1, 1) == 0
        assert add(-5, -3) == -8
    
    def test_add_zero(self):
        """Test adding zero."""
        assert add(0, 0) == 0
        assert add(5, 0) == 5
    
    def test_add_floats(self):
        """Test adding floating point numbers."""
        assert add(2.5, 3.5) == 6.0
    
    def test_add_with_invalid_input(self):
        """Test that invalid inputs raise TypeError."""
        with pytest.raises(TypeError):
            add("2", 3)
        
        with pytest.raises(TypeError):
            add(None, 5)
        
        with pytest.raises(TypeError):
            add([1, 2], 3)


class TestSubtract:
    """Test cases for the subtract function."""
    
    def test_subtract_positive_numbers(self):
        """Test subtracting two positive numbers."""
        assert subtract(5, 3) == 2
    
    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers."""
        assert subtract(-1, -1) == 0
        assert subtract(-5, -3) == -2
    
    def test_subtract_zero(self):
        """Test subtracting zero."""
        assert subtract(5, 0) == 5
        assert subtract(0, 0) == 0
    
    def test_subtract_floats(self):
        """Test subtracting floating point numbers."""
        assert subtract(5.5, 2.5) == 3.0
    
    def test_subtract_with_invalid_input(self):
        """Test that invalid inputs raise TypeError."""
        with pytest.raises(TypeError):
            subtract("5", 3)
        
        with pytest.raises(TypeError):
            subtract(None, 5)
        
        with pytest.raises(TypeError):
            subtract([1, 2], 3)


class TestMultiply:
    """Test cases for the multiply function."""
    
    def test_multiply_positive_numbers(self):
        """Test multiplying two positive numbers."""
        assert multiply(3, 4) == 12
    
    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers."""
        assert multiply(-2, 3) == -6
        assert multiply(-2, -3) == 6
    
    def test_multiply_zero(self):
        """Test multiplying by zero."""
        assert multiply(0, 5) == 0
        assert multiply(5, 0) == 0
        assert multiply(0, 0) == 0
    
    def test_multiply_floats(self):
        """Test multiplying floating point numbers."""
        assert multiply(2.5, 4.0) == 10.0
        assert multiply(0.5, 0.5) == 0.25
    
    def test_multiply_with_invalid_input(self):
        """Test that invalid inputs raise TypeError."""
        with pytest.raises(TypeError):
            multiply("3", 4)
        
        with pytest.raises(TypeError):
            multiply(None, 5)
        
        with pytest.raises(TypeError):
            multiply([1, 2], 3)


class TestDivide:
    """Test cases for the divide function."""
    
    def test_divide_positive_numbers(self):
        """Test dividing two positive numbers."""
        assert divide(10, 2) == 5.0
        assert divide(9, 3) == 3.0
    
    def test_divide_negative_numbers(self):
        """Test dividing negative numbers."""
        assert divide(-10, 2) == -5.0
        assert divide(-10, -2) == 5.0
    
    def test_divide_floats(self):
        """Test dividing floating point numbers."""
        assert divide(7.5, 2.5) == 3.0
        assert divide(1.0, 4.0) == 0.25
    
    def test_divide_by_zero(self):
        """Test that dividing by zero raises ZeroDivisionError."""
        with pytest.raises(ZeroDivisionError):
            divide(10, 0)
        
        with pytest.raises(ZeroDivisionError):
            divide(0, 0)
    
    def test_divide_with_invalid_input(self):
        """Test that invalid inputs raise TypeError."""
        with pytest.raises(TypeError):
            divide("10", 2)
        
        with pytest.raises(TypeError):
            divide(None, 5)
        
        with pytest.raises(TypeError):
            divide([1, 2], 3)
