print(__file__)

numbers = [1, 2, 3, 4, 5, 6]

number = int(input("Please enter a number: "))

squares = [number ** 2 for number in range(1, 11)]  # this code is NOT modifying the value of 'number' in the out scope

index_pos = numbers.index(number)
print(squares[index_pos])
