#! /usr/bin/python3

with open("input.txt", "r") as file:
    lines = file.read().strip().split('\n')


def checkRule(l, rules):
    for n in l:
        if n in rules:
            matched = list(set(rules[n]) & set(l))
            for r in matched:
                ni = l.index(n)
                rni = l.index(r)
                if not ni < rni:
                    return False
    return True



def fixRules(l, rules):
    ok = l.copy()
    for n in ok:
        if n in rules:
            matched = list(set(rules[n]) & set(ok))
            for r in matched:
                ni = ok.index(n)
                rni = ok.index(r)
                if not ni < rni:
                    p = ok.pop(ni)
                    ok.insert( 0 if rni == 0 else rni-1, p)
    return ok




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
    ok = l.copy()

    if not checkRule(ok, rules):
        while not checkRule(ok, rules):
            ok = fixRules(ok, rules)
        sum += int(ok[len(ok) // 2])

print(sum)

