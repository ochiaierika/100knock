#!/usr/bin/env bash

cd ~/research/practice/100knock/

# confirm whether these characters are same as in col1.txt
cat data/hightemp.txt | cut -f 1

# confirm whether these characters are same as in col2.txt
cat data/hightemp.txt | cut -f 2
