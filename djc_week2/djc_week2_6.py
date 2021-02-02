import sys

counts = int(input())
nums = [0 for i in range(10001)]

for i in range(counts):
    nums[int(sys.stdin.readline())] += 1

for j in range(10001):
    for k in range(nums[j]):
        sys.stdout.write(str(j) + "\n")



