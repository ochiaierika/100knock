#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'erika.ochiai'


def n_gram(target, n=2):
    return [target[i:i+n]for i in range(len(target)-1)]

if __name__ == '__main__':
    sentence = 'I am an NLPer'
    print(n_gram(sentence))
    print(n_gram(sentence.split(' ')))
