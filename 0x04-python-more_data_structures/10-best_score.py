#!/usr/bin/python3

def best_score(a_dictionary):
    # if no score found return None
    if a_dictionary:
        # return key with biggest value.
        # find biggest value
        # max_value = max(a_dictionary.values())
        # return key of biggest value
        return max(a_dictionary, key=a_dictionary.get)
    else:
        None
