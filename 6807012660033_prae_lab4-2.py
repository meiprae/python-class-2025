import random
import json

def get_grade(score):
    if score >= 80:
        return 'A'
    elif score >= 70:
        return 'B'
    elif score >= 60:
        return 'C'
    elif score >= 50:
        return 'D'
    else:
        return 'F'

#
def grade_to_value(grade):
    return {
        'A': 4,
        'B': 3,
        'C': 2,
        'D': 1,
        'F': 0
    }[grade]
    
def generate_score():
    score = int(random.normalvariate(70, 15))  # mean = 70, std dev = 15
    return max(0, min(100, score))

students = {}

for i in range(1, 51):
    student_id = f"S{i:03}"

    eng_score = generate_score()
    com_score = generate_score()
    net_score = generate_score()
    math_score = generate_score()

    eng_grade = get_grade(eng_score)
    com_grade = get_grade(com_score)
    net_grade = get_grade(net_score)
    math_grade = get_grade(math_score)

    total_points = (
        grade_to_value(eng_grade) +
        grade_to_value(com_grade) +
        grade_to_value(net_grade) +
        grade_to_value(math_grade)
    )
    avg_grade_value = round(total_points / 4, 2)

    # colect student data
    students[student_id] = {
        "Eng": eng_grade,
        "Math": math_grade,
        "Com": com_grade,
        "Net": net_grade,
        "Sum": avg_grade_value
    }

# the final output
print(json.dumps(students, indent=4))

