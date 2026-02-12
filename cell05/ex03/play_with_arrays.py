#!/usr/bin/env -S python3

arr = [2, 8, 9, 48, 8, 22, -12, 2]
new_arr = []

for x in arr:
    if arr.count(x) > 1:
        continue
    
    if x > 5:
        new_arr.append(x + 2)

print(f"Original array: {arr}")
print(f"New array: {new_arr}")