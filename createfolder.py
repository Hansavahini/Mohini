import os

# Number of students
n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")

    # Create folder with student's name
    os.makedirs(name, exist_ok=True)

    print("Folder created for:", name)

print("All student folders created successfully.")