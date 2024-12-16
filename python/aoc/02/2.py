#! /usr/bin/python3

with open("input.txt", "r") as file:
    lines = file.read().strip().split('\n')


def isSafe(l):
    di = 0
    prev = l[0]
    for i in range(1, len(l)):
        dif = l[i] - prev
        if dif == 0:
            return False
        aDif = abs(dif)
        nDif = (dif / aDif) 
        if aDif > 3 or (di != 0 and nDif != di):
            return False
        di = nDif
        prev = l[i]
    return True


num_safe = 0
for line in lines:
    s = list(map(lambda x: int(x), list(filter(None, line.strip().split(' ')))))
    if any(isSafe(s[:l] + s[l+1:]) for l in range(len(s))):
        num_safe += 1

print(num_safe)
