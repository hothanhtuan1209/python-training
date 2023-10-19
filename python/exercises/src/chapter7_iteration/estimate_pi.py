import math


def factorial(n):
    """
    Calculate the factorial of an integer.

    Recursively computes the factorial of an integer 'n'.

    Parameters:
        n (int): The non-negative integer for which to calculate the factorial.

    Returns:
        int: The factorial of 'n'.
    """
    if n == 0:
        return 1
    else:
        recurse = factorial(n - 1)
        result = n * recurse
        return result


def estimate_pi():
    """
    Estimate the mathematical constant pi using a mathematical series.

    This function estimates the value of pi using a mathematical series
    expansion. It calculates the series until a term is smaller than 1e-15
    and returns the estimate.

    Returns:
        float: The estimated value of pi.
    """
    total = 0
    k = 0
    factor = 2 * math.sqrt(2) / 9801
    while True:
        num = factorial(4 * k) * (1103 + 26390 * k)
        den = factorial(k) ** 4 * 396 ** (4 * k)

        total += num / den
        term = factor * num / den

        if abs(term) < 1e-15:
            break
        k += 1
    return 1 / (factor * total)


print(estimate_pi())
print(math.pi)
