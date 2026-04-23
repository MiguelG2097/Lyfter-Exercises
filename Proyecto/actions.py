student_dict = {
    "full_name": "",
    "section": "",
    "spanish_grade": 0,
    "english_grade": 0,
    "social_studies_grade": 0,
    "science_grade": 0,
    "average": 0
}
students = []


def student_input():
    while True:
        try:
            student_count = int(input("How many students do you want to enter "))

            if student_count > 0:
                break
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid number")
    
    for i in range(student_count):
        student_name = input("Enter student name: ")
        student_section = input("Enter student section: ")
        student_spanish_grade = get_valid_grade("Spanish")
        student_english_grade = get_valid_grade("English")
        student_social_grade = get_valid_grade("Social Studies")
        student_science_grade = get_valid_grade("Science")

        student_dict = {
            "full_name": student_name,
            "section": student_section,
            "spanish_grade": student_spanish_grade,
            "english_grade": student_english_grade,
            "social_studies_grade": student_social_grade,
            "science_grade": student_science_grade
        }

        students.append(student_dict)
        print(f"Student '{student_name}' added successfully.")
    print(f"\n{student_count} student(s) added successfully.")

def get_valid_grade(subject_name):
    while True:
        try:
            grade = int(input(f"Enter {subject_name} grade: "))

            if grade >= 0 and grade <= 100:
                return grade
            else:
                print("Grade must be between 0 and 100.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

def view_students ():
    if len(students) == 0:
        print("There are no students registered yet. ")
    else:
        for student in students:
            print("------------------------------")
            print(f"Full name: {student['full_name']}")
            print(f"Section: {student['section']}")
            print(f"Spanish grade: {student['spanish_grade']}")
            print(f"English grade: {student['english_grade']}")
            print(f"Social studies grade: {student['social_studies_grade']}")
            print(f"Science grade: {student['science_grade']}")

def top3_avg ():
    for student in students:
        average = (
            student["spanish_grade"] + student["english_grade"] +
            student["social_studies_grade"] + student["science_grade"]) / 4 
        student["average"] = average

    students.sort(key=lambda student: student["average"], reverse=True)

    top_students = students[:3]

    print("\n --- Top students ---")

    for i, student in enumerate(top_students, start=1):
        print(f"\n Top # {i}")
        print(f"Full Name: {student['full_name']} ")
        print(f"Average: {student['average']:.2f} ")

def overall_avg():
    if len(students) == 0:
        print("There are no students registered yet.")
        return
    
    total_average = 0

    for student in students:
        total_average = total_average + student["average"]
    
    overall_average = total_average / len(students)
    
    print("\n--- Overall average grade ---")
    print(f"Overall average grade: {overall_average:.2f}")