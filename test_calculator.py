"""Tests for calculator module - TDD Example."""

import pytest
from calculator import add


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
