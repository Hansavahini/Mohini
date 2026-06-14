from datetime import datetime

# Parent Class
class Person:
    def __init__(self, name, adhar_id, dob, blood_group,
                 height, weight, email, disability, phone):
        self.name = name
        self.__adhar_id = adhar_id      # Hidden
        self.dob = dob
        self.blood_group = blood_group
        self.height = height
        self.weight = weight
        self.email = email
        self.__disability = disability  # Hidden
        self.phone = phone

    def display_details(self):
        print("Name:", self.name)
        print("DOB:", self.dob)
        print("Blood Group:", self.blood_group)
        print("Height:", self.height)
        print("Weight:", self.weight)
        print("Email:", self.email)
        print("Phone:", self.phone)


# Child Class: Teacher
class Teacher(Person):
    def __init__(self, name, adhar_id, dob, blood_group,
                 height, weight, email, disability, phone,
                 employee_id, subject, salary):

        # Call Parent Class Constructor
        super().__init__(name, adhar_id, dob, blood_group,
                         height, weight, email, disability, phone)

        # Teacher-specific attributes
        self.employee_id = employee_id
        self.subject = subject
        self.salary = salary

    def display_teacher_details(self):
        self.display_details()
        print("Employee ID:", self.employee_id)
        print("Subject:", self.subject)
        print("Salary:", self.salary)


# Creating Teacher Object
t1 = Teacher(
    name="Anita Sharma",
    adhar_id="123456789012",
    dob="10-05-1990",
    blood_group="B+",
    height=1.65,
    weight=58,
    email="anita@gmail.com",
    disability="None",
    phone="9876543210",
    employee_id="EMP101",
    subject="Python Programming",
    salary=50000
)

# Display Details
t1.display_teacher_details()