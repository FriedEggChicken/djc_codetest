import sys
input = sys.stdin.readline # sys.stdin.readline() 로 해주면 출력초과
    
def cases(first,length):
    if(length == 6):
        for i in range(k):
            if(check[i] == 1):
                print(nums[i],end=' ')
        print()
    for i in range(first,k):
        check[i] = 1
        cases(i+1,length+1)
        check[i] = 0
        
while(True):  
    nums = [*map(int,input().split(" "))] 
    k = nums[0]
    nums = nums[1:]
    if(k == 0):
        break
    
    case = []
    check = [0 for i in range(k)]
    cases(0,0)
    print()
        
