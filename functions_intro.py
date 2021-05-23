def multiply(a, b):
    result = a * b
    return result


def is_palindrome(string):
    return string[::-1].casefold() == string.casefold()


def is_palindrome_sentence(string):
    result = ""
    for char in string:
        if char.isalpha():
            result += char
    return is_palindrome(result)


print(is_palindrome_sentence("Hallo Du gruenes Ei"))
print(is_palindrome_sentence("Was it a car or a cat I saw?"))
print(is_palindrome_sentence("Go hang a salami, I'm a lasagna hog"))



# answer = multiply(10, "hello")
# print(answer)
#
# while True:
#     word = input("Please enter a word to check: ")
#     if is_palindrome(word):
#         print("{} is a palindrome")
#     else:
#         print("{} is not a palindrome")
