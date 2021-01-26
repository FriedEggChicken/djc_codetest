num = int(input())

height = []
weight = []
people = []
if(2<= num and num <=50):
    for i in range(num):
        a,b = input().split(" ")
        if(10 <= int(a) and int(a)<=200 and 10<=int(b) and int(b)<=200):
            weight.append(int(a))
            height.append(int(b))
            people.append([int(a),int(b)])
            people2 = [a for a in range(num)]
    for j in range(0,num):
        g = 1
        for k in range(0,num):
            if(people[j][0]<people[k][0] and people[j][1]<people[k][1]):
                g += 1
            people2[j] = g
for i in range(num):
    print(people2[i], end=" ")