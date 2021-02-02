import sys
from collections import deque

N = int(sys.stdin.readline())
quene = deque()

for i in range(N):
    command = sys.stdin.readline().split()
    
    if(command[0] == "push"):
        quene.append(command[1])
    elif(command[0] == "pop"):
        if(len(quene)==0):
            print(-1)
        else:
            print(quene.popleft())
    elif(command[0] == "size"):
        print(len(quene))
    elif(command[0] == "empty"):
        if(len(quene)==0):
            print(1)
        else:
            print(0)
    elif(command[0] == "front"):
        if(len(quene)==0):
            print(-1)
        else:
            print(quene[0])
    else:
        if(len(quene)==0):
            print(-1)
        else:
            print(quene[-1])
