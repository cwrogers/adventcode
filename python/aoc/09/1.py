#! /usr/bin/python3

with open("input.txt", "r") as file:
    s = file.read().strip()

id = 0
rs = ""
ss = ""
for i in range(len(s)):
    d = int(s[i])
    if i % 2 == 0:
        rs += (str(id) + ",") * d
        id += 1
    else:
        rs += ".," * d

front = 0
rs = rs.split(",")
rs.pop()
end = len(rs) - 1

while front < end:
    c = False
    while rs[front] != ".":
        front += 1
        c = True
    while rs[end] == ".":
        end -= 1
        c = True
    if c:
        continue
    if rs[front] == '.':
        num = rs[end]
        rs.pop(end)
        rs[front] = num
        rs += ['.']

cs = 0

for i in range(len(rs)):
    if rs[i] == '.':
        continue
    cs += i * int(rs[i])

print(cs)
