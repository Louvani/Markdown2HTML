#!/usr/bin/python3
'''0. Start a script '''

import sys
from os.path import exists

def read_file(filename=""):
    '''function to read a file and keep lines in an array'''
    cp_line = []
    with open(filename, encoding='utf-8') as f:
        for line in f:
            if line[0] == '#':
                headings(line, cp_line)
        return cp_line

def write_file(filename="", cp_line=""):
    ''' function that writes a string to a text file (UTF8)
    and returns the number of characters written'''
    with open(filename, mode='w', encoding='utf-8') as f:
        for line in cp_line:
            f.write(line)

def headings(line, cp_line):
    '''Convert Mark down headings into html headings'''
    level = line.count('#')
    line = line.replace(('#' * level) + ' ', '<h%s>'%(level))
    index = line.find('\n')
    line = line[:index] + '</h%s>'%(level) + line[index:]
    cp_line.append(line)

def unordered(line, cp_line):
    ''' parsing Unordered listing syntax for generating HTML '''

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit('Usage: ./markdown2html.py README.md README.html')
    md_name = sys.argv[1]
    html_name = sys.argv[2]
    if not exists(sys.argv[1]):
        sys.exit('Missing ' + md_name)
    lines = read_file(md_name)
    write_file(html_name, lines)
