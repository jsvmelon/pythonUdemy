import generators


def sign_flipping_odd_numbers() -> generators:
    odd = 1
    sign = 1
    while True:
        yield odd * sign
        odd += 2
        sign *= -1


def pi_series() -> generators:
    odd = sign_flipping_odd_numbers()
    approximation = 1 / next(odd)
    while True:
        yield approximation * 4
        approximation += 1 / next(odd)


if __name__ == "__main__":
    pi = pi_series()
    for i in range(10000000):
        next(pi)

    print(next(pi))
