"""Basic arithmetic operations for a simple calculator."""

from numbers import Real


def _validate_numbers(left: Real, right: Real) -> None:
    """Validate that both operands are real numbers, excluding booleans."""
    if isinstance(left, bool) or isinstance(right, bool):
        raise TypeError("operands must be real numbers")
    if not isinstance(left, Real) or not isinstance(right, Real):
        raise TypeError("operands must be real numbers")


def add(left: Real, right: Real) -> Real:
    """Return the sum of two real numbers."""
    _validate_numbers(left, right)
    return left + right


def subtract(left: Real, right: Real) -> Real:
    """Return the difference between two real numbers."""
    _validate_numbers(left, right)
    return left - right


def multiply(left: Real, right: Real) -> Real:
    """Return the product of two real numbers."""
    _validate_numbers(left, right)
    return left * right


def divide(left: Real, right: Real) -> float:
    """Return the quotient of two real numbers.

    Raises:
        ValueError: If the divisor is zero.
        TypeError: If either operand is not a real number.
    """
    _validate_numbers(left, right)
    if right == 0:
        raise ValueError("cannot divide by zero")
    return left / right


def power(left: Real, right: Real) -> Real:
    """Return the first real number raised to the power of the second."""
    _validate_numbers(left, right)
    return left ** right


def main() -> None:
    """Run a small smoke demonstration of the calculator operations."""
    print(f"2 + 3 = {add(2, 3)}")
    print(f"7 - 4 = {subtract(7, 4)}")
    print(f"6 * 5 = {multiply(6, 5)}")
    print(f"10 / 2 = {divide(10, 2)}")


if __name__ == "__main__":
    main()
