frontend = {"Rahul", "Anu", "Meera"}

backend = {"Anu", "Arjun", "Nimal"}

backend.add("Akhil")
frontend.remove("Meera")

print("Students in both courses:")
print(frontend & backend)

print("Students only in Backend:")
print(backend - frontend)

all_students = frontend | backend

print("Total Unique Students:")
print(len(all_students))

courses = {
    "Frontend": len(frontend),
    "Backend": len(backend)
}

print("Course Details:")

for course, count in courses.items():
    print("Course:", course, ", Students:", count)

new_courses = {course: count for course, count in courses.items()}

new_courses["Fullstack"] = courses["Frontend"] + courses["Backend"]

print("New Courses Dictionary:")
print(new_courses)

