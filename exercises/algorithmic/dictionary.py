"""
Exercise 1: Convert two lists into a dictionary
"""


def transform_list_into_dict(l1, l2):
    return dict(zip(l1, l2))


"""
Exercise 2: Merge two Python dictionaries into one
"""


def merge_dict(d1, d2):
    return {**d1, **d2}


"""
Exercise 3: Print the value of key ‘history’ from the below dict

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
"""


def nested_dict(d):
    return d["class"]["student"]["marks"]["history"]


"""
Exercise 4: Initialize dictionary with default values
"""


def initialize_dict(l, d):
    return dict.fromkeys(l, d)


"""
Exercise 5: Create a dictionary by extracting the keys from a given dictionary
"""


def extract_keys(dictionary, keys):
    return {k: dictionary[k] for k in keys}


"""
Exercise 6: Delete a list of keys from a dictionary
"""


def delete_keys(dictionary, keys):
    for key in keys:
        del dictionary[key]

    return dictionary


"""
Exercise 7: Check if a value exists in a dictionary
"""


def check_values(dictionary, value):
    if value in dictionary.values():
        return "La valeur '{}' est bien présente".format(value)


"""
Exercise 8: Get the key of a minimum value from the following dictionary
"""


def min_key(dictionary):
    return min(dictionary, key=dictionary.get)


"""
Exercise 9: Change value of a key in a nested dictionary

Write a Python program to change Brad’s salary to 8500 in the dictionary.
"""


def update_nested_dictionary(dictionary):
    dictionary["emp3"]["salary"] = 8500
    return dictionary
