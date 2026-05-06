
class Employee:

    def __init__(self, name, role):
        self.name = name
        self.role = role

    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)



class Trainer(Employee):

    def __init__(self, name, role, specialization):
        self.name = name
        self.role = role
        self.specialization = specialization

    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)
        print("Specialization:", self.specialization)



class YogaInstructor(Employee):

    def __init__(self, name, role, yoga_style):
        self.name = name
        self.role = role
        self.yoga_style = yoga_style

    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)
        print("Yoga Style:", self.yoga_style)



class MultiTrainer(Trainer, YogaInstructor):

    def __init__(self, name, role, specialization, yoga_style):
        self.name = name
        self.role = role
        self.specialization = specialization
        self.yoga_style = yoga_style

    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)
        print("Specialization:", self.specialization)
        print("Yoga Style:", self.yoga_style)



emp1 = Employee("Rahul", "Manager")

trainer1 = Trainer("Kevin", "Trainer", "Weight Training")

yoga1 = YogaInstructor("Anu", "Yoga Instructor", "Hatha Yoga")

multi1 = MultiTrainer("Arun", "Multi Trainer",
                      "Cardio", "Power Yoga")


# Display details
print("Employee Details")
emp1.display()

print("Trainer Details")
trainer1.display()

print("Yoga Instructor Details")
yoga1.display()

print("Multi Trainer Details")
multi1.display()