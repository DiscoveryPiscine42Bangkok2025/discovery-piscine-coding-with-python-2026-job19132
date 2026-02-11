#!/usr/bin/env python3
number = float(input("Give me a number: "))

if number.is_integer():
    print(int(number))
else:
    print(int(number) + 1)
