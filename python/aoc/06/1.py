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

pos = getPos(imap)
di = 0
d = dirs[0]
areasBeen = {}

def getNext():
    i = 0
    while True:
        np = (pos[0] + d[0]*i, pos[1] + d[1]*i)
        if np[0] < 0 or np[1] < 0:
            raise Exception
        if imap[np[1]][np[0]] == '#':
            break
        areasBeen[np] = True
        i += 1
    return pos[0] + d[0]*(i-1), pos[1] + d[1]*(i-1)

e = False
while not e:
    try:
        pos = getNext()
        print("turning")
        di += 1
        d = dirs[di % 4]
    except:
        e = True




print(len(list(areasBeen.values())))

