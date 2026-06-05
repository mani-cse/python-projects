class Student:
    def __init__(self,name,age,dept,marks):
        self.name = name
        self.age = age
        self.dept = dept
        self.marks = marks
    def display(self):
        print ("Student Name:",self.name)
        print ("Student Age:",self.age)
        print ("Student Dept:",self.dept)
        print ("Student Marks:",self.marks)
        print("--------------------------------------")
students = []
def add_student():
    name = input("Enter Name:")
    age = int(input("Enter Age:"))
    dept = input("Enter Dept:")
    marks = int(input("Enter Marks:"))
    s = Student (name,age,dept,marks)
    students.append(s)
    print("STUDENT ADDED SUCCESSFULY!")
def viwe_student():
    if len(students) == 0:
        print("No Student Found!")
    else:
        print("\n=== All Student ===")
        for s in students:
            s.display()
def search_student():
    name = input("ENTER STUDENT NAME TO SEARCH:")
    found = False
    for s in students:
        if s.name.lower() == name.lower():
            print("\n STUDENT FOUND !")
            s.display()
            found = True
            break
    if not found:
        print("STUDENT NOT FOUND !") 
def  update_marks():
    name = input("ENTER STUDENT NAME TO UPDATE:")
    found = False
    for s in students:
        if s.name.lower() == name.lower():
            print("CURRENT MARKS:",s.marks)
            new_marks = int(input("ENTER NEW MARKS:"))
            if new_marks >= 0 and new_marks <= 100:
                s.marks = new_marks   
                print("MARKS UPDATED SUCCESSFULY !")
            else:
                print("INVALID MARKS !")
            found = True
            break
    if not found:
        print("STUDENT NOT FOUND !")
def delete_student():
    name = input("Enter Student Name To Delete:")
    found = False
    for s in students:
        if s.name.lower() == name.lower():
            students.remove(s)
            print("STUDENT DELETED SUCCESSFULY !")
            found = True
            break
    if not found:
        print("STUDENT NOT FOUND !")
def manu():
    print("\n === STUDENT MANAGEMENT SYSTEM ===")
    print("1. Add Student")
    print("2. Viwe All Student")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Exit")
    return int(input("Enter Choice:"))
while True:
    choice = manu()
    if choice == 1:
        add_student()
    elif choice == 2:
        viwe_student()
    elif choice == 3:
        search_student()
    elif choice == 4:
        update_marks()
    elif choice == 5:
        delete_student()
    elif choice == 6:
        print("GOOD BYE BRO !")
        break
