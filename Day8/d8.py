#! /usr/bin/env pypy3
from util import *

sys.stdin = open(__file__.replace('py', 'in'))
input = sys.stdin.readline

ls = list(lines())

patterns = []
outputs = []
for i in ls:
    i = i.split("|")
    patterns.append(i[0])
    outputs.append(i[1])
counter=0
numbers = ["", "", "","" , "", "", "", "","", ""]
sums = 0
for ind, p in enumerate(patterns):
    for c in p.split():
        if len(c) == 7:
            numbers[8] = sorted(c)
        if len(c) == 4:
            numbers[4] = sorted(c)
        if len(c) == 2:
            numbers[1] = sorted(c)
        if len(c) == 3:
            numbers[7] = sorted(c)
    for c in p.split():
        if len(c) == 5:  
            if numbers[1][0] in c and numbers[1][1] in c:
                numbers[3] = sorted(c)
            elif sum([1 for x in numbers[4] if x in c]) == 3:
                numbers[5] = sorted(c)
            else:
                numbers[2] = sorted(c)
        if len(c) == 6 :
            if numbers[1][0] not in c or numbers[1][1] not in c:
                numbers[6] = sorted(c)
            elif numbers[4][0] in c and numbers[4][1] in c and numbers[4][2] in c and numbers[4][3] in c:
                numbers[9] = sorted(c)
            else:
                numbers[0] = sorted(c)
        


    out = ""
    for s in outputs[ind].split():
        out += str(numbers.index(sorted(s)))
    sums += int(out)

print(sums)