#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'erika.ochiai'


def odd_characters(target):
    return target[::2]


if __name__ == '__main__':
    target = u'パタトクカシーー'
    print(odd_characters(target))
