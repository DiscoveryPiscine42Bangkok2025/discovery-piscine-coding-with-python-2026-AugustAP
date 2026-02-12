#!/usr/bin/env -S python3

from sys import argv

if len(argv) < 2:
    print("none")
else:
    for param in argv[1:]:
        if param.endswith("ism"):
            continue
        else:
            print(param+ "ism")