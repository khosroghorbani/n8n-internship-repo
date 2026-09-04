def factorial(n):
    """Calculate and return the factorial of a non-negative integer n.

    Raises ValueError if n is not an int or is negative.
    """
    if not isinstance(n, int):
        raise ValueError("n must be a non-negative integer")
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

__all__ = ["factorial"]
