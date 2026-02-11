#!/usr/bin/env -S python3

number = float(input("Give me a number: "))

if number - int(number) == 0:
    print("This number is an integer.")
else:
    print("This number is a decimal.")