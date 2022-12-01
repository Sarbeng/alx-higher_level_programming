#!/usr/bin/python3
"""My maths program

 Args:
 a: first integer
 b: second integer

Returns:
The return value. a + b
"""

if __name__ == " __main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    """Print the sum of a and b """
    print(f"{a} + {b} = {add(a, b)}")

    """Print the sub of a and b """
    print(f"{a} - {b} = {sub(a, b)}")

    """Print the multiplication of a and b """
    print(f"{a} * {b} = {mul(a, b)}")

    """Print the div of a and b """
    print(f"{a} / {b} = {div(a, b)}")
