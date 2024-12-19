#! /usr/bin/python3

with open("input.txt", "r") as file:
    line = list(map(lambda x: int(x), file.read().strip().split(' ')))

cache = {}

def doRules(d, n, e):
    r = []
    if (d,n) in cache:
        return cache[(d,n)]
    if n == e:
        return 1
    if d == 0:
        r =  [1]
    elif len(str(d)) % 2 == 0:
        nd = list(str(d))
        left = int(''.join(nd[:len(nd)//2]))
        right = int(''.join(nd[len(nd)//2:]))
        r = [left, right]
    else:
        r = [d * 2024]
    c = 0
    for item in r:
        c += doRules(item, n+1, e)
    cache[(d, n)] = c
    return c


rules = line
sum = 0
for i in rules:
    sum += doRules(i, 0, 75)


print(sum)
