import random
import math
N=1000
P=list()
D=list()
for i in range(N):
    P.append(random.uniform(-10e+6,10e+6))
for p_i in P:
    for p_j in P:
        if(p_i!=p_j):
            D.append(abs(p_i-p_j))
dmin=min(D)
print(dmin)