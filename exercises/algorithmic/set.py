"""
Exercise 1: Add a list of elements to a set
"""


def add_list_to_set(list, set):
    set.update(list)
    return set


"""
Exercise 2: Return a new set of identical items from two sets
"""


def intersection_set(s1, s2):
    set = s1.intersection(s2)
    return set


"""
Exercise 3: Get Only unique items from two sets
"""


def union_set(s1, s2):
    set = s1.union(s2)
    return set


"""
Exercise 4: Update the first set with items that don’t exist in the second set
"""


def difference_update(s1, s2):
    s1.difference_update(s2)
    return s1


"""
Exercise 5: Remove items from the set at once
"""


def remove_items(s):
    s.difference_update({10, 20, 30})
    return s


"""
Exercise 6: Return a set of elements present in Set A or B, but not both
"""


def symmetric_diff(s1, s2):
    set = s1.symmetric_difference(s2)
    return set


"""
Exercise 7: Check if two sets have any elements in common. If yes, display the common elements
"""


def disjoint(s1, s2):
    if s1.isdisjoint(s2):
        print("Two sets have no items in common")
    else:
        print("Two sets have items in common")
        set = s1.intersection(s2)
        return set


"""
Exercise 8: Update set1 by adding items from set2, except common items
"""


def symmetric_diff_update(s1, s2):
    s1.symmetric_difference_update(s2)
    return s1


"""
Exercise 9: Remove items from set1 that are not common to both set1 and set2
"""


def intersection_update(s1, s2):
    s1.intersection_update(s2)
    return s1
