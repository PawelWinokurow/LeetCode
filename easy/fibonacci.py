def fibonacci(n):
    a, b = 0, 1
    for i in range(1,n):
        a, b = b, a + b
    return a


def fibonacci_rec(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci_rec(n-1) + fibonacci_rec(n-2)

n = 7
a = fibonacci_rec(n)
pass