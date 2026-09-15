# basics
A Python project learning Test-Driven Development with basic functions
# TEST (Red)
def test_add():
    assert add(2, 3) == 5

# CODE (Green)
def add(a, b):
    return a + b

# REFACTOR (Blue)
# In this case, it's already clean!