list = [1, 2, 3, 4, 5]
for i in list:
    j = i * 2
    print(j)


projects = ["'Learn Python", "Learn JavaScript", "Learn C++"]

lower = [project.lower() for project in projects]

print(lower)

person = {
    "name": "Feri",
    "age": 36,
    "country": "Romania",
}

for p in person.items():
    print(f"{p[0]}: {p[1]}")
