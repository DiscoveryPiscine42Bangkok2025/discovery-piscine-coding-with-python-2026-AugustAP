#!/usr/bin/env -S python3

from sys import argv

if len(argv) != 2:
    print("none")
else:
    str = ""
    for char in argv[1]:
        if char == 'z' :
            str += 'z'
    if str == '':
        str = "none"
    print(str)