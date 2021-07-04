def sum_eo(n, t):
    result = 0
    start = None
    if t == "e":
        start = 2
    elif t == "o":
        start = 1
    else:
        return -1

    for i in range(start, n, 2):
        result += i
    return result


print(sum_eo(7, "e"))
print(sum_eo(6, "e"))
print(sum_eo(1000, "e"))
print(sum_eo(0, "e"))

print(sum_eo(7, "o"))
print(sum_eo(9, "o"))
print(sum_eo(3, "a"))
print(sum_eo(0, "o"))
