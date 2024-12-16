#! /usr/bin/python3

from aoc.common import *

with open("input.txt", "r") as file:
    lines = file.read().strip().split('\n')

count = 0
for y in range(len(lines)):
    for x in range(len(lines[y])):
        l = lines[y][x]
        if l != "A":
            continue
        checks = {}

        if x == 0 or x == len(lines[y]) or y == 0 or y == len(lines):
            continue

        try:
            tl = lines[y-1][x-1]
            tr = lines[y-1][x+1]
            bl = lines[y+1][x-1]
            br = lines[y+1][x+1]
            
            top = list(filter(lambda x: x in ["M", "S"], [tl, tr]))
            btm = list(filter(lambda x: x in ["M", "S"], [bl, br]))
            lft = list(filter(lambda x: x in ["M", "S"], [tl, bl]))
            rgt = list(filter(lambda x: x in ["M", "S"], [tr, br]))


            for i in [lft, rgt]:
                assert len(i) == 2
    
            if (lft == rgt and btm != top) or (btm == top and lft != rgt):
                count += 1

        except:
            pass

print(count)

