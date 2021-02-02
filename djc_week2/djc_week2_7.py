import sys

N = int(sys.stdin.readline())
people = []
if(2<=N and N<=50):
    for i in range(N):
        weight,height = map(int,sys.stdin.readline().split(" "))
        if((10<=weight and weight<=200) and (10<=height and height<=200)):
            people.append([weight,height])

rank = [1]*N

for j in range(N):
    for k in range(N):
        if(people[j][0]<people[k][0] and people[j][1]<people[k][1]):
            rank[j] += 1
for i in range(N):
    print(rank[i])