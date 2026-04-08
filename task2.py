people = {}

for i in range(5):
    ism = input("Ism kiriting: ")
    yosh = int(input("Yosh kiriting: "))
    people[ism] = yosh

sorted_people = sorted(people.items(), key=lambda x: x[1])

for ism, yosh in sorted_people:
    print(ism, yosh)