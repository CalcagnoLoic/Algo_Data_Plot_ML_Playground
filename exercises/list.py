"""
Exercise 1: Reverse a list
"""


def reverse_list(l):
    l.reverse()
    return l


"""
Exercise 2: Concatenate two lists index-wise
"""


def concat_list(l1, l2):
    return [i + j for i, j in zip(l1, l2)]


"""
Exercise 3: Turn every item of a list into its square
"""


def square_list(l):
    return [x * x for x in l]


"""
Exercise 4: Concatenate two lists in the following order

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
new_list -> ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
"""


def concat_list_v2(l1, l2):
    return [i + j for i in l1 for j in l2]


"""
Exercise 5: Iterate both lists simultaneously
"""


def iterate_simultaneously(l1, l2):
    return [(i, j) for i, j in zip(l1, l2[::-1])]


"""
Exercise 6: Add new item to list after a specified item

Write a program to add item 7000 after 6000 
"""


def add_specific_item(l):
    l[2][2].append(7000)
    return l


"""
Exercise 7: Extend nested list by adding the sublist
"""


def extend_nested_list(l, sublist):
    l[2][1][2].extend(sublist)
    return l
