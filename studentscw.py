python_students = {"Rahul", "Anu", "Arjun"}
data_science_students = {"Anu", "Meera", "Akhil"}

python_students.add("Nimal")
data_science_students.remove("Akhil")

common_students = python_students.intersection(data_science_students)

print("Students in both courses:")
print(common_students)

only_python = python_students.difference(data_science_students)

print("Students only in Python:")
print(only_python)

all_students = python_students.union(data_science_students)

print("All students:")
print(all_students)

courses = {
    "Python": 4,
    "Data Science": 2
}

print("Course Details:")

for course, count in courses.items():
    print("Course:", course, ", Students:", count)

growth = {}

for course, count in courses.items():
    growth[course] = count * 2

print("Expected Growth:")
print(growth)
