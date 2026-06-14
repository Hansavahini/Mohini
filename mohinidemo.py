import csv

def store_students():
    # Number of students
    n = int(input("Enter number of students: "))

    # Open output files
    with open("boys.csv", "w", newline="") as boysfile, \
         open("girls.csv", "w", newline="") as girlsfile:

        boys_writer = csv.writer(boysfile)
        girls_writer = csv.writer(girlsfile)

        # Write header
        header = ["Roll No", "Name", "Gender", "Division"]
        boys_writer.writerow(header)
        girls_writer.writerow(header)

        # Input student details
        for i in range(n):
            print("\nEnter details of Student", i + 1)

            roll = input("Enter Roll No: ")
            name = input("Enter Name: ")
            gender = input("Enter Gender (Boy/Girl): ").strip().lower()
            division = input("Enter Division: ")

            record = [roll, name, gender, division]

            if gender == "boy" or gender == "male":
                boys_writer.writerow(record)
            elif gender == "girl" or gender == "female":
                girls_writer.writerow(record)
            else:
                print("Invalid gender! Record not stored.")

    print("\nBoys details stored in boys.csv")
    print("Girls details stored in girls.csv")

# Function call
store_students()