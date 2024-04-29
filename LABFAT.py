def fib(n):

    if n in (0, 1):
        return n
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

if __name__ == "__main__":
    n = int(input("Enter the index of the Fibonacci number: "))
    print(fib(n))
