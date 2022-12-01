#!/usr/bin/python3
"""
Program that 
imports def add(a, b): from the file add_0.py
print resulrs of addition 1+2 = 3
Args:
    a: 1
    b: 2
print: <a value> + <b value> = <add(a, b) value>
followed with a new line
"""
from add_0 import add

a = 1
b = 2

print("{} + {} = {}".format(a, b, add(a, b)))
