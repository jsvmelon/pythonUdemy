import timeit
from statistics import mean, stdev


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


if __name__ == "__main__":
    def fact_wrapper() -> int:
        """Wrapper for timing using a fixed number as the argument"""
        return fact(900)


    def fact_recursive_wrapper() -> int:
        """Wrapper for timing using a fixed number as the argument"""
        return fact_recursive(900)


    t1 = timeit.repeat(fact_wrapper, number=1000)
    print(t1)
    print(sum(t1), mean(t1), stdev(t1))  # not useful as we don't control the overall system sufficiently

    t2 = timeit.repeat(fact_recursive_wrapper, number=1000)
    print(t2)
    print(sum(t2), mean(t2), stdev(t2))  # not useful as we don't control the overall system sufficiently
