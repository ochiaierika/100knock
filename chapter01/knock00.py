#!/usr/bin/env python
# -*- coding: utf-8 -*-

def reverse_string(target):
    return target[::-1]

if __name__=='__main__':
    target = 'stressed'
    result = reverse_string(target)
    print(result)