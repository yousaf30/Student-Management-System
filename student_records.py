import csv

DATA_FILE = "students.csv"


# ---------------- Helper Functions ----------------

def load_data():
    data = []
    try:
        with open(DATA_FILE, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["marks"] = float(row["marks"])  # convert string → float
                data.append(row)
    except FileNotFoundError:
        return []   # file exist nahi to empty list return hogi

    return data


def save_data(data):
    with open(DATA_FILE, "w", newline="") as f:
        fieldnames = ["roll", "name", "class", "marks"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


# ---------------- Core Functionalities ----------------

def add_student():
    data = load_data()
    print("\n---- Add Student ----")

    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    class_name = input("Enter Class: ")
    marks = float(input("Enter Marks: "))

    student = {
        "roll": roll,
        "name": name,
        "class": class_name,
        "marks": marks
    }

    data.append(student)
    save_data(data)
    print("Student added successfully!")


def view_students():
    data = load_data()
    print("\n---- All Students ----")
    if not data:
        print("No student records found.")
        return

    for s in data:
        print(f"Roll: {s['roll']}, Name: {s['name']}, Class: {s['class']}, Marks: {s['marks']}")


def search_student():
    data = load_data()
    roll = input("Enter Roll No to search: ")
    for s in data:
        if s["roll"] == roll:
            print(f"Found → Name: {s['name']}, Class: {s['class']}, Marks: {s['marks']}")
            return
    print("Student not found!")


def update_student():
    data = load_data()
    roll = input("Enter Roll No to update: ")

    for s in data:
        if s["roll"] == roll:
            print("\n--- Update Student ---")
            s["name"] = input("New Name: ")
            s["class"] = input("New Class: ")
            s["marks"] = float(input("New Marks: "))
            save_data(data)
            print("Record updated successfully!")
            return

    print("Student not found!")


def delete_student():
    data = load_data()
    roll = input("Enter Roll No to delete: ")

    new_data = [s for s in data if s["roll"] != roll]

    if len(new_data) == len(data):
        print("Student not found!")
        return

    save_data(new_data)
    print("Record deleted successfully!")


# ---------------- Report Generator ----------------

def generate_report():
    data = load_data()
    print("\n---- Student Report ----")

    if not data:
        print("No data available.")
        return

    total = len(data)
    class_count = {}

    for s in data:
        class_name = s["class"]
        class_count[class_name] = class_count.get(class_name, 0) + 1

    print(f"Total Students: {total}")
    print("\nClass-wise Count:")
    for c in class_count:
        print(f"{c} → {class_count[c]}")


# ---------------- Main Menu ----------------

while True:
    print("\n===== Student Record Management System (CSV Only) =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Generate Report")
    print("7. Exit")

    choice = input("Enter your choice: ")

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
        generate_report()
    elif choice == "7":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")
