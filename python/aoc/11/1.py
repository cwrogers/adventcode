#! /usr/bin/python3

with open("input.txt", "r") as file:
    line = list(map(lambda x: int(x), file.read().strip().split(' ')))


def doRules(s):
    print(s)
    i = 0
    while True:
        if i >= len(s):
            break
        d = s[i]
        if d == 0:
            s[i] = 1
        elif len(str(d)) % 2 == 0:
            nd = list(str(d))
            left = int(''.join(nd[:len(nd)//2]))
            right = int(''.join(nd[len(nd)//2:]))
            s.insert(i , right)
            s.insert(i , left)
            s.pop(i+2)
            i += 1
        else:
            s[i] *= 2024
        i += 1
    print(s)
    return s

rules = line
for i in range(25):
    rules = doRules(rules)

print(len(rules))
