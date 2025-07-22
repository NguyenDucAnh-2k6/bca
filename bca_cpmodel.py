#PYTHON 
from ortools.linear_solver import pywraplp
import sys
def Input():
  m,n=map(int, input().split()) #Number of teachers and courses
  #List P of courses compatible with teachers
  P=[[0 for j in range(n+1)] for i in range(m+1)]
  for i in range(1,m+1):
    #Input a row
    row=[int(x) for x in input().split()]
    for j in range(1, len(row)):
      P[i][row[j]]=1 #Update courses that teacher i can teach
  #Number of conflict courses
  K=int(input())
  B=[]
  for k in range(K):
      i, j= map(int, input().split())
    
      B.append([i,j])
  return m,n,P,B
m,n,P,B=Input()

solver=pywraplp.Solver.CreateSolver('SCIP')
INF=solver.infinity()

x={}
for i in range(1,m+1):
  for j in range(1,n+1):
    x[i,j]=solver.IntVar(0,1,'x('+str(i)+','+str(j)+')')
z=solver.IntVar(0,n,'z')
for i in range(1,m+1):
  for j in range(1,n+1):
    if P[i][j]==0:
      c=solver.Constraint(0,0)
      c.SetCoefficient(x[i,j],1)
for j in range(1, n+1):
  c=solver.Constraint(1,1)
  for i in range(1,m+1):
    c.SetCoefficient(x[i,j], 1)
for [j1, j2] in B:
  for i in range(1, m+1):
    #x[i,j1]+x[i,j2]<=1
    #c=solver.Constraint(0,1)
    #c.SetCoefficient(x[i,j1],1)
    #c.SetCoefficient(x[i, j2],1)
    solver.Add(x[i,j1]+x[i,j2]<=1)
for i in range(1,m+1):
  c=solver.Constraint(-INF, 0)
  #for j in range(1, n+1):
  #  c.SetCoefficient(x[i,j],1)
  #c.SetCoefficient(z,-1)
  solver.Add(solver.Sum([x[i,j] for j in range(1, n+1)])-z<=0)

obj=solver.Objective()
obj.SetCoefficient(z,1)
obj.SetMinimization()

status=solver.Solve()
if status == pywraplp.Solver.OPTIMAL:
  print(int(solver.Objective().Value()))
else:
  print(-1)
