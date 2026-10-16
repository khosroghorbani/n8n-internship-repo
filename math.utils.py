"""Utility math functions."""


_INVALID_N_MESSAGE = "n must be a non-negative integer"


def factorial(n: int) -> int:
    """Return factorial of a non-negative integer n using an iterative algorithm.

    Boolean values are rejected even though ``bool`` is a subclass of ``int``.

    Raises:
        ValueError: if n is not an int, is a boolean, or is negative.
    """
    if isinstance(n, bool) or not isinstance(n, int) or n < 0:
        raise ValueError(_INVALID_N_MESSAGE)

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
