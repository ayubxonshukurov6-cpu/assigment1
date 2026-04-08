def combine_data(names, scores):
    return list(zip(names, scores))

def get_passed_students(names, scores):
    return list(filter(lambda x: x[1] >= 60, zip(names, scores)))

def show_students(students):
    for name, score in students:
        print(f"{name}: {score} ball")

# Misol
names = ["Ali", "Vali", "Gulbahor", "Dilshod"]
scores = [55, 70, 90, 45]

students = combine_data(names, scores)
print("Barcha talabalar:")
show_students(students)
print("\nO‘tgan talabalar:")
show_students(get_passed_students(names, scores))