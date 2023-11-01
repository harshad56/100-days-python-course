import random
names = ["harshad", "beth", "devendra", "jay", "karan"]


# dictionary comprehension syntax:
# syntax={new_key:new_value for (key,value) in dict}

students_scores = {student: random.randint(20, 100) for student in names}
print(students_scores)

passed_students = {student: scores for (
    student, scores) in students_scores.items()if scores >= 60}

print(passed_students)
