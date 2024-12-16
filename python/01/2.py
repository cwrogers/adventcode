#! /usr/bin/python3

left, right = [], []

with open("input.txt", "r") as file:
    lines = file.read().strip().split('\n')

right_map = {}
sim_score = 0

for line in lines:
    l = list(filter(None, line.strip().split(' ')))
    left.append(int(l[0]))
    right.append(int(l[1]))

for d in right:
    if d in right_map:
        right_map[d] += 1
    else:
        right_map[d] = 1


for d in left:
    r = right_map[d] if d in right_map else 0
    sim_score += d * r

print(sim_score)
