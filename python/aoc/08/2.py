#! /usr/bin/python3

import itertools


with open("input.txt", "r") as file:
    lines = file.read().strip().split('\n')

antennas = {}

for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] != '.':
            if lines[y][x] in antennas:
                antennas[lines[y][x]] += [(x,y)]
                continue
            antennas[lines[y][x]] = [(x,y)]

ans = {}
for freq in antennas.keys():
    combos = list(itertools.combinations(antennas[freq], 2))
    for c in combos:
        a1 = c[0]
        a2 = c[1]
        d = abs(a1[0] - a2[0]) + abs(a1[1] - a2[1])
        cx = a1[0] - a2[0]
        cy = a1[1] - a2[1] 
        ans[a1] = True
        ans[a2] = True
        while True:
            anti_1 = (a1[0] + cx, a1[1] + cy)
            if anti_1[0] >= 0 and anti_1[0] < len(lines[0]) and \
                    anti_1[1] >= 0 and anti_1[1] < len(lines):
                ans[anti_1] = True
            else:
                break
            a1 = anti_1
        while True:
            anti_2 = (a2[0] - cx, a2[1] - cy)
            if anti_2[0] >= 0 and anti_2[0] < len(lines[0]) and \
                    anti_2[1] >= 0 and anti_2[1] < len(lines):
                ans[anti_2] = True
            else:
                break
            a2 = anti_2

print(len(ans.values()))
