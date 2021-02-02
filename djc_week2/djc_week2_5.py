import sys

counts = int(input())
nums = []
for i in range(counts):
    nums.append(int(sys.stdin.readline()))

nums.sort()

answer = ""
for i in range(counts):
    answer += str(nums[i]) + "\n"

sys.stdout.write(answer)
