import sys
from heapq import heappop,heappush
input = sys.stdin.readline

def dijkstra(start):
    heap = []
    heappush(heap,[0,start])
    dp = [float('INF') for i in range(v+1)]
    dp[start] = 0
    while heap:
        weight, vertex = heappop(heap)
        for n_n,n_w in lines[vertex]:
            wei = n_w + weight
            if(dp[n_n]>wei):
                dp[n_n] = wei
                heappush(heap,[wei,n_n])
    return dp

v,e = map(int,input().split(" "))

k = int(input())

lines = [[] for i in range(v+1)]

for i in range(e):
    u, ve, w = map(int,input().split(" "))
    lines[u].append([ve,w]) #목적지, 가중치

dp = dijkstra(k)

for i in range(1,v+1):
    if(dp[i]==float('INF')):
        print('INF')
        continue
    print(dp[i])
    
        
    