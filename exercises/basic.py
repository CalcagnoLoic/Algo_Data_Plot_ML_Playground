"""
Exercise 1: Calculate the multiplication and sum of two numbers

Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
"""


def make_calculation(n1: int, n2: int) -> str:
    if n1 * n2 <= 1000:
        return "The result is {}.".format(n1 * n2)
    else:
        return "The result is {}.".format(n1 + n2)


"""
Exercise 2: Print the sum of the current number and the previous number

Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.
"""


def make_iteration() -> str:
    result = ""
    sum = 0

    for x in range(1, 10):
        total = sum + x
        result += "Current Number {} Previous Number {} Sum: {} \n".format(
            x, sum, total
        )
        sum = x

    return result


"""
Exercise 3: Print characters from a string that are present at an even index number

Write a program to accept a string from the user and display characters that are present at an even index number.
"""


def print_char() -> str:
    original_string = input("Enter a string: ")
    length = len(original_string)
    result = ""

    for i in range(0, length - 1, 2):
        result += original_string[i] + "\n"

    return result


"""
Exercise 4: Remove first n characters from a string

Write a program to remove characters from a string starting from zero up to n and return a new string.
"""


def remove_chars(string: str, n: int) -> str:
    return string[n:]


"""
Exercise 5: Check if the first and last number of a list is the same

Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.
"""


def check_first_last_number(list: list) -> bool:
    if list[0] == list[-1]:
        return True
    else:
        return False


"""
Exercise 6: Display numbers divisible by 5 from a list

Iterate the given list of numbers and print only those numbers which are divisible by 5.
"""


def display_5_fold(number: list) -> list:
    multiple = []
    for x in number:
        if x % 5 == 0:
            multiple.append(x)

    return multiple


"""
Exercise 7: Return the count of a given substring from a string

Write a program to find how many times substring “Emma” appears in the given string.
"""


def display_count(string: str) -> str:
    return string.count("Emma")


"""
Exercise 8: Print the following pattern

1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
"""


def pattern(num: int):
    for i in range(num):
        for j in range(i):
            print(i, end=" ")

        print("\r")


"""
Exercise 9: Check Palindrome Number

Write a program to check if the given number is a palindrome number.
"""


def is_palindrom(string: str) -> bool:
    if string == string[::-1]:
        return True
    else:
        return False


"""
Exercise 10: Create a new list from two list using the following condition

Given two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.
"""


def new_list(list1: list, list2: list) -> list:
    new_list_1 = []
    new_list_2 = []

    for i in list1:
        if i % 2 != 0:
            new_list_1.append(i)

    for j in list2:
        if j % 2 == 0:
            new_list_2.append(j)

    return new_list_1 + new_list_2


"""
Exercise 11: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.

Note here exp is a non-negative integer, and the base is an integer.
"""


def exponent(base: int, exp: int) -> int:
    if exp > 0:
        return base**exp
    else:
        raise Exception("Exponent must be positive")
