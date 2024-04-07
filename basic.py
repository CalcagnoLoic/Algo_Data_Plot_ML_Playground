"""
Exercise 1: Calculate the multiplication and sum of two numbers

Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
"""


def make_calculation(n1: int, n2: int) -> str:
    if n1 * n2 <= 1000:
        print("The result is {}.".format(n1 * n2))
    else:
        print("The result is {}.".format(n1 + n2))


make_calculation(20, 30)
make_calculation(40, 30)

"""
Exercise 2: Print the sum of the current number and the previous number

Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.
"""
