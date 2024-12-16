#! /usr/bin/python3

with open("input.txt", "r") as file:
    lines = file.read().strip().split('\n')

rules = {}
rrules = True
sum = 0
for line in lines:
    if len(line.strip()) == 0:
        rrules = False
        continue

    if rrules:
        r = line.split('|')
        if r[0] in rules:
            rules[r[0]] += [r[1]]
        else:
            rules[r[0]] = [r[1]]
        continue

    l = line.split(',')

    failed = False
    for n in l:
        if n in rules:
            matched = list(set(rules[n]) & set(l))
            for r in matched:
                if not l.index(n) < l.index(r):
                    failed = True
                    break
        if failed:
            break

    if not failed:
        sum += int(l[len(l) // 2])

print(sum)
