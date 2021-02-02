n = int(input())

num_row = []
stack = []
symbol = []
num_list = []
k=0
answer = 0

for i in range(n):
    num_row.append(int(input()))

for j in range(1,n+1):
    stack.append(j)
    symbol.append("+")
    while(stack and stack[-1] == num_row[k]):
        k += 1
        symbol.append("-")
        num_list.append(stack.pop())
if(len(num_list) == len(num_row)):
    for l in range(n):
        if(num_list[l] != num_row[l]):
            answer = 1
            break
else:
    answer = 1

if(answer == 1):
    print("NO")
else:
    for m in symbol:
        print(m)