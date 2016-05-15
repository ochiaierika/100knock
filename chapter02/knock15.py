#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'erika.ochiai'

import sys


def tail_lines(input_file, n):
    with open(input_file, 'r') as f:
        for line in f.readlines()[-n:]:
            line = line.rstrip()
            print(line)

if __name__ == '__main__':
    if len(sys.argv) <= 2:
        print('Please set file name (and # of lines which you want to show.)')
    else:
        tail_lines(sys.argv[1], int(sys.argv[2]))
