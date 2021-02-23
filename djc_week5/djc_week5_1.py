import sys

N,S = map(int,sys.stdin.readline().strip().split(" "))

nums = [*map(int,sys.stdin.readline().split(" "))]

result = [0]

count = 0

for i in nums:
    for j in list(result):
        each_sum = i + j
        result.append(each_sum)
        if(result[-1] == S):

            count += 1
print(count)