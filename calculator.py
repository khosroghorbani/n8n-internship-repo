from numbers import Real


def _validate_numbers(left, right):
    """Validate that both operands are real numbers, excluding booleans."""
    if isinstance(left, bool) or isinstance(right, bool):
        raise TypeError("operands must be real numbers, not bool")
    if not isinstance(left, Real) or not isinstance(right, Real):
        raise TypeError("operands must be real numbers")


def add(left, right):
    """Return the sum of two real numbers."""
    _validate_numbers(left, right)
    return left + right


def subtract(left, right):
    """Return the difference between two real numbers."""
    _validate_numbers(left, right)
    return left - right


def multiply(left, right):
    """Return the product of two real numbers."""
    _validate_numbers(left, right)
    return left * right


def divide(left, right):
    """Return the quotient of two real numbers.

    Raises:
        ZeroDivisionError: If the divisor is zero.
    """
    _validate_numbers(left, right)
    if right == 0:
        raise ZeroDivisionError("cannot divide by zero")
    return left / right


def main():
    """Run a small demonstration of the calculator operations."""
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
    print(f"4 * 3 = {multiply(4, 3)}")
    print(f"8 / 2 = {divide(8, 2)}")


if __name__ == "__main__":
    main()
