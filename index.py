from datetime import datetime
import re

class Person:

    def __init__(self, name, adhar_id, dob, blood_group,
                 height, weight, email, phone, disability):

        self.name = name

        self.__adhar_id = adhar_id
        self.__disability = disability

        self.set_dob(dob)
        self.blood_group = blood_group
        self.set_height(height)
        self.set_weight(weight)
        self.set_email(email)
        self.set_phone(phone)


    def set_email(self, email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(pattern, email):
            self.email = email
        else:
            raise ValueError("Invalid Email")

    def set_phone(self, phone):
        if phone.isdigit() and len(phone) == 10:
            self.phone = phone
        else:
            raise ValueError("Phone number must contain 10 digits")

    def set_height(self, height):
        if height > 0:
            self.height = height
        else:
            raise ValueError("Height must be positive")

    def set_weight(self, weight):
        if weight > 0:
            self.weight = weight
        else:
            raise ValueError("Weight must be positive")

    def set_dob(self, dob):
        try:
            self.dob = datetime.strptime(dob, "%d-%m-%Y")
        except:
            raise ValueError("DOB should be in DD-MM-YYYY format")


    def display_details(self):
        print("Name:", self.name)
        print("DOB:", self.dob.strftime("%d-%m-%Y"))
        print("Blood Group:", self.blood_group)
        print("Height:", self.height)
        print("Weight:", self.weight)
        print("Email:", self.email)
        print("Phone:", self.phone)

    def calculate_age(self):
        today = datetime.today()
        age = today.year - self.dob.year
        if (today.month, today.day) < (self.dob.month, self.dob.day):
            age -= 1
        return age

    def calculate_bmi(self):
        return round(self.weight / (self.height ** 2), 2)

    def update_email(self, new_email):
        self.set_email(new_email)

    def update_weight(self, new_weight):
        self.set_weight(new_weight)

    def is_adult(self):
        return self.calculate_age() >= 18

    # Controlled access to hidden data
    def get_adhar_id(self):
        return self.__adhar_id

    def get_disability(self):
        return self.__disability
    
p = Person(
    "Rahul",
    "12345678901234",
    "15-08-2002",
    "O+",
    1.75,
    40,
    "sakshi@gmail.com",
    "1999876543210",
    "None"
)

p.display_details()
print("Age:", p.calculate_age())
print("BMI:", p.calculate_bmi())
print("Adult:", p.is_adult())
