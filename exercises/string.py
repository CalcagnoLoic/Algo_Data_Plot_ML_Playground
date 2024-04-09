import string

"""
Exercise 1: Append new string in the middle of a given string

Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.
"""


def blend_string(s1, s2):
    middle_string = int(len(s1) / 2)

    return s1[:middle_string:] + s2 + s1[middle_string:]


"""
Exercise 2: Create a new string made of the first, middle, and last characters of each input string
"""


def blend_string_v2(s1, s2):
    def detect_middle_position(s):
        return int(len(s) / 2)

    first_position = s1[0] + s2[0]
    last_position = s1[-1] + s2[-1]
    middle_position = s1[detect_middle_position(s1)] + s2[detect_middle_position(s2)]

    new_string = first_position + middle_position + last_position
    return new_string


"""
Exercise 4: Arrange string characters such that lowercase letters should come first
"""


def first_lowercase(s):
    lowercase = []
    uppercase = []

    for char in s:
        if char.islower():
            lowercase.append(char)
        else:
            uppercase.append(char)

    return "".join(lowercase + uppercase)


"""
Exercise 5: Count all letters, digits, and special symbols from a given string
"""


def count_chars(s):
    letters = []
    digits = []
    symbols = []

    for elem in s:
        if elem.isalpha():
            letters.append(elem)
        elif elem.isnumeric():
            digits.append(elem)
        else:
            symbols.append(elem)

    return (
        "Chars: {}".format(len(letters))
        + "\n"
        + "Digits: {}".format(len(digits))
        + "\n"
        + "Symbols: {}".format(len(symbols))
    )


"""
Exercise 6: Calculate the sum and average of the digits present in a string
"""


def count_sum_avg(s):
    sum = 0
    total_char = 0

    for elem in s:
        if elem.isdigit():
            sum += int(elem)
            total_char += 1

    avg = sum / total_char

    return "Sum: {} Average: {}".format(sum, avg)


"""
Exercise 7: Remove empty strings from a list of strings
"""


def remove_empty_s(s):
    return list(filter(None, s))


"""
Exercise 8: Remove special symbols / punctuation from a string
"""


def remove_special_chars(s):
    return s.translate(str.maketrans("", "", string.punctuation))


"""
Exercise 9: Removal all characters from a string except integers
"""


def remove_all_letters(s):
    return "".join([elem for elem in s if elem.isdigit()])


"""
Exercise 10: Replace each special symbol with # in the following string
"""


def replace_special_chars(s):
    special_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    for elem in special_chars:
        s = s.replace(elem, "#")

    return s
