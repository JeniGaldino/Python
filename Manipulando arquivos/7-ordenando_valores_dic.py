courses = []
with open("dados/courses.csv", encoding="utf-8") as file:
    for line in file:
        name, category = line.rstrip().split(",")
        course = {}
        course["name"] = name
        course["category"] = category
        courses.append(course)
print(courses)

def get_name(courses):
    return courses["name"]

def get_category(courses):
    return courses["category"]

for course in sorted(courses, key=get_name): #sozinho não funciona porque precisa de uma chave, ou seja, temos que riar uma função
    print(f"{course['name']} -{course['category']}")