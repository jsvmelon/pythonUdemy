for i in range(1, 11):
    for j in range(1, 11):
        print(i, i*j)

[print(i, i*j) for i in range(1, 11) for j in range(1, 11)]
