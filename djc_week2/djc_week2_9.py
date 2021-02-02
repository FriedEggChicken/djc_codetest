import sys

words = sys.stdin.readline().rstrip()
counts = len(words)

for i in range(len(words)-1):
    if(words[i]+words[i+1] == "c="):
        counts -= 1
    elif(words[i]+words[i+1] == "c-"):
        counts -= 1
    elif(words[i]+words[i+1] == "d-"):
        counts -= 1
    elif(words[i]+words[i+1] == "lj"):
        counts -= 1
    elif(words[i]+words[i+1] == "nj"):
        counts -= 1
    elif(words[i]+words[i+1] == "s="):
        counts -= 1
    elif(words[i]+words[i+1] == "z="):
        counts -= 1

for i in range(len(words)-2):
    if(words[i]+words[i+1]+words[i+2] == "dz="):
        counts -= 1

print(counts)
        