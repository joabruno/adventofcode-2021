#! /usr/bin/env pypy3
from util import *
import numpy as np
sys.stdin = open(__file__.replace('py', 'in'))
input = sys.stdin.readline

def find_adj_indeces(index_row, index_column, nparr):
    adj =[]
    if index_row == 0 and index_column == 0:
        adj.append((index_row+1,index_column))
        adj.append((index_row,index_column+1))
    elif index_row == len(nparr)-1 and index_column == len(row)-1:
        adj.append((index_row-1,index_column))
        adj.append((index_row,index_column-1))
    elif index_row == 0 and index_column == len(row)-1:
        adj.append((index_row+1,index_column))
        adj.append((index_row,index_column-1))
    elif index_row == len(nparr)-1 and index_column == 0:
        adj.append((index_row-1,index_column))
        adj.append((index_row,index_column+1))
    elif index_row == 0 and not index_column == len(row)-1:
        adj.append((index_row+1,index_column))
        adj.append((index_row,index_column+1))
        adj.append((index_row,index_column-1))
    elif index_column == 0 and not index_row == len(nparr)-1:
        adj.append((index_row+1,index_column))
        adj.append((index_row,index_column+1))
        adj.append((index_row-1,index_column))
    elif index_row == len(nparr)-1:
        adj.append((index_row-1,index_column))
        adj.append((index_row,index_column-1))
        adj.append((index_row,index_column+1))
    elif index_column == len(row)-1:
        adj.append((index_row-1,index_column))
        adj.append((index_row,index_column-1))
        adj.append((index_row+1,index_column))
    else:
        adj.append((index_row+1,index_column))
        adj.append((index_row-1,index_column))
        adj.append((index_row,index_column+1))
        adj.append((index_row,index_column-1))
    return adj


ls = list(lines())
nparr = np.zeros((len(ls), len(ls[0])))
for i, j in enumerate(ls):
    for a,b in enumerate(j):
        nparr[i][a] = int(b)
lowerthanadj =[]
for index_row, row in enumerate(nparr):
    for index_column, column in enumerate(row):
        adj = find_adj_indeces(index_row, index_column, nparr)
        if all(nparr[x][y] > nparr[index_row][index_column] for (x,y) in adj):
            lowerthanadj.append([(index_row,index_column)])

candset = lowerthanadj.copy()
basins = lowerthanadj.copy()
while not all(len(x) == 0 for x in candset):
    templistlist = []
    for i, c in enumerate(candset):
        templist = []
        for ind in c:
            adj = find_adj_indeces(ind[0], ind[1], nparr)
            for a in adj:
                if nparr[a[0]][a[1]] == 9:
                    continue
                if nparr[ind[0]][ind[1]] < nparr[a[0]][a[1]]:
                    templist.append(a)
        basins[i] = basins[i] + templist
        templistlist.append(templist)
        candset = templistlist
        

for i, b in enumerate(basins):
    res = []
    [res.append(x) for x in b if x not in res]
    basins[i] = res

print(np.prod(sorted([len(x) for x in basins])[-3:]))