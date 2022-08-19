from itertools import count
from util import *
import numpy as np
sys.stdin = open(__file__.replace('py', 'in'))
input = sys.stdin.readline


opens = ["(", "[", "{", "<"]
closes = [")", "]", "}", ">"]
space = 1
ls = list(lines())
ilegals = []
endings = []
def some(l):
    for i, c in enumerate(l):
        x = len(l)
        if i >= len(l)-1 and c in opens:
            endings.append(l)
            return
        if c in opens:
            continue
        else:
            if l[i-1] in opens:
                if opens.index(l[i-1]) == closes.index(c):
                    l = l[:i-1] + l[i+1:]
                    some(l)
                    return
                else:
                    ilegals.append(c)
                    return
            else:
                    ilegals.append(c)
                    return
for line in ls:
    some(line)
# s =0
# for d in ilegals:
#     if d == "}":
#         s += 1197
#     if d == ")":
#         s+= 3
#     if d == "]":
#         s+= 57
#     if d == ">":
#         s+= 25137
#print(s)
#print(endings)
sums = []
for e in endings:
    s = 0
    rev_closes = [closes[opens.index(o)] for o in reversed(e)]
    #print(rev_closes)
    for rc in rev_closes:
        s *= 5
        s += closes.index(rc)+1
    sums.append(s)
print(sorted(sums)[len(sums)//2])
