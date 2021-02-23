import sys
from heapq import heappush,heappop
input = sys.stdin.readline

N,M = map(int,input().split(" "))
roads = [[] for i in range(N+1)]

def dijkstra(start):
    heap = []
    heappush(heap,[0,start])
    dp = [float('inf') for i in range(N+1)]
    dp[start] = 0
    while heap:

        weight, num = heappop(heap)
        for n_n, n_w in roads[num]:

            wei = weight + n_w
            if dp[n_n] > wei:
                dp[n_n] = wei
                heappush(heap,[wei,n_n])
    return dp

for i in range(M):
    A_i, B_i = map(int,input().split(" "))
    roads[A_i].append([B_i,1]) # 가중치 1
    roads[B_i].append([A_i,1])

dp = dijkstra(1)
max_dp = max(dp[1:])

print(dp.index(max_dp),end=' ')
print(max_dp,end=' ')
print(dp.count(max_dp))

