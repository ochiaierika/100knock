#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'erika.ochiai'


import sys

def tab_to_space(input_file):
    with open(input_file, 'r') as f:
        for line in f:
            print(line.rstrip().replace('\t', ' '))

if __name__ == '__main__':
    if len(sys.argv) is 2:
        tab_to_space(sys.argv[1])
