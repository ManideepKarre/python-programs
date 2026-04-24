#What it does 1, Add student 2, View student 3, Search student 4, Delete student

#Creating a menu
def show_menu():
    print("\n----Student Manager----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    print("6. Show Stats") #Add this for Showing Stats
    


#storing the data

students=[
    {"name": "John","age": 20, "year": 3},
    {"name": "Max","age": 19, "year": 3},
    {"name": "Wick","age": 21, "year": 4},
] #Adding a demo data

#Adding a student
def add_student():
    name = input("Enter name: ")
    age = int(input("Enter Age: "))
    year = input("Enter year: ")

    students.append({"name": name,"age": age,"year": year})
    print("Student added!")

#Showing Stats

def show_data ():
    if len(students) ==0:
        print("No Data")
        return
    total = len(students)
    ages = [s["age"] for s in students]
    avg_age = sum(ages)/total

    print(f"Total Students: {total}")
    print(f"Average age : {avg_age:.2f}")


#View Students

def view_students():
    if len(students) ==0:
        print("No students found")
    else:
        for i, s in enumerate(students, start=1):
            print(f"{i}. Name: {s["name"]}, Age: {s['age']}")

def search_student():
    search = input()

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
    elif choice == "6":
        show_data()
        
