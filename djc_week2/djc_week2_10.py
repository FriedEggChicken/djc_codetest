m,n = map(int,input().split(" "))

i = 1

portion = []

gcd = 1
lcm = 1

while(True):
    if(m%i==0 and n%i==0):
        m = m/i
        n = n/i
        portion.append(i)
        i = 1
    i += 1
    if(i>m or i>n):
        break

for j in range(len(portion)):
    gcd *= portion[j]

lcm = int(gcd*m*n)

print(gcd)
print(lcm)
    