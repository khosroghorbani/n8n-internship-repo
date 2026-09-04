def factorial(n: int) -> int:
    """Return n! for non-negative integer n.

    Args:
        n (int): Non-negative integer whose factorial is computed.

    Returns:
        int: Factorial of n.

    Raises:
        TypeError: If n is not an int.
        ValueError: If n is negative.

    Examples:
        >>> factorial(5)
        120
    """
    if not isinstance(n, int):
        raise TypeError("n must be an int")
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
