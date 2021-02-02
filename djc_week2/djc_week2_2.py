cost = int(input())

rest = 1000 - cost

changes = 0
i = 0

money = [500,100,50,10,5,1]

while(i<6):
    changes = changes + int(rest / money[i])
    rest = rest % money[i]
    i += 1

print(changes)
