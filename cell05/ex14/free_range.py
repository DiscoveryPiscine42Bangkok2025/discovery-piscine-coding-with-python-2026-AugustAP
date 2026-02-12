#!/usr/bin/env -S python3

from sys import argv

if len(argv) != 3:
    print("none")
else:
    arr = []
    for i in range(int(argv[1]), int(argv[2])+1):
        arr.append(i)
    print(arr)