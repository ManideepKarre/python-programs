#What it does 1, Add student 2, View student 3, Search student 4, Delete student

#Creating a menu
def show_menu():
    print("\n----Student Manager----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

#storing the data

students=[
    {"name": "John","age": 20, "year": 3},
    {"name": "Max","age": 19, "year": 3},
    {"name": "Wick","age": 21, "year": 4},
] #Adding a demo data

#Adding a student
def add_student():
    name = input("Enter name: ")
    age = input("Enter Age: ")
    year = input("Enter year: ")

    students.append({"name": name,"age": age,"year": year})
    print("Student added!")

#View Students

def view_students():
    if len(students) ==0:
        print("No students found")
    else:
        for s in students:
            print("-",s)

#Main Loop

while True:
    show_menu()
    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "5":
        print("GoodBye!")
        break
