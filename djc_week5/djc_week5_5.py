import sys
from heapq import heappop,heappush
input = sys.stdin.readline


def floyd(start): #dijkstra임
    heap = []
    heappush(heap,[0,start])
    dp = [float('inf') for i in range(n+1)]
    dp[start] = 0
    while heap:
        weight,num = heappop(heap)
        for n_n,n_w in roads[num]:
            wei = n_w + weight
            if(dp[n_n]>wei):
                dp[n_n] = wei
                heappush(heap,[wei,n_n])
    return dp

n = int(input())
m = int(input())

roads = [[] for i in range(n+1)]

for i in range(m):
    a,b,c = map(int,input().split(" "))
    roads[a].append([b,c])

for i in range(1,n+1):
    dp = floyd(i)
    dp = dp[1:]
    for j in range(n):
        if(dp[j] == float('inf')):
            dp[j] = 0
    print(*dp)
    
