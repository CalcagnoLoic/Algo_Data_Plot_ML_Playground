from datetime import datetime, timedelta
from time import strftime, gmtime

"""
Exercise 1: Print current date and time in Python
"""


def display_date():
    return strftime("%Y-%m-%d %H:%M", gmtime())


"""
Exercise 2: Convert string into a datetime object
"""


def transform_into_datetime(s):
    dt_obj = datetime.strptime(s, "%b %d %Y %I:%M%p")

    return dt_obj.strftime("%Y-%m-%d %H:%M:%S")


"""
Exercise 3: Subtract a week (7 days)  from a given date in Python
"""


def time_delta(y, m, d):
    date = datetime(y, m, d)
    new_date = date - timedelta(days=7)
    return new_date.strftime("%Y-%m-%d")

"""
Exercise 4: Print a date in a the following format

Day_name  Day_number  Month_name  Year
"""
def format_date(y, m, d):
    date = datetime(y, m, d)
    return date.strftime("%A %d %B %Y")

"""
Exercise 5: Find the day of the week of a given date
"""
def find_day_name(y, m, d):
    return datetime(y, m, d).strftime("%A")