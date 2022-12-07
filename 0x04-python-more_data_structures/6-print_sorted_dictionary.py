#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # function that prints a dictionary by ordered keys using .items()
    # first have to sort the dictionary using sorted
    # then print the dictionary
    for key in sorted(a_dictionary.keys()):
        print('{} : {}'.format(key, a_dictionary[key]))
