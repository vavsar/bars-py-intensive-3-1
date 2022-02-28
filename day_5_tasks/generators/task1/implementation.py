def fib(n):
    if n < 3:
        yield 1

    a = b = 1
    for _ in range(n - 2):
        c = a + b
        a, b = b, c
        yield c

