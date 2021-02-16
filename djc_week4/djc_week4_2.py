import sys
from collections import deque

def bfs(person):
    visited[person] = 1
    
    d = deque()
    d.append(person)
    
    while d:
        v = d.popleft()
        for i in family[v]:
            if not visited[i]:
                visited[i] = 1
                count[i] = count[v] + 1
                d.append(i)
                  
n = int(sys.stdin.readline())

family = [[] for i in range(n+1)]

visited = [0 for i in range(n+1)]

count = [0 for i in range(n+1)]

a,b = map(int,sys.stdin.readline().split(" "))

m = int(sys.stdin.readline())

for i in range(m):
    parent,child = map(int,sys.stdin.readline().split(" "))
    family[parent].append(child)
    family[child].append(parent)

bfs(a)
if count[b] == 0:
    print(-1)
else:
    print(count[b])
    

