import sys

def dfs(row,column):
    bug = 0
    for i in range(row):
        for j in range(column):
            if(field[j][i] == 1):
                field[j][i] = 0
                bug += 1
                move = [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]
                while move:
                    x,y = move.pop()
                    if(0<=y and y<N and 0<=x and x<M):
                        if(field[y][x] == 1):
                            field[y][x] = 0
                            move.append([x,y+1])
                            move.append([x,y-1])
                            move.append([x+1,y])
                            move.append([x-1,y])
                            
    return bug           
    
T = int(sys.stdin.readline())

for i in range(T):
    M, N, k = map(int,sys.stdin.readline().split(" "))
    
    field = [[0 for a in range(M)] for j in range(N)]
    
    for j in range(k):
        x, y = map(int,sys.stdin.readline().split(" "))
        field[y][x] = 1
    
    print(dfs(M,N))
    
    
        

    

