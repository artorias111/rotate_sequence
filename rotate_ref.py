#!/usr/bin/env python3

import argparse

import sys

parser = argparse.ArgumentParser()
parser.add_argument('--ref', type = str, required=True)
parser.add_argument('--pos', type = int, required = True)
args = parser.parse_args()

ref_fasta = args.ref
rotate_pos = args.pos

char_count = 0
new_str = '' # new string that's gonna be your rotated circular genome
header = ''

f = open(ref_fasta, 'r')
for i in f:
    i = i.strip()
    if i == '':
        continue
    if i[0] == '>':
        header = i
    else:
        new_str += i
f.close()

left = new_str[:rotate_pos]
right = new_str[rotate_pos:]

print('rotated sequence:', file = sys.stderr)
print(right+'\n'+left, file = sys.stderr)


sys.stdout.write(header+' rotated\n')
sys.stdout.write(right+left+'\n')
