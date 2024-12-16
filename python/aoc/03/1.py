#! /usr/bin/python3
import re
from functools import reduce

regex = re.compile(r"mul\(\d+,\d+\)")

with open("input.txt", "r") as file:
    s = file.read().strip()

def mul(x, y):
    return x * y

sum = 0
for com in [x.group() for x in regex.finditer(s)]:
    sum += reduce(mul, [int(''.join(filter(str.isdigit, d))) for d in com.split(',')])

print(sum)
