#! /usr/bin/python3
from typing import Tuple

with open("input.txt", "r") as file:
    imap = file.read().strip().split('\n')

dirs = [(0, -1),
        (1, 0),
        (0, 1),
        (-1, 0)]

def getPos(grid) -> Tuple[int,int]:
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '^':
                return x, y
    return -1, -1

areasBeen = {}

def getNext(pos, grid):
    i = 0
    while True:
        np = (pos[0] + d[0]*i, pos[1] + d[1]*i)
        if np[0] < 0 or np[1] < 0:
            raise Exception
        if grid[np[1]][np[0]] == '#':
            break
        if np in areasBeen:
            if d in areasBeen[np]:
                return -1, -1
            areasBeen[np] += [d]
        else:
            areasBeen[np] = [d]
        i += 1
    return pos[0] + d[0]*(i-1), pos[1] + d[1]*(i-1)

count = 0

for y in range(len(imap)):
    for x in range(len(imap[y])):
        e = False
        di = 0
        d = dirs[0]
        pos = getPos(imap)
        if imap[y][x] != '.':
            continue
        line = imap[y]
        imap[y] = line[:x] + '#' + line[x+1:]
        areasBeen = {}
        while not e:
            try:
                pos = getNext(pos, imap)
                if pos == (-1, -1):
                    count += 1 
                    break
                di += 1
                d = dirs[di % 4]
            except Exception as err:
                e = True
        imap[y] = line[:x] + '.' + line[x+1:]


print(count)

