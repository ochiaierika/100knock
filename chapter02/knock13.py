#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'erika.ochiai'

import os


def merge_column_files():
    data_path = os.path.expanduser('~/research/practice/100knock/data')
    output_file = data_path + '/merge_columns.txt'
    file1 = data_path + '/col1.txt'
    file2 = data_path + '/col2.txt'

    with open(output_file, 'w') as fw,\
            open(file1, 'r') as f1,\
            open(file2, 'r') as f2:
        column1 = f1.readline()
        column2 = f2.readline()
        # This part will skip if file1 or file2 finish.
        while column1 and column2:
            fw.write('{}\t{}\n'.format(column1.rstrip(), column2.rstrip()))
            column1 = f1.readline()
            column2 = f2.readline()

if __name__ == '__main__':
    merge_column_files()
