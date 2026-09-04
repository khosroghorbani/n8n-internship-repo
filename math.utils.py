"""Utility math functions."""


def factorial(n: int) -> int:
    """Return factorial of a non-negative integer n using an iterative algorithm.

    Raises:
        ValueError: if n is not an int or is negative.
    """
    # Reject booleans (bool is a subclass of int)
    if not isinstance(n, int) or isinstance(n, bool):
        raise ValueError("n must be a non-negative integer")
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
