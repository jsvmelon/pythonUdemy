def fact(n):
    """ calculate n! iteratively"""
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result


def fact_recursive(n: int) -> int:
    """ calculate n! recursively """
    if n < 0:
        raise ValueError("n! is not defined for negative numbers")
    if 0 <= n <= 1:
        return 1
    return fact_recursive(n - 1) * n


def fib_recursive(n: int) -> int:
    if n <= 2:
        return 1
    return fib_recursive(n - 2) + fib_recursive(n - 1)


def fib(n: int) -> int:
    """ returns the n-th number of the fibonacci series """
    n_minus_2, n_minus_1 = (1, 1)
    if 0 <= n <= 2:
        return 1
    for _ in range(3, n + 1):
        next_value = n_minus_1 + n_minus_2
        n_minus_2 = n_minus_1
        n_minus_1 = next_value
    return n_minus_1


if __name__ == "__main__":
    for i in range(0, 30):
        print(i, fact_recursive(i))

    for i in range(0, 36):
        print(fib_recursive(i))

    for i in range(0, 36):
        print(i, fib(i))
