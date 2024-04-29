"""
This module calculates Fibonacci numbers.
"""

def fib(n):
    """
    Calculate the Fibonacci number for the given index.

    Args:
        n (int): Index of the Fibonacci number to calculate.

    Returns:
        int: The Fibonacci number at the given index.
    """
    if n in (0, 1):
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

if __name__ == "__main__":
    n = int(input("Enter the index of the Fibonacci number: "))
    print(fib(n))
