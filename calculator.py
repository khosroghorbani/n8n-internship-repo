"""Simple arithmetic calculator."""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return a minus b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return a divided by b.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("cannot divide by zero")
    return a / b


def power(a, b):
    """Return a raised to the power of b."""
    return a ** b


if __name__ == "__main__":
    print("2 + 3 =", add(2, 3))
    print("7 - 4 =", subtract(7, 4))
    print("5 * 6 =", multiply(5, 6))
    print("8 / 2 =", divide(8, 2))
    print("2 ** 3 =", power(2, 3))
