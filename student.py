from datetime import datetime

class Person:
    def __init__(self, name, adhar_id, dob, blood_group, height, weight, email, disability, phone):
        self.name = name
        self.__adhar_id = adhar_id      
        self.dob = dob
        self.blood_group = blood_group
        self.height = height
        self.weight = weight
        self.email = email
        self.__disability = disability  
        self.phone = phone

    def display_details(self):
        print("Name:", self.name)
        print("DOB:", self.dob)
        print("Blood Group:", self.blood_group)
        print("Height:", self.height, "m")
        print("Weight:", self.weight, "kg")
        print("Email:", self.email)
        print("Phone:", self.phone)

    def calculate_age(self):
        birth = datetime.strptime(self.dob, "%d-%m-%Y")
        today = datetime.today()
        age = today.year - birth.year
        if (today.month, today.day) < (birth.month, birth.day):
            age -= 1
        return age

    def calculate_bmi(self):
        return round(self.weight / (self.height ** 2), 2)

    def is_adult(self):
        return self.calculate_age() >= 18


class Student(Person):
    def __init__(self, name, adhar_id, dob, blood_group, height, weight,
                 email, disability, phone, div, roll_number):
        super().__init__(name, adhar_id, dob, blood_group,
                         height, weight, email, disability, phone)

        self.div = div
        self.roll_number = roll_number

    def display_student_details(self):
        self.display_details()
        print("Division:", self.div)
        print("Roll Number:", self.roll_number)

s1 = Student(
    name="Rahul",
    adhar_id="123456789012",
    dob="15-08-2005",
    blood_group="O+",
    height=1.72,
    weight=65,
    email="rahul@gmail.com",
    disability="None",
    phone="9876543210",
    div="A",
    roll_number=25
)

s1.display_student_details()

print("Age:", s1.calculate_age())
print("BMI:", s1.calculate_bmi())
print("Adult:", s1.is_adult())