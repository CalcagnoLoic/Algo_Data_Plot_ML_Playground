import os

"""
Exercise 1: Accept numbers from a user

Write a program to accept two numbers from the user and calculate multiplication
"""


def make_user_calculation():
    number_1 = int(input("Enter a first number: "))
    number_2 = int(input("Enter a secund number: "))

    return number_1 * number_2


"""
Exercise 2: Display three string “Name”, “Is”, “James” as “Name**Is**James”

Display the ** separator between each string.
"""


def display_string(string1: str, string2: str, string3: str) -> str:
    return f"{string1}**{string2}**{string3}"


"""
Exercise 3: Convert Decimal number to octal using print() output formatting
"""


def display_octal(num: int) -> int:
    return int("{:o}".format(num))


"""
Exercise 4: Display float number with 2 decimal places
"""


def display_float(num: float) -> float:
    return float("{:.2f}".format(num))


"""
Exercise 5: Accept a list of 5 float numbers as an input from the user
"""


def display_list() -> list:
    user_input = str(input("Enter float numbers separated by space: "))
    user_list = [float(i) for i in user_input.split()]

    return user_list


"""
Exercise 6: Write all content of a given file into a new file by skipping line number 5
"""


def read_write_file():
    try:
        with open("exercises/files/file.txt") as fp:
            lines = fp.readlines()

        with open("exercises/files/new_file.txt", "w") as fp:
            count = 0
            for line in lines:
                if count == 4:
                    count += 1
                    continue
                else:
                    fp.write(line)
                count += 1

    except FileNotFoundError:
        print("oops")


"""
Exercise 7: Check file is empty or not
"""


def is_empty_file():
    return os.stat("exercises/files/new_file.txt").st_size == 0


"""
Exercise 8: Read line number 4 from the following file
"""


def read_4th_line():
    with open("exercises/files/new_file.txt", "r") as fp:
        for i, line in enumerate(fp.readlines()):
            if i == 3:
                return line
