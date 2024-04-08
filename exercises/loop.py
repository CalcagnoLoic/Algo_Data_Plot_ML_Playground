"""
Exercise 1: Print First 10 natural numbers using while loop
"""


def while_loop():
    x = 1

    while x <= 10:
        print(x)
        x += 1


"""
Exercise 2: Calculate the sum of all numbers from 1 to a given number
"""


def calculate_number() -> int:
    number = int(input("Enter a number: "))
    sum = 0

    for x in range(1, number + 1):
        sum += x

    return sum


"""
Exercise 3: Display numbers from a list using loop

Write a program to display only those numbers from a list that satisfy the following conditions

    The number must be divisible by five
    If the number is greater than 150, then skip it and move to the next number
    If the number is greater than 500, then stop the loop
"""


def display_numbers_from_list(liste: list):
    for elem in liste:
        if elem > 500:
            break
        elif elem > 150:
            continue
        elif elem % 5 == 0:
            print(elem)


"""
Exercise 4: Count the total number of digits in a number

Write a program to count the total number of digits in a number using a while loop.
"""


def count_with_while(num: int):
    count = 0

    while num != 0:
        num = num // 10
        count += 1

    return count


"""
Exercise 5: Write a program to display all prime numbers within a range
"""


def prime_number(start: int, end: int) -> int:
    for elem in range(start, end):
        if elem > 1:
            for item in range(2, elem):
                if elem % item == 0:
                    break
            else:
                print(elem)

