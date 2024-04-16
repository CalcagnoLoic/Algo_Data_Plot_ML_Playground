import random
import secrets
import string
import time
from random import sample

"""
Exercise 1: Generate 3 random integers between 100 and 999 which is divisible by 5
"""
print("Generation of 3 randoms intergers: ")
for num in range(3):
    print(random.randrange(100, 999, 3))

print("---------------------------")


"""
Exercise 2: Random Lottery Pick. Generate 100 random lottery tickets and pick two lucky tickets from it as a winner.
"""
lottery_tickets = []
for i in range(100):
    lottery_tickets.append(random.randrange(1000000000, 9999999999))

winner_tickets = sample(lottery_tickets, 2)
print("The lottery tickets are:", winner_tickets)
print("---------------------------")


"""
Exercise 3: Generate 6 digit random secure OTP
"""
secure_choice = secrets.SystemRandom()
random_secure_OTP = secure_choice.randrange(100000, 999999)

print("Generate a random secure OTP: ", random_secure_OTP)
print("---------------------------")


"""
Exercise 4: Pick a random character from a given String
"""
mystring = "random-generation"
print("Random character is: ", random.choice(mystring))
print("---------------------------")


"""
Exercise 5: Generate random String of length 5
"""


def generate_random_string(n):
    letters = string.ascii_letters
    res = "".join(random.choice(letters) for x in range(n))
    return res


print("A random string of 5 chars: ", generate_random_string(5))
print("A random string of 15 chars: ", generate_random_string(15))
print("---------------------------")


"""
Exercise 6: Generate a random Password which meets the following conditions
    Password length must be 10 characters long.
    It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.
"""


def generate_password():
    chars = string.ascii_letters + string.punctuation + string.digits
    password = random.sample(chars, 6)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)
    password += random.sample(string.ascii_uppercase, 2)

    random.shuffle(password)
    password = "".join(password)

    return password


print("My password is: ", generate_password())
print("---------------------------")


"""
Exercise 7: Calculate multiplication of two random float numbers

Note:
    First random float number must be between 0.1 and 1
    Second random float number must be between 9.5 and 99.5
"""
first_random_number = round(random.uniform(0.1, 1), 1)
secund_random_number = round(random.uniform(9.5, 99.5), 1)

print(
    "Result of multiplication is equal to: ", first_random_number * secund_random_number
)
print("---------------------------")


"""
Exercise 8: Generate random secure token of 64 bytes and random URL
"""

print("Random secure token 64bytes:", secrets.token_hex(64))
print("Random secure URL: ", secrets.token_urlsafe(64))
print("---------------------------")


"""
Exercise 9: Roll dice in such a way that every time you get the same number

Dice has 6 numbers (from 1 to 6). Roll dice in such a way that every time you must get the same output number. do this 5 times.
"""
dice = [1, 2, 3, 4, 5, 6]
for i in range(5):
    random.seed(50)
    print(random.choice(dice))
print("---------------------------")

"""
Exercise 10: Generate a random date between given start and end dates
"""


def get_random_date(start, end):
    dateformat = "%d/%m/%Y"

    start_time = time.mktime(time.strptime(start, dateformat))
    end_time = time.mktime(time.strptime(end, dateformat))

    random_time = random.uniform(start_time, end_time)
    random_date =  time.strftime(dateformat, time.localtime(random_time))

    return random_date


print("Generate a random between date: ", get_random_date("16/04/2020", "16/04/2024"))
