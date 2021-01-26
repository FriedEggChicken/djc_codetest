num = int(input())
if(num>=1 and num<=9):
    for i in range(1,10,1):
        print('{} * {} = {}'.format(num,i,num*i))