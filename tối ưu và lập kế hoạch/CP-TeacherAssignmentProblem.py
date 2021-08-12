import numpy as np
from numpy.lib.npyio import load 
import pandas as pd
#from ortools.linear_model import pywraplp
from ortools.sat.python import cp_model

import time
start= time.time()
f = open("data/input/3.txt", "r")
Lines = f.readlines()
count = 0
# Strips the newline character
n,m = list(map(int,Lines[0].strip().split(" ")))
print("giá trị m,n là {} và {}".format(m,n))
canAssignment = np.zeros([m,n])

d = list(map(int,list(map(float,Lines[1].strip().split(" ")))))
t = list(map(int,list(map(float,Lines[2].strip().split(" ")))))
#print(d)
for i in range(n):
    h = list(map(int,Lines[i+3].strip().split(" ")))
    if h[0]>0:
        for j in h[1:]:
            canAssignment[j][i] = 1
x = []
conflict = [list(map(int,line.strip().split(" "))) for line in Lines[n+3:]]
model = cp_model.CpModel()


for i in range(m):
    mm = []
    for j in range(n):
        mm.append(model.NewIntVar(0, 1, 'x{}{}'.format(i,j)))
    x.append(mm)
z = model.NewIntVar(0, n, 'z')
total_tc = 0
for i in d:
    total_tc =total_tc + i
load = {}
for j in range(m):
    load[j] = model.NewIntVar(0, total_tc, 'load{}'.format(j))


for i in range(m):
    for j in range(n):
        if (canAssignment[i][j] == 0):
            model.Add(x[i][j] == 0)


for i in range(m):
    a = [d[j] * x[i][j] for j in range(n)]
    model.Add(load[i]==sum(a))
for i in range(m):
    model.Add(load[i]<=t[i])


for i in range(n):
    a = [x[j][i] for j in range(m)]
    model.Add(sum(a)<=1)

for i in range(n):
    for j in range(n):
        for k in range(m):
            if i!=j and conflict[i][j]:
                model.Add(x[k][i]+x[k][j]<=1)

kk=[]
for i in range(n):
    for j in range(m):
        kk.append(x[j][i])
model.Add(z==sum(kk))
model.Maximize(z)
end = time.time()
print(end - start)
solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.OPTIMAL:
    print('Solution:')
    print('Objective value =', solver.ObjectiveValue())
else:
    print('The problem does not have an optimal solution.')
end = time.time()
print(end - start)