student_score = input("input a list of student score:").split()

for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)


height_score = 0
for score in student_score:
    if score > height_score:
        height_score = score

print(f" the height score is the class is:{height_score} ")
