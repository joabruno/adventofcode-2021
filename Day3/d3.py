from util import *
import math
sys.stdin = open(__file__.replace('py', 'in'))

L = list(lines())
Lox = L.copy()
Lco = L.copy()
oxy = []
co2 = []
print(7//2)
for i in range(len(Lox[0])):
    for l in Lox:
        if l[i] == "1":
            oxy.append(l)
        else:
            co2.append(l)
    if len(oxy) >= math.ceil(len(Lox) / 2):
        Lox = oxy
        #print(oxy)
    else:
        Lox = co2
        #print(co2)
    if len(Lox) == 1:
        continue
    oxy = []
    co2 = []
print(oxy)
o = oxy[0]
oxy = []
co2 = []
for i in range(len(L[0])):
    for l in Lco:
        if l[i] == "1":
            oxy.append(l)
            print("asdasd")
        else:
            co2.append(l)
    if len(oxy) < math.ceil(len(Lco) / 2):
        Lco = oxy
        print(oxy)
    else:
        Lco = co2
        print(co2)
    if len(Lco) == 1:
        print("fin")
        break
    oxy = []
    co2 = []

c = co2[0]

print(int(o, 2)* int(c, 2))
#int('11111111', 2)