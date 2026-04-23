import csv

def write_data(file_path, data, headers):
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter (file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

def export_students_to_csv(data):
    headers = [
        "full_name",
        "section",
        "spanish_grade",
        "english_grade",
        "social_studies_grade",
        "science_grade",
        "average"
    ]

    if data:
        write_data('students.csv', data, headers)
        print("Student data was successfully saved to 'students.csv'. ")
    else:
        print("No student data available to export. ")

def import_csv(students):
    try:
        with open('students.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            imported_count = 0
            
            for row in reader:
                student = {
                    "full_name": row["full_name"],
                    "section": row["section"],
                    "spanish_grade": int(row["spanish_grade"]),
                    "english_grade": int(row["english_grade"]),
                    "social_studies_grade": int(row["social_studies_grade"]),
                    "science_grade": int(row["science_grade"]),
                    "average": float(row["average"])
                }

                students.append(student)
                imported_count = imported_count + 1
            
            if imported_count > 0:
                print(f"{imported_count} student(s) were imported from 'students.csv'. ")
            else:
                print("The file is empty. No students were imported. ")
    except FileNotFoundError:
        print("No exported CSV file was found. ")
