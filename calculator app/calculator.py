def add(x, y):
    """Adds two numbers."""
    return x + y

def subtract(x, y):
    """Subtracts y from x."""
    return x - y

def multiply(x, y):
    """Multiplies two numbers."""
    return x * y

def divide(x, y):
    """Divides x by y. Raises ValueError if y is zero."""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y
