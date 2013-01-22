#!/bin/python

import os

s = open("ascii.txt",'r').read()
tokens = []
cur_tok = ""


for i in s:
    cur_tok += i
    if len(cur_tok) == 8:
            tokens.append(cur_tok)
            cur_tok = ""

int_chars = [int(x, 2) for x in tokens]
print(int_chars)
chars = [chr(x) for x in int_chars]

print(chars)

s2 = "".join(chars)
print(s2)

tokens = []
cur_tok = ""
for i in s2:
    cur_tok += i
    if len(cur_tok) == 8:
            tokens.append(cur_tok)
            cur_tok = ""
			
int_chars = [int(x, 2) for x in tokens]
chars = [chr(x) for x in int_chars]

print("".join(chars))
print("\n")

os.system("pause")