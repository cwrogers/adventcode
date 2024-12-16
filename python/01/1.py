#! /usr/bin/python3

left, right = [], []

with open("input.txt", "r") as file:
    lines = file.read().strip().split('\n')

for line in lines:
    l = list(filter(None, line.strip().split(' ')))
    left.append(int(l[0]))
    right.append(int(l[1]))


left = sorted(left)
right = sorted(right)
td = 0

for i in range(len(left)):
    td += (abs(left[i] - right[i]))

print(td)
