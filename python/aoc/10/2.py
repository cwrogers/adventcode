#! /usr/bin/python3
from aoc.common import adj4

with open("input.txt", "r") as file:
    lines = file.read().strip().split('\n')


def getScore(x, y):
    d = lines[x][y]
    if d == '9':
        print("found 9")
        return 1
    score = 0
    for c in adj4:
        nx = x + c[0]
        ny = y + c[1]
        if (ny < 0 or ny >= len(lines)) or (nx < 0 or nx >= len(lines[0])):
            continue
        if(lines[nx][ny] == str(int(d) + 1)):
            score += getScore(x+c[0], y+c[1])
    return score

scores = 0

for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == '0':
            scores += (getScore(y,x))

print(scores)
