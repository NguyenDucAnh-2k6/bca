def Input(): #Gathering inputs
    m,n=map(int, input().split()) #Enter m and n
    P=[set() for j in range(n+1)] #Set of teachers suitable for course j
    for i in range(1,m+1):  #Input lines - number of compatible subjects + subject list
      row=[int(x) for x in input().split()]
      for j in range(1,len(row)):
        P[row[j]].add(i)
    K=int(input()) #Number of conflicting pairs
    conflict=[[False for i in range(n+1)] for j in range(n+1)] #List of conflicting pairs
    for i in range(K):
      i,j=map(int, input().split())
      conflict[i][j]=True
      conflict[j][i]=True   
    return m,n,P,K,conflict
def inputfile(filename):
    with open(filename, 'r') as f:
        [m,n]=[int(x) for x in f.readline().split()]
        P=[set() for _ in range(n+1)]
        for i in range(1,m+1):
            row=[int(x) for x in f.readline().split()]
            for j in range(len(row)):
                P[row[j]].add(i)
        [K]=[int(x) for x in f.readline().split()] 
        conflict=[[False for i in range(n+1)] for j in range(n+1)]
        for _ in range(K):
            [i,j]=[int(x) for x in f.readline().split()]
            conflict[i][j]=True
            conflict[j][i]=True
    return m,n,P,K,conflict
#m,n,P,K,conflict=Input()  
m,n,P,K,conflict=inputfile('BCA data.txt')
x=[0 for j in range(n+1)] #Sol representation
load=[0 for i in range(m+1)] #Compute load
best_assign=[0 for _ in range(n+1)]
def check(v,k): #Check if teacher v can be assigned to course k
    for j in range(1,k):
      if conflict[j][k] and v==x[j]:
        return False
    return True 
def Sol(): #Checking min and max of load
    global best, best_assign
    maxload=max(load)
    if maxload < best:
      best=maxload
      best_assign[:]=x[:]
def Try(k):
    for v in P[k]: #Browse through teachers can be assigned with course k
       if check(v,k):
          x[k]=v
          load[v]+=1 #Update our data structure
          if k==n:
             Sol()
          else:
             if load[v]<best:
                Try(k+1)
          load[v]-=1
best=1e9
Try(1)
print("Minimal max load: ", best)
# Print optimal assignments
print("\nOptimal Course Assignments:")
for i in range(1,m+1):
    print("Teacher ",i, "will teach courses: ")
    for j in range(1,n+1):
       if best_assign[j]==i:
          print(j, end=' ')
    print()      


    