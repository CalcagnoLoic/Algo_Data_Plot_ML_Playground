"""
Exercise 1: Write a program to create a function that takes two arguments, name and age, and print their value.
"""


def presentation(name: str, age: int) -> str:
    return "My name is {} and I'm {} years old.".format(name, age)


"""
Exercise 2: Create a function with variable length of arguments

Write a program to create function func1() to accept a variable length of arguments and print their value.
"""


def func1(*args):
    result = ""

    for elem in args:
        result += elem + "\n"

    return result


"""
Exercise 3: Return multiple values from a function

Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call.
"""


def calculation(num1: int, num2: int):
    res1 = num1 + num2
    res2 = num1 - num2

    return [res1, res2]


"""
Exercise 4: Create a function with a default argument

Write a program to create a function show_employee() using the following conditions.

    It should accept the employee’s name and salary and display both.
    If the salary is missing in the function call then assign default value 9000 to salary
"""


def show_employee(name, salary=9000):
    return "Name: {} Salary: {}".format(name, salary)


"""
Exercise 5: Create an inner function to calculate the addition in the following way

    Create an outer function that will accept two parameters, a and b
    Create an inner function inside an outer function that will calculate the addition of a and b
    At last, an outer function will add 5 into addition and return it
"""


def outer_function(a, b):
    def addition(a, b):
        return a + b

    result = addition(a, b)

    return result + 5


"""
Exercise 6: Create a recursive function

Write a program to create a recursive function to calculate the sum of numbers from 0 to 10. 
"""


def recursiv(num: int) -> int:
    if num:
        return num + recursiv(num - 1)
    else:
        return 0


"""
Exercise 7: Assign a different name to function and call it through the new name

Below is the function display_student(name, age). Assign a new name show_student(name, age) to it and call it using the new name.
"""


def display_student(name, age):
    return "My name is {} and I'm {} years old.".format(name, age)


show_student = display_student


"""
Exercise 8: Generate a Python list of all the even numbers between 4 to 30
"""


def even_list():
    return list(range(4, 30, 2))


"""
Exercise 9: Find the largest item from a given list
"""


def largest_item(liste: list):
    return max(liste)
