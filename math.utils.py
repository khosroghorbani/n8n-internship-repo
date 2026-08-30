"""Math utility functions."""

def factorial(n: int) -> int:
    """Return n! for non-negative integers. Raises ValueError for negative input and TypeError for non-int."""
    if not isinstance(n, int):
        raise TypeError('n must be an int')
    if n < 0:
        raise ValueError('n must be non-negative')
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
