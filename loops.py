# loops are used for iterating over a sequence

people = ['john', 'paul', 'sam', 'susan']

# for - break - continue
for person in people:
    if person == 'john':
        continue
    if person == 'sam':
        break
    print(person)

# range
for i in range(len(people)):
    print(people[i])

for i in range(0,10): #(0-9)
    print(i)

# while loop
count = 0
while count <= 10:
    print(count)
    count += 1 # python has no ++ operator
