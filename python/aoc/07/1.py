#! /usr/bin/python3
import itertools

with open("input.txt", "r") as file:
    lines = file.read().strip().split('\n')

ops = ['+', '*']
sum = 0
for line in lines:
    l = line.split(':')
    target = int(l[0])
    nums = list(map(lambda x: int(x),l[1].strip().split(' ')))
    for opl in list(itertools.product(ops, repeat=len(nums) - 1)):
        t = nums[0]
        for n in range(1,len(nums)):
            if opl[n-1] == '+':
                t += nums[n]
            elif opl[n-1] == '*':
                t *= nums[n]
        if t == target:
            sum += target
            break


print(sum)
