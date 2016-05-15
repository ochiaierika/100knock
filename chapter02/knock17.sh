#!/usr/bin/env bash

cd ~/research/practice/100knock/data/

# confirm result was same as knock17.py
cut -f1 hightemp.txt | sort | uniq