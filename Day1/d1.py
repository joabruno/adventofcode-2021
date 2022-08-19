from util import *

sys.stdin = open(__file__.replace('py', 'in'))

L = list(ints())


biggers = 0
before = -1
for index, newin in enumerate(L):
    newsum = sum(L[index:index+3])
    if before == -1:
        before = newsum
        continue
    if newsum > before:
        biggers +=1
        print("increased")
    
    before = newsum
print(biggers)