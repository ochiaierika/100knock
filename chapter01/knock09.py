#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'erika.ochiai'

import random

def typoglycemia(sentence):
    words = list()
    for word in sentence.split(' '):
        if len(word) >= 4:
            contents = list(word[1:-1])
            random.shuffle(contents)
            word = word[0] + ''.join(contents) + word[-1]
        words.append(word)
    return ' '.join(words)


if __name__ == '__main__':
    test_sentence = "I couldn't believe that I could actually understand what I was reading : t" \
                    "he phenomenal power of the human mind ."
    print(typoglycemia(test_sentence))
