num = int(input())
if(1<=num and num<=1000000):
    for i in range(num):
        a = str(i)
        b = 0
        for j in range(len(a)):
            b += int(a[j])
        if((i + b) == num):
            answer = int(a)
            break
    if(i == num-1):
        answer = 0
print(answer)
