#!/usr/bin/env -S python3

from sys import argv

if len(argv) != 2:
    print("none")
else:
    param = argv[1]
    guess = input("What was the parameter? ")
    if param == guess:
        print("Good job!")
    else:
        print("Nope, sorry...")