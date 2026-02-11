#!/usr/bin/env -S python3

from sys import argv

count = 0
if len(argv) != 3:
    print("none")
    exit(0)
else :
    x = argv[1]
    message = argv[2].split(' ')
    for i in message:
        if x == i:
            count += 1
    print(count)