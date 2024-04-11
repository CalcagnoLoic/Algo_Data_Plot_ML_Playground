"""
Exercise 1: Reverse the tuple
"""


def reverse_tuple(tuple):
    return tuple[::-1]


"""
Exercise 2: Access value 20 from the tuple
"""


def access_value(tuple):
    return tuple[1][1]


"""
Exercise 3: Unpack the tuple into 4 variables
"""


def unpack_tuple(tuple):
    var1, var2, var3, var4 = tuple
    return var1, var2, var3, var4


"""
Exercise 4: Swap two tuples
"""


def swap_tuple(tuple1, tuple2):
    tuple1, tuple2 = tuple2, tuple1
    return (tuple1, tuple2)


"""
Exercise 5: Copy specific elements from one tuple to a new tuple
"""


def copy_elem(tuple):
    new_tuple = tuple[3:-1]
    return new_tuple


"""
Exercise 6: Modify the tuple

Given is a nested tuple. Write a program to modify the first item (22) of a list inside a following tuple to 222
"""


def update_tuple(tuple):
    tuple[1][0] = 222
    return tuple


"""
Exercise 7: Sort a tuple of tuples by 2nd item
"""


def sort_tuple(t):
    return tuple(sorted(list(t), key=lambda x: x[1]))


"""
Exercise 8: Counts the number of occurrences of item 50 from a tuple
"""


def count_occurrence(tuple, value):
    return tuple.count(value)
