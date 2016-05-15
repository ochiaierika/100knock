#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'erika.ochiai'

import sys


def sort_third_column(input_file):
    lines = list()
    with open(input_file, 'r') as f:
        for line in f:
            line = line.rstrip().split('\t')
            lines.append(line)
    return sorted(lines, key=lambda x:x[2], reverse=True)

if __name__ == '__main__':
    if len(sys.argv) is not 2:
        print('Please set file name.')
    else:
        sorted_lines = sort_third_column(sys.argv[1])
        for line in sorted_lines:
            print('\t'.join(line))
