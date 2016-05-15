#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'erika.ochiai'

import sys

def head_lines(input_file, n):
    with open(input_file, 'r') as f:
        count = 0
        for line in f:
            count += 1
            line = line.rstrip()
            print(line)
            if count >= n:
                break


if __name__ == '__main__':
    # TODO: argparse
    if len(sys.argv) is not 3:
        print('Please set file name (and # of lines which you want to show.)')
    else:
        head_lines(sys.argv[1], int(sys.argv[2]))
