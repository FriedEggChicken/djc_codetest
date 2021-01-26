num = int(input())

for i in range(1,num+1,1):
    a,b = input().split(" ")
    if(0<int(a) and int(a)<10 and 0<int(b) and int(b)<10):
        print(int(a)+int(b))