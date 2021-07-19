a = 2
b = 3
print("a = {}, b = {}".format(a, b))

# swapping values the python way
a, b = b, a
print("a = {}, b = {}".format(a, b))


def fibonacci(n: int):
    a_, b_ = 0, 1
    for i in range(0, n+1):
        yield a_
        a_, b_ = b_, a_+b_


for fib in fibonacci(21):
    print(fib)
