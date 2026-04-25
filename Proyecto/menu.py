from actions import student_input, view_students, top3_avg, overall_avg
from data import export_students_to_csv, import_csv

def menu():

    students = []

    
    while True:
        try:
            print("\n===== Student Menu =====")
            print("1- Enter student information")
            print("2- View information for all students")
            print("3- View the top 3 students with the highest average grade")
            print("4- View the average grade of all students")
            print("5- Export all current data to a CSV file")
            print("6- Import students from CSV")
            print("7- Exit Menu")


            num = int(input("Select a value to perform a menu action: "))
        

            if num == 1:
                student_input(students)
            elif num == 2:
                view_students(students)
            elif num == 3:
                top3_avg(students)
            elif num == 4:
                overall_avg(students)
            elif num == 5:
                export_students_to_csv(students)
            elif num == 6:
                import_csv(students)
            elif num == 7:
                print("Exit Menu ")
                break
            else:
                print("Incorrect option. Select an option from the menu.")
        except ValueError:
            print(f"The selected option is incorrect. Select a number from the menu.")

