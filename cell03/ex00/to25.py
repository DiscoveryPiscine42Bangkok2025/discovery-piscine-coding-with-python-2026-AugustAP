#!/usr/bin/env -S python3

print("Enter a number less than 25")
number = int(input())

if number <= 25:
    while number < 26:  
        print("Inside the loop, my variable is",number)
        number += 1
else:
    print("Error")