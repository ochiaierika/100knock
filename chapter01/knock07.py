#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'erika.ochiai'


def template_sentence(x, y, z):
    return "{}時の{}は{}".format(x, y, z)

if __name__ == '__main__':
    print(template_sentence(x=12, y="気温", z=22.4))
