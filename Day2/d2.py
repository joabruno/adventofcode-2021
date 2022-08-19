from util import *

sys.stdin = open(__file__.replace('py', 'in'))

L = list(lines())

hori_pos = 0
aim = 0
depth = 0
for l in L:
    line = l.split()
    if line[0] == "forward":
        hori_pos += int(line[1])
        depth += aim*int(line[1])
    elif line[0] == "up":
        aim -= int(line[1])
    elif line[0] == "down":
        aim += int(line[1])
print(hori_pos * depth)