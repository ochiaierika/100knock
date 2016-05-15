#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'erika.ochiai'

import sys
import os


def divide_n_files(input_file, n):
    output_file = os.path.expanduser('~/research/practice/100knock/data/knock16')
    with open(input_file, 'r') as f:
        # TODO: change to alphabet. not number
        line_count, file_num = 0, 0
        file_name = '{}_{}.txt'.format(output_file, file_num)
        fw = open(file_name, 'w')
        for line in f:
            if line_count >= n:
                fw.close()
                file_num += 1
                file_name = '{}_{}.txt'.format(output_file, file_num)
                fw = open(file_name, 'w')
                line_count = 0
            fw.write(line)
            line_count += 1
        fw.close()

if __name__ == '__main__':
    if len(sys.argv) is not 2:
        print('Please set file name and # of lines which you want to show.')
    else:
        divide_n_files(sys.argv[1], int(sys.argv[2]))
