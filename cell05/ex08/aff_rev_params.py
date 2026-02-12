#!/usr/bin/env -S python3

from sys import argv

if len(argv) <= 2:
    print("none")
else:
    for param in reversed(argv[1:]):
        print(param)