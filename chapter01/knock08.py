#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'erika.ochiai'


def cipher(string):
    return ''.join([chr(219-ord(char)) if char.islower() else char for char in string])


if __name__ == '__main__':
    word = '12Adfd34'
    # print encrypted/decrypted words
    print(cipher(word))
    print(cipher(cipher(word)))
