#!/usr/bin/python3

def uniq_add(my_list=[]):
    # first we need to get the unique values
    uniq = list(set(my_list))
    # set an empty variable to do the addition
    add = 0
    # loop through our unique values and add them
    for i in range(len(uniq)):
        add += uniq[i]
    return add
