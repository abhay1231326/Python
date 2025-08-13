students = []
grades = []

def add_student():
    name = input("enter student name:")
    if name in students:
        print("students alerday exists.")
        return
    try:
        greade = float(input("enter grade:"))
        students.append(name)
        grades.append(grades)
        print("student added successfully.")
    except ValueError:
        print("invalid grade. please enter a number .")
        
def update_grade():
            name = input("enter student name to uodate grade:")
            if name in students:
                index = students.index(name)
                try:
                    new_grade = float(input("enter new grade"))
                    grades[index] = new_grade 
                    print("grade updated successfully.")
                except ValueError:
                    print("invalide grade.please enter a number.")
                else:
                    print("student not found")
                    
def calculate_average():
                        if grades:
                            avg = sum(grades)/len(grades)
                            print(f"average grade of the class:{avg:.2f}")
                        else:
                            print("no grades to calculate average.")
                            
def highest_lowest_grade():
                                if grades:
                                    highest = max(grades)
                                    lowest = min(grades)
                                    print(f"highest grade:{highest}")
                                    print(f"lowest grade:{lowest}")
                                else:
                                    print("no grades to show.")
                                    
def display_menu():
    print("\n--- Student Grade Management System ---")
    print("1. Add a student and grade")
    print("2. Update student grade")
    print("3. Remove a student")
    print("4. Calculate average grade")
    print("5. Show highest and lowest grade")
    print("6. Exit")

while True:
    display_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        update_grade()
    elif choice == '3':
        remove_student()
    elif choice == '4':
        calculate_average()
    elif choice == '5':
        highest_lowest_grade()
    elif choice == '6':
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please select from 1 to 6.")
                                        
            
        
