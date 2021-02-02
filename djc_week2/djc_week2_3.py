N = int(input())

for i in range(N):
    N_str = str(i)
    s_sum = 0
    for j in range(len(N_str)):
        s_sum += int(N_str[j])
    if(N == i+s_sum):
        creator = i
        break
    if(i == N-1):
        creator = 0
print(creator)