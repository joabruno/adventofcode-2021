#! /usr/bin/env pypy3
from util import *

sys.stdin = open(__file__.replace('py', 'in'))
input = sys.stdin.readline

order = input().split(",")
order = [int(s) for s in order]
boards = []
curr_line = []
while True:
    new = input()
    if new == "s":
        break
    if len(new) < 2:
        boards.append(curr_line)
        curr_line = []
        continue
    new = new.split()
    new_i = [int(s) for s in new]
    curr_line.append(new_i)

boards = boards[1:]
winning_board = 0
def check_for_winner():
    winning_boards = []
    for i, b in enumerate(boards):
        if len(b) < 1:
            continue
        for row in b:
            if sum(row)== -5:
                print("winner board is number: ", i)
                print(b)
                winning_boards.append(i)
        for column in range(len(b[0])):
            if sum([c[column] for c in b]) == -5:
                print("winner board is number: ", i) 
                print(b)
                winning_boards.append(i)
    return winning_boards


for o in order:
    for b_index, b in enumerate(boards):
        if len(b) < 1:
            continue
        for r_index,row in enumerate(b):
            boards[b_index][r_index] = [-1 if x == o else x for x in row]
    winning_boards = check_for_winner()
    if  len(winning_boards) > 0:
        winning_number = o
        winning_board = winning_boards[-1]
        if sum([1 for c in boards if c != []]) == 1:
                break
        for wb in winning_boards:    
            boards[wb] = []
        
    #print(len(boards))
print(winning_board)
print(boards)
print(sum([sum([x for x in r if x != -1]) for r in boards[winning_board]])* winning_number)