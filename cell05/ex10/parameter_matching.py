#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("none")
else:
    keyword = sys.argv[1]
    matching = str(input("What was the parameter? " ))

    if matching == keyword:
        print("Good job!")
    else:
        print("Nope, sorry...")
