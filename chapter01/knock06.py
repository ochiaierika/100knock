#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'erika.ochiai'


def n_gram(target, n=2):
    return [target[i:i+n]for i in range(len(target)-1)]

def has_target_word(target_set, target_word):
    if target_word in target_set:
        print('{} is in {}.'.format(target_word, target_set))
    else:
        print('{} is not in {}.'.format(target_word, target_set))

if __name__ == '__main__':
    x_word, y_word = 'paraparaparadise', 'paragraph'
    target_bigram = 'se'

    x = set(n_gram(x_word))
    y = set(n_gram(y_word))

    print(x.union(y))
    print(x.difference(y))
    print(y.difference(x))
    print(x.intersection(y))

    has_target_word(x, target_bigram)
    has_target_word(y, target_bigram)
