# Student Record Management System (Console Based)
# Developed in Python – using file handling

import os

FILENAME = "student_records.txt"

# Function to add a student record
def add_student():
    with open(FILENAME, "a") as file:
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        dept = input("Enter Department: ")
        marks = input("Enter Marks: ")
        file.write(f"{roll},{name},{dept},{marks}\n")
    print("✔️ Student record added successfully!\n")

# Function to display all student records
def view_students():
    print("\n📄 All Student Records:\n")
    if not os.path.exists(FILENAME):
        print("No records found.\n")
        return

    with open(FILENAME, "r") as file:
        records = file.readlines()
        if not records:
            print("No records to display.\n")
        else:
            for line in records:
                roll, name, dept, marks = line.strip().split(",")
                print(f"Roll: {roll} | Name: {name} | Dept: {dept} | Marks: {marks}")
    print()

# Function to search for a student
def search_student():
    roll_no = input("Enter Roll Number to Search: ")
    found = False
    with open(FILENAME, "r") as file:
        for line in file:
            roll, name, dept, marks = line.strip().split(",")
            if roll == roll_no:
                print(f"\n🔍 Found: Roll: {roll} | Name: {name} | Dept: {dept} | Marks: {marks}\n")
                found = True
                break
    if not found:
        print("❌ Student not found.\n")

# Function to update a student record
def update_student():
    roll_no = input("Enter Roll Number to Update: ")
    updated = False
    new_lines = []
    with open(FILENAME, "r") as file:
        for line in file:
            roll, name, dept, marks = line.strip().split(",")
            if roll == roll_no:
                print("Enter New Details:")
                name = input("New Name: ")
                dept = input("New Department: ")
                marks = input("New Marks: ")
                new_lines.append(f"{roll},{name},{dept},{marks}\n")
                updated = True
            else:
                new_lines.append(line)
    with open(FILENAME, "w") as file:
        file.writelines(new_lines)
    if updated:
        print("✅ Record updated successfully!\n")
    else:
        print("❌ Student not found.\n")

# Function to delete a student record
def delete_student():
    roll_no = input("Enter Roll Number to Delete: ")
    deleted = False
    new_lines = []
    with open(FILENAME, "r") as file:
        for line in file:
            roll, name, dept, marks = line.strip().split(",")
            if roll != roll_no:
                new_lines.append(line)
            else:
                deleted = True
    with open(FILENAME, "w") as file:
        file.writelines(new_lines)
    if deleted:
        print("🗑️ Record deleted successfully!\n")
    else:
        print("❌ Student not found.\n")

# Menu function
def menu():
    while True:
        print("📘 STUDENT RECORD MANAGEMENT SYSTEM")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("👋 Exiting Program. Goodbye!")
            break
        else:
            print("❗ Invalid choice. Try again.\n")

# Run the menu
menu()
