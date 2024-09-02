#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number.

    This function uses a recursive approach to calculate the factorial
    of a non-negative integer. The factorial of a number n is the product
    of all positive integers less than or equal to n. For example, factorial(5)
    is 5 * 4 * 3 * 2 * 1 which equals 120.

    Parameters:
    n (int): A non-negative integer whose factorial is to be computed.

    Returns:
    int: The factorial of the given number n. For n = 0, the function returns 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
