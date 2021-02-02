N = int(input())
people = []

for i in range(N):
    age,name = input().split(" ")
    age = int(age)
    people.append([age,name])
people.sort(key = lambda student:student[0])

# =============================================================================
# for j in range(N):
#     for k in range(j+1,N):
#         if(people[j][0]>people[k][0]):
#             change = people[j]
#             people[j] = people[k]
#             people[k] = change
#         elif(people[j][2]>people[k][2]):
#             change = people[j]
#             people[j] = people[k]
#             people[k] = change
# =============================================================================
            
for student in people:
    print("{} {}".format(student[0],student[1]))