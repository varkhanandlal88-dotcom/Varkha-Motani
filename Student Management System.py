class Student:
    def __init__(self):
        self.students = []

    # Add Student Photo

    from tkinter import Tk
    from tkinter.filedialog import askopenfilename

    Tk().withdraw()

    photo = askopenfilename(
        title="Select Student Photo",
         filetypes=[
             ("Image Files", "*.png *.jpg *.jpeg")
         ]
    )
    print(photo)

    # Add Student
    def add_student(self):
        print("\n------ Add Student ------")

        roll_no = input("Enter Roll No: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")
        

        student = {
            "Roll No": roll_no,
            "Name": name,
            "Age": age,
            "Course": course
        }

        self.students.append(student)

        print("\nStudent Added Successfully!")


    # View Students
    def view_students(self):
        print("\n------ Student List ------")

        if len(self.students) == 0:
            print("No Student Found!")
            return

        for student in self.students:
            print("-" * 30)
            print(f"Roll No : {student['Roll No']}")
            print(f"Name    : {student['Name']}")
            print(f"Age     : {student['Age']}")
            print(f"Course  : {student['Course']}")

    # Search Student
    def search_student(self):
        print("\n------ Search Student ------")

        roll_no = input("Enter Roll No: ")

        for student in self.students:
            if student["Roll No"] == roll_no:
                print("\nStudent Found!")
                print("-" * 30)
                print(f"Roll No : {student['Roll No']}")
                print(f"Name    : {student['Name']}")
                print(f"Age     : {student['Age']}")
                print(f"Course  : {student['Course']}")
                return

        print("Student Not Found!")

    # Update Student
    def update_student(self):
        print("\n------ Update Student ------")

        roll_no = input("Enter Roll No: ")

        for student in self.students:
            if student["Roll No"] == roll_no:

                student["Name"] = input("Enter New Name: ")
                student["Age"] = input("Enter New Age: ")
                student["Course"] = input("Enter New Course: ")

                print("\nStudent Updated Successfully!")
                return

        print("Student Not Found!")

    # Delete Student
    def delete_student(self):
        print("\n------ Delete Student ------")

        roll_no = input("Enter Roll No: ")

        for student in self.students:
            if student["Roll No"] == roll_no:
                self.students.remove(student)
                print("\nStudent Deleted Successfully!")
                return

        print("Student Not Found!")

# Object Creation
obj = Student()

# Main Menu
while True:

    print("\n")
    print("=" * 40)
    print(" STUDENT MANAGEMENT SYSTEM ")
    print("=" * 40)
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("\nEnter Your Choice: ")

    if choice == "1":
        obj.add_student()

    elif choice == "2":
        obj.view_students()

    elif choice == "3":
        obj.search_student()

    elif choice == "4":
        obj.update_student()

    elif choice == "5":
        obj.delete_student()

    elif choice == "6":
        print("\nThank You!")
        break

    else:
        print("\nInvalid Choice!")