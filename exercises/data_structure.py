"""
Exercise 1: Create a list by picking an odd-index items from the first list and even index items from the second
"""


def create_new_list(l1, l2):
    elem_l1 = l1[1::2]
    elem_l2 = l2[0::2]

    return list(elem_l1 + elem_l2)


"""
Exercise 2: Remove and add item in a list

Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.
"""


def remove_add_into_list(l):
    item = l.pop(4)
    l.append(item)
    l.insert(2, item)

    return l


"""
Exercise 3: Slice list into 3 equal chunks and reverse each chunk
"""


def create_chunk(l):
    chunk_size = len(l) // 3

    for i in range(0, len(l), chunk_size):
        item = l[i : chunk_size + i]
        print(item[::-1])


"""
Exercise 4: Count the occurrence of each element from a list

Write a program to iterate a given list and count the occurrence of each element and create a dictionary to show the count of each element.
"""


def count_occurs(l):
    counter = dict()

    for i in l:
        counter[i] = counter.get(i, 0) + 1

    return counter


"""
Exercise 5: Create a Python set such that it shows the element from both lists in a pair
"""


def zip_set(l1, l2):
    return set(zip(l1, l2))


"""
Exercise 6: Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list
"""


def exist_dict_list(l, d):
    return [item for item in l if item in d.values()]


"""
Exercise 7: Remove duplicates from a list and create a tuple and find the minimum and maximum number
"""


def find_min_max(l):
    my_tuple = tuple(set(l))

    return "Min: {} Max: {}".format(min(my_tuple), max(my_tuple))
