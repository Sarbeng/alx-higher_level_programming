#!/usr/bin/env python3
def no_c(my_string):
    copy = []
    for x in my_string:
        if x != 'c' and x != 'C':
            # print(x)
            copy.append(x)
    return ("".join(copy))
