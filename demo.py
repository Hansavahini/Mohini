import csv
import os

class Student:

    def __init__(self, roll_no="", name="", division="", height="", weight="", disability=""):
        self.roll_no = roll_no
        self.name = name
        self.division = division
        self.height = height
        self.weight = weight
        self.disability = disability

    def getValues(self):
        self.roll_no = int(input("Enter Roll No : "))
        self.name = input("Enter Name : ")
        self.division = input("Enter Division : ")
        self.height = input("Enter Height : ")
        self.weight = input("Enter Weight : ")
        self.disability = input("Any Disability (Yes/No) : ")

    def printValues(self):
        print("\nRoll No :", self.roll_no)
        print("Name :", self.name)
        print("Division :", self.division)
        print("Height :", self.height)
        print("Weight :", self.weight)
        print("Disability :", self.disability)

    def getPropertyAsList(self):
        return [
            self.roll_no,
            self.name,
            self.division,
            self.height,
            self.weight,
            self.disability
        ]


def isPrime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


StudentsList = []

# Load old records
if os.path.exists("studentdetails.csv"):
    with open("studentdetails.csv", "r", newline="") as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            s = Student(
                int(row[0]),
                row[1],
                row[2],
                row[3],
                row[4],
                row[5]
            )
            StudentsList.append(s)

# Accept new records
n = int(input("Enter Number of Students : "))

for i in range(n):
    s = Student()
    s.getValues()
    StudentsList.append(s)

# Save all records
with open("studentdetails.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    for s in StudentsList:
        writer.writerow(s.getPropertyAsList())

# Save Prime Roll Number Students
with open("PrimeRollNo.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    for s in StudentsList:
        if isPrime(int(s.roll_no)):
            writer.writerow(s.getPropertyAsList())

# Display all students
print("\nAll Student Records")

for s in StudentsList:
    s.printValues()

print("\nPrime Roll Number students stored in PrimeRollNo.csv")