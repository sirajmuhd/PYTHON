import os

filename = "students.txt"


if os.path.exists(filename):
    print("Existing student names:")

    with open(filename, "r") as file:
        old_names = file.readlines()

        if old_names:
            for name in old_names:
                print(name.strip())
        else:
            print("No names found.")

else:
    print("File does not exist. A new file will be created.")


count = int(input("How many student names do you want to add? "))


with open(filename, "a") as file:
    for i in range(count):
        name = input(f"Enter student name {i+1}: ")
        file.write(name + "\n")

print("\nUpdated student list:")


with open(filename, "r") as file:
    all_names = file.readlines()

    for name in all_names:
        print(name.strip())