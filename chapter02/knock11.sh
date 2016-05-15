#!/usr/bin/env bash


# confirm with sed command
sed s/$'\t'/$' '/g ../data/hightemp.txt

# confirm with tr command
cat ../data/hightemp.txt | tr '\t' ' '

# confirm with expand command
expand -t 1 ../data/hightemp.txt

