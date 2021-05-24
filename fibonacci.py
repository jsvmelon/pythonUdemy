from typing import Tuple


def fibonacci_helper(n: int) -> Tuple:
    """
    Helper function that recursively calculates the n-th fibonacci number but
    return a tuple of the n-th and (n-1)-th fibonacci number.
    :param n: positive integer to specify which fibonacci number is calculated
    :return: A tuple containing the n-th and the n-1-th fibonacci number
    """
    if n < 0:
        raise ValueError
    elif n == 0:
        return 1, 0
    else:
        previous = fibonacci_helper(n - 1)
        return previous[0] + previous[1], previous[0]


def fibonacci(n: int) -> int:
    """
    Calculates the `n` -th fibonacci number, starting with 0 for f_0
    :param n: zero or any positive integer
    :return: the n-th fibonacci number
    """
    return fibonacci_helper(n)[0]


def fibonacci_iterative(n: int) -> int:
    """
    Calculates the `n` -th fibonacci number, starting with 0 for f_0 in with
    an iteration instead of recursion.
    :exception ValueError: if `n` is lower than 0
    :param n: zero or any positive integer
    :return: the n-th fibonacci number
    """
    if n < 0:
        raise ValueError
    result, n_minus_1, n_minus_2 = 1, 1, 1
    for number in range(1, n):
        result = n_minus_1 + n_minus_2
        n_minus_2 = n_minus_1
        n_minus_1 = result
    return result


print(fibonacci_iterative(0))
print(fibonacci_iterative(1))
print(fibonacci_iterative(2))
print(fibonacci_iterative(3))
print(fibonacci_iterative(4))

# print(fibonacci(0))
# print(fibonacci(1))
# print(fibonacci(2))
# print(fibonacci(3))
# print(fibonacci(4))
# print(fibonacci(100))
