#!/usr/bin/env python3

def add_one(x):
    x += 1
    print("Inside function:", x)

number = 5
print("Before function:", number)

add_one(number)

print("After function:", number)
