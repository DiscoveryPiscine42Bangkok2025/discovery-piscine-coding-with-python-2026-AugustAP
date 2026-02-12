#!/usr/bin/env -S python3

from sys import argv

if len(argv) < 2:
    print("none")
else:
    print(f"parameters: {len(argv)-1}")
    for i in range(1, len(argv)):
        print(f"{argv[i]}: {len(argv[i])}")