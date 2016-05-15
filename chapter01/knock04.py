#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'erika.ochiai'


def atomic_symbols(line):
    atom_dic = dict()
    first_char = {1, 5, 6, 7, 8, 9, 15, 16, 19}
    for num, word in enumerate(line.split(' '), 1):
        endpoint = 2
        if num in first_char:
            endpoint = 1
        atom_dic[word[:endpoint]] = num
    return atom_dic


if __name__ == '__main__':
    sentence = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. ' \
               'New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
    print atomic_symbols(sentence)
