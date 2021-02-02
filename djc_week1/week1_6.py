bf = "BWBWBWBW"
wf = "WBWBWBWB"

black_f = [bf,wf,bf,wf,bf,wf,bf,wf]
white_f = [wf,bf,wf,bf,wf,bf,wf,bf]

n,m = map(int,input().split(" "))
board = []
minn = float('inf')
for a in range(n):
    board.append(input())
for i in range(n-7):
    for j in range(m-7):
        count = 0
        for k in range(8):
            for l in range(8):
                if(board[i+k][j+l] != black_f[k][l]):
                    count += 1
        minn = min(minn,count)
        count = 0
        for k in range(8):
            for l in range(8):
                if(board[i+k][j+l] != white_f[k][l]):
                    count += 1
        minn = min(minn,count)
print(minn)
    