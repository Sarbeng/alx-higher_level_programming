#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if sentence[0] == '':
        first = None
    else:
        first = sentence[0]
    multiple = length, first
    return multiple
