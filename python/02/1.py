#! /usr/bin/python3

with open("input.txt", "r") as file:
    lines = file.read().strip().split('\n')


num_safe = 0
for line in lines:
    l = list(map(lambda x: int(x), list(filter(None, line.strip().split(' ')))))
    di = 0
    prev = l[0]
    safe = True
    for i in range(1, len(l)):
        dif = l[i] - prev
        if dif == 0:
            safe = False
            break
        aDif = abs(dif)
        nDif = (dif / aDif) 
        if aDif > 3 or (di != 0 and nDif != di):
            print("Not Safe", l)
            safe = False
            break
        di = nDif
        prev = l[i]
            
    if safe:
        num_safe += 1

print(num_safe)
