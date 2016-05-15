#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'erika.ochiai'

import os


def divide_columns():
    data_path = os.path.expanduser('~/research/practice/100knock/data')
    input_file = data_path + '/hightemp.txt'
    file1 = data_path + '/col1.txt'
    file2 = data_path + '/col2.txt'

    with open(input_file, 'r') as f,\
            open(file1, 'w') as fw1,\
            open(file2, 'w') as fw2:
        for line in f:
            # this time input file is fixed so didn't add any validation like length
            line = line.rstrip().split('\t')
            fw1.write('{}\n'.format(line[0]))
            fw2.write('{}\n'.format(line[1]))


if __name__ == '__main__':
    divide_columns()
