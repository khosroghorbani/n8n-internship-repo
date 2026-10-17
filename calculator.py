"""Basic calculator operations."""

from __future__ import annotations

from numbers import Real


_INVALID_OPERAND_MESSAGE = "operands must be real numbers"


def _validate_operands(left: Real, right: Real) -> None:
    """Validate that both operands are real numbers, excluding booleans."""
    if (
        isinstance(left, bool)
        or isinstance(right, bool)
        or not isinstance(left, Real)
        or not isinstance(right, Real)
    ):
        raise TypeError(_INVALID_OPERAND_MESSAGE)


def add(left: Real, right: Real) -> Real:
    """Return the sum of two real numbers."""
    _validate_operands(left, right)
    return left + right


def subtract(left: Real, right: Real) -> Real:
    """Return the difference between two real numbers."""
    _validate_operands(left, right)
    return left - right


def multiply(left: Real, right: Real) -> Real:
    """Return the product of two real numbers."""
    _validate_operands(left, right)
    return left * right


def divide(left: Real, right: Real) -> Real:
    """Return the quotient of two real numbers.

    Raises:
        TypeError: if either operand is not a real number.
        ZeroDivisionError: if the divisor is zero.
    """
    _validate_operands(left, right)
    if right == 0:
        raise ZeroDivisionError("cannot divide by zero")
    return left / right


if __name__ == "__main__":
    print(f"2 + 3 = {add(2, 3)}")
    print(f"7 - 4 = {subtract(7, 4)}")
    print(f"6 * 5 = {multiply(6, 5)}")
    print(f"8 / 2 = {divide(8, 2)}")
