"""
This module calculates Fibonacci numbers.
"""

def fib(index):
    """
    Calculate the Fibonacci number for the given index.

    Args:
        index (int): Index of the Fibonacci number to calculate.

    Returns:
        int: The Fibonacci number at the given index.
    """
    if index in (0, 1):
        return index

    a, b = 0, 1
    for _ in range(2, index + 1):
        a, b = b, a + b
    return b

if __name__ == "__main__":
    user_input = 7
    print(fib(user_input))
