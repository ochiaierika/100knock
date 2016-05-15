#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'erika.ochiai'

import re


def word_length(target_line):
    return [len(word) for word in re.sub(r'[,.]', '', target_line).split(' ')]

if __name__ == '__main__':
    sentence = u'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
    print(word_length(sentence))
