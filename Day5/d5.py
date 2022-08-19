#! /usr/bin/env pypy3
from util import *
import numpy as np

sys.stdin = open(__file__.replace('py', 'in'))
input = sys.stdin.readline

instructions = []
while True:
    newline = input()
    if newline == "end":
        break
    newline = newline.replace("->", " ")
    newline = newline.replace(",", " ")
    newline = newline.split()
    instructions.append([int(x) for x in newline])
    #print(newline)
nparray = np.zeros((1000,1000))
for i in instructions:
    if i[0] == i[2]:
        if i[1] >= i[3]:
            for j in range(abs(i[1]- i[3])+1):
                nparray[i[3]+j][i[0]] += 1
        else:
            for j in range(abs(i[1]- i[3])+1):
                nparray[i[1]+j][i[0]] += 1
                
    if i[1] == i[3]:
        if i[0] >= i[2]:
            for j in range(abs(i[0]- i[2])+1):
                nparray[i[1]][i[2]+j] += 1
        else:
            for j in range(abs(i[0]- i[2])+1):
                nparray[i[1]][i[0]+j] += 1
    if abs(i[1]- i[3]) == abs(i[0]- i[2]):
        if i[1]>= i[3]:
            if i[0]>= i[2]:
                for j in range(abs(i[1]- i[3])+1):
                    nparray[i[3]+j][i[2]+j] += 1
            else:
                for j in range(abs(i[1]- i[3])+1):
                    #print(i[0]+abs(i[1]- i[3]))
                    nparray[i[3]+j][i[2]-j] += 1
        else:
            if i[0]>= i[2]:
                for j in range(abs(i[1]- i[3])+1):
                    nparray[i[2]+j][i[3]-j] += 1
            else:
                for j in range(abs(i[1]- i[3])+1):
                    nparray[i[1]+j][i[0]+j] += 1
        #diagonal

s = 0


print(nparray)
for row in nparray:
    s += sum([1 if x > 1 else 0 for x in row])
print(s)