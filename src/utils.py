# Addition
def add(a, b):
    """
    Adds two numbers together.
    """
    return a + b


# Subtraction
def subtract(a, b):
    """
    Subtracts the second number from the first.
    """
    return a - b


# Multiplication
def multiply(a, b):
    """
    Multiplies two numbers together.
    """
    return a * b


# Division
def divide(a, b):
    """
    Divides the first number by the second.
    Raises ValueError if the second number is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


if __name__ == "__main__":
    # Example usage
    print("Addition:", add(2, 3))
    print("Subtraction:", subtract(5, 3))
    print("Multiplication:", multiply(2, 3))
    print("Division:", divide(6, 3))
    try:
        print("Division by zero:", divide(1, 0))
    except ValueError as e:
        print(e)
