#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'erika.ochiai'


def alternation(first, second):
    return ''.join([f + s for f, s in zip(first, second)])

if __name__ == '__main__':
    first_word, second_word = u'パトカー', u'タクシー'
    print(alternation(first_word, second_word))
