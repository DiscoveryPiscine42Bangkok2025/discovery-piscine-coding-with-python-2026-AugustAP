#!/usr/bin/env -S python3

print("Enter the first number:")
n1 = int(input())
print("Enter the second number:")
n2 = int(input())
total = n1 * n2
print(f"{n1} x {n2} = {total}")
if total < 0:
    print("The result is negative.")
elif total == 0:
    print("The result is positive and negative.")
elif total > 0:
    print("The result is positive.")