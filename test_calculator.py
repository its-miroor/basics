"""Tests for calculator module - TDD Example."""

import pytest
from calculator import add, subtract


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
