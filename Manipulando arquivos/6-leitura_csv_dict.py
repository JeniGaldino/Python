courses = []
with open("dados/couses.csv", encoding="utf-8") as file:
    for line in file:
        name, category = line.rstrip().split(",")
        course = {}
        course["name"] = name
        course["category"] = category
        courses.append(course)
print(courses)

for course in courses:
    print(f"{course['name']} -{course['category']}")