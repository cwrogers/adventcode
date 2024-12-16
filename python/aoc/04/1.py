#! /usr/bin/python3

from aoc.common import *

with open("input.txt", "r") as file:
    lines = file.read().strip().split('\n')

count = 0
for y in range(len(lines)):
    for x in range(len(lines[y])):
        l = lines[y][x]
        checks = {}
        for i in range(1,4):
            for ax,ay in adj8:
                if (ax,ay) not in checks:
                    checks[(ax,ay)] = l
                try:
                    nx = x + ax * i
                    ny = y + ay * i
                    if nx < 0 or nx > len(lines[y]) or ny < 0 or ny > len(lines):
                        continue
                    checks[(ax,ay)] += lines[ny][nx]
                except Exception as e:
                    continue

        count += len(list(filter(lambda x: x == "XMAS", checks.values())))

print(count)

