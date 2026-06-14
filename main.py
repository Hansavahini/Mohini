from datetime import datetime

class Person:
    def __init__(self, name, adhar_id, dob, blood_group,
                 height, weight, email, disability):
        self.name = name
        self.adhar_id = adhar_id
        self.dob = dob          # Format: YYYY-MM-DD
        self.blood_group = blood_group
        self.height = height    # in meters
        self.weight = weight    # in kg
        self.email = email
        self.disability = disability

    # Display all details
    def display_details(self):
        print("Name:", self.name)
        print("Adhar ID:", self.adhar_id)
        print("DOB:", self.dob)
        print("Blood Group:", self.blood_group)
        print("Height:", self.height, "m")
        print("Weight:", self.weight, "kg")
        print("Email:", self.email)
        print("Disability:", self.disability)

    # Calculate age
    def calculate_age(self):
        birth = datetime.strptime(self.dob, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birth.year
        if (today.month, today.day) < (birth.month, birth.day):
            age -= 1
        return age

    # Calculate BMI
    def calculate_bmi(self):
        bmi = self.weight / (self.height ** 2)
        return round(bmi, 2)

    # Update email
    def update_email(self, new_email):
        self.email = new_email

    # Update weight
    def update_weight(self, new_weight):
        self.weight = new_weight

    # Check if person is adult
    def is_adult(self):
        return self.calculate_age() >= 18

    # Check disability
    def has_disability(self):
        return self.disability.lower() == "yes"

    # Validate email
    def validate_email(self):
        return "@" in self.email and "." in self.email

    # Validate Adhar number
    def validate_adhar(self):
        return self.adhar_id.isdigit() and len(self.adhar_id) == 12

    # String representation
    def __str__(self):
        return (f"Name: {self.name}, Age: {self.calculate_age()}, "
                f"Email: {self.email}, Blood Group: {self.blood_group}")


# Example
p1 = Person(
    "Rahul",
    "123456789012",
    "2003-05-10",
    "O+",
    1.75,
    70,
    "rahul@gmail.com",
    "No"
)

p1.display_details()

print("\nAge:", p1.calculate_age())
print("BMI:", p1.calculate_bmi())
print("Is Adult:", p1.is_adult())
print("Has Disability:", p1.has_disability())
print("Email Valid:", p1.validate_email())
print("Adhar Valid:", p1.validate_adhar())

p1.update_email("rahul123@gmail.com")
p1.update_weight(72)

print("\nAfter Update:")
print(p1)