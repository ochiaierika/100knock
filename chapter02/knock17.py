#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'erika.ochiai'

import sys


def unique_words(input_file):
    words = set()
    with open(input_file, 'r') as f:
        for line in f:
            line = line.rstrip().split('\t')
            words.add(line[0])
    return words

if __name__ == '__main__':
    if len(sys.argv) is not 2:
        print('Please set file name.')
    else:
        unique = unique_words(sys.argv[1])
        for word in sorted(unique):
            print(word)
