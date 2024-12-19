#! /usr/bin/python3
from aoc.common import adj4

with open("input.txt", "r") as file:
    lines = file.read().strip().split('\n')

shapesize = {
}
seen = {}

def calcShape(x, y, h=(-1,-1)):
    if (x, y) in seen:
        return 0
    if h == (-1, -1):
        h = (x, y)
        shapesize[h] = 0
    shapesize[h] += 1
    v = lines[x][y]
    p = 0
    seen[(x, y)] = True
    for c in adj4:
        nx = x + c[0]
        ny = y + c[1]
        if (ny < 0 or ny >= len(lines)) or (nx < 0 or nx >= len(lines[0])):
            p += 1
            continue
        if lines[nx][ny] == v and lines[nx][ny] not in seen:
            p += calcShape(nx, ny, h)
        else:
            p += 1
    return p

    

total = 0
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if (y, x) not in seen:
            perim = calcShape(y,x)
            a = perim * shapesize[(y,x)]
            total += a
            print(lines[y][x], a)

print(total)
