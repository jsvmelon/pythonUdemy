import sys


def my_range(n: int):
    print("my_range starts")
    start = 0
    while start < n:
        print("my_range is returning {}".format(start))
        yield start
        start += 1


_ = input("line 13")
big_range = my_range(5)

_ = input("line 16")
print("big range is {} bytes".format(sys.getsizeof(big_range)))

# create a list containing all the values in big range
big_list = []
_ = input("line 21")
for value in big_range:
    _ = input("line 23")
    big_list.append(value)

print("big list is {} bytes".format(sys.getsizeof(big_list)))
print(big_range)
print(big_list)
