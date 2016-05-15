#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'erika.ochiai'

import sys


def count_lines(filename):
    count = 0
    with open(filename) as f:
        for line in f:
            count += 1
    return count

if __name__ == '__main__':
    if len(sys.argv) is not 2:
        print('Please input file name which you want to count!')
    else:
        input_file = sys.argv[1]
        print('The number of line is %d.' % count_lines(input_file))
