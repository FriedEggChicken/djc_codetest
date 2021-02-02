n,m = map(int,input().split(" "))
card_num = []
max_sum = []

card_num = [int(x) for x in input().split(" ")]

for j in range(n-2):
    for k in range(j+1,n-1):
        for l in range(k+1,n):
            card_sum = card_num[j] + card_num[k] + card_num[l]
            if(card_sum<=m):
                max_sum.append(card_sum)
print(max(max_sum))