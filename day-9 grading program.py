student_score = {
    "harry": 81,
    "ron": 78,
    "Hermione": 99,
    "darco": 74,
    "nevile": 62,
}

# Todo-1: create an empty dictionay called student_grade

student_grade = {}

# Todo-2:write your code below to add the grade to student_grades.
for student in student_score:
    score = student_score[student]
    if score > 90:
        student_grade[student] = "outstanding"

    elif score > 80:
        student_grade[student] = "exceads exeception"

    elif score > 70:
        student_grade[student] = "acceptable"

    else:
        student_grade[student] = "fail"

print(student_grade)
