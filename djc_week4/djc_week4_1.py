import sys
from collections import deque

def bfs(a):
    count = 0
    d = deque()
    d.append(a)
    visited[a] = 1 # 1은 True
    while d:
        v = d.popleft()
        count += 1
        for i in computers[v]:
            if not visited[i]:      #True 가 아닐때
                visited[i] = 1
                d.append(i)
    return count

N,M = map(int,sys.stdin.readline().split(" "))

computers = [[] for i in range(N+1)] #N번째 컴퓨터를 위해 N+1

for i in range(M):
    believer, other = map(int,sys.stdin.readline().split(" "))
    computers[other].append(believer) #other안에 believer 넣어줌

results = [0] * (N+1) # N까지하면 리스트 N-1까지만 만들어짐

for i in range(1,N+1):
    visited = [0] * (N+1)
    results[i] = bfs(i)

most_computer = max(results)

for i in range(1,N+1):
    if results[i] == most_computer:
        print(i,end=' ')



    