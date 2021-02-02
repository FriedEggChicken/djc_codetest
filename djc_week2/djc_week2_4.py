words = input()
counts = 0
for i in range(len(words)):   
    if(words[i] == " "):
        counts += 1
if(words[0] == " "):
    counts -= 1
if(words[len(words)-1] == " "):
    counts -= 1
counts += 1

print(counts)