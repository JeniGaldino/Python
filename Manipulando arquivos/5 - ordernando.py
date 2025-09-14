courses = []

with open("dados/couses.csv", "r", encoding="utf-8") as file:
    for line in file:
        language, category = line.rstrip().split(",")
        courses.append(f"{language}-{category}")
        print(courses)
        
for courses in sorted(courses):
    print(courses)