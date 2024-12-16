#! /usr/bin/python3
import re
from functools import reduce

regex = re.compile(r"mul\(\d+,\d+\)|do\(\)|don't\(\)")

with open("input.txt", "r") as file:
    s = file.read().strip()

def mul(x, y):
    return x * y

sum = 0
t = 1
for com in [x.group() for x in regex.finditer(s)]:
    match(com):
        case "do()":
            t = 1
        case "don't()":
            t = 0
        case _:
            sum += reduce(mul, [int(''.join(filter(str.isdigit, d))) for d in com.split(',')]) * t

print(sum)
