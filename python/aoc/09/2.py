#! /usr/bin/python3

with open("input.txt", "r") as file:
    s = file.read().strip()


class l_elem:
    size : int = 0
    def __init__(self, size):
        self.size = size
        
class dig(l_elem):
    def __init__(self, size, id):
        super().__init__(size)
        self.id = id

    def __str__(self):
        return str(str(self.id) * self.size)

class space(l_elem):
    def __init__(self, size):
        super().__init__(size)
    def __str__(self):
        return str('.' * self.size)

id = 0
rs = []
for i in range(len(s)):
    d = int(s[i])
    if i % 2 == 0:
        rs += [dig(d, id)]
        id += 1
    else:
        rs += [space(d)]
#print(''.join([str(x) for x in rs]))

front = 0
end = len(rs) - 1
   

while end >= 0: 
    while type(rs[end]) is not dig or front >= len(rs) - 1:
        end -= 1
        front = 0
        continue
    while type(rs[front]) is not space:
        front += 1
        continue
    if type(rs[front]) is space:
        size = rs[front].size
        num = rs[end]
        if num.size > size or front > end:
            front += 1
            continue
        dif = size - num.size
        val = rs.pop(end)
        rs.insert(front, val)
        if dif == 0:
            rs.pop(front+1)
        else:
            rs[front+1].size = dif
            offset = dif
            for i in range(dif):
                offset += rs[front + 1 + i].size
            front += offset
        rs.insert(end, space(num.size))
        end -= 1
        #print(''.join([str(x) for x in rs]))

ss = []
for x in rs:
    if type(x) is dig:
        ss += [x.id] * x.size
    elif type(x) is space:
        ss += ['.'] * x.size

cs = 0

for i in range(len(ss)):
    if ss[i] == '.':
        continue
    cs += i * int(ss[i])

print(cs)
