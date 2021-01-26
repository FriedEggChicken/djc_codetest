num,mvalue = map(int,input().split(" "))
arr = [int(x) for x in input().split(" ")]
sumlist = []
for i in range(0,num-2,1):
    for j in range(i+1,num-1,1):
        for k in range(j+1,num,1):
            sum = arr[i] + arr[j] + arr[k]
            if(mvalue>=sum):
                sumlist.append(sum)
maxone = sumlist[0]
for n in range(1,len(sumlist)):
    if(maxone<sumlist[n]):
        maxone = sumlist[n]
print(maxone)