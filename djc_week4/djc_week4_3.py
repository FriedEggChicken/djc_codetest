import sys

def dfs(x,y,num_row):
    
    if(len(num_row) == 6):
        if(num_row not in result):
            result.append(num_row)
        return
    
    for k in range(4):
        new_x = x + move_x[k]
        new_y = y + move_y[k]
        if(0<=new_x and new_x<5 and 0<=new_y and new_y<5):
            dfs(new_x,new_y,num_row+board[new_x][new_y])
    
board = []

for i in range(5):
    a,b,c,d,e = sys.stdin.readline().strip().split(" ")
    board.append([a,b,c,d,e])

result = []
move_x = [1,-1,0,0]
move_y = [0,0,1,-1]

for i in range(5):
    for j in range(5):
        dfs(i,j,board[i][j])

print(len(result))
