#!/usr/bin/python3

import sys
from os.path import exists

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit('Usage: ./markdown2html.py README.md README.html')
    if not exists(sys.argv[1]):
        sys.exit('Missing ' + sys.argv[1])
