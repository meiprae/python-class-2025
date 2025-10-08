## Grading System

# Grading
def grade_student(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


# Student handler
def add_grade():
    student_id = input("Enter Student ID: ")
    eng = int(input("Enter English Score: "))
    math = int(input("Enter Math Score: "))
    cp = int(input("Enter Computer Score: "))
    db = int(input("Enter Database Score: "))


    with open("grade.txt", "a") as file:
        file.write(f"{student_id},{eng},{math},{cp},{db}\n")
    print("Grades added successfully.")


def add_student():
    student_id = input("Enter Student ID: ")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    with open("students.txt", "a") as file:
        file.write(f"{student_id},{first_name},{last_name}\n")
    print("Student added successfully.")


def show_grades():
    # Show student info with grade and order grade avg by DESC
    try:
        with open("students.txt", "r") as student_file, open(
            "grade.txt", "r"
        ) as grade_file:
            students = {
                line.split(",")[0]: line.strip().split(",")[1:]
                for line in student_file.readlines()
            }
            grades = grade_file.readlines()
            if not grades:
                print("No grades found.")
                return
            print("\nStudent Grades:")
            for grade in grades:
                student_id, eng, math, cp, db = grade.strip().split(",")
                if student_id in students:
                    first_name, last_name = students[student_id]
                    avg_score = (float(eng) + float(math) + float(cp) + float(db)) / 4
                    letter_grade = grade_student(avg_score)
                    print(
                        f"ID: {student_id}, Name: {first_name} {last_name}, "
                        f"Scores: [Eng: {eng}, Math: {math}, CP: {cp}, DB: {db}], "
                        f"Avg: {avg_score:.2f}, Grade: {letter_grade}"
                    )
                else:
                    print(f"ID: {student_id} not found in student records.")
    except FileNotFoundError:
        print("No students or grades found. Please ensure the files exist.")


def top5_scorer():
    try:
        with open("grade.txt", "r") as file:
            grades = file.readlines()
            if not grades:
                print("No grades found.")
                return
            score_list = []
            for grade in grades:
                student_id, eng, math, cp, db = grade.strip().split(",")
                avg_score = (float(eng) + float(math) + float(cp) + float(db)) / 4
                score_list.append((student_id, avg_score))
            score_list.sort(key=lambda x: x[1], reverse=True)
            print("\nTop 5 Scorers:")
            for student_id, avg_score in score_list[:5]:
                print(f"ID: {student_id}, Average Score: {avg_score:.2f}")
    except FileNotFoundError:
        print("No grades found. The file does not exist.")


# Manu
def menu(choice):
    if choice == "1":
        add_student()
    elif choice == "2":
        add_grade()
    elif choice == "3":
        show_grades()
    elif choice == "4":
        top5_scorer()
    elif choice == "5":
        print("Exiting the program.")
        exit()
    else:
        print("Invalid choice. Please try again.")


# Main Program
while True:
    print("\nMenu:")
    print("1. Add Student")
    print("2. Add Grades")
    print("3. View Students")
    print("4. View Grades and Top 5 Scorers")
    print("5. Exit")
    user_choice = input("Enter your choice: ")
    menu(user_choice)
