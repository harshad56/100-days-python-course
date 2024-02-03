student_height = (
    input("write the height of the student separted by comma: ")).split(",")


for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
print(student_height)  # it use for code in converting to list


# 1)in loops example below add of stdunts ex 123,345,234
# 2)here we see total_of_student_height = 0
# 3)then 1st height is 123 is add on using total_of_student_height += height
# in  total_of_student_height

# 4)then 2nd height is 345 is add on using total_of_student_height += height
# in  total_of_student_height

# then 3rd height is 234 is add on using total_of_student_height += height
# in  total_of_student_height

# 5)here it go on it go like a loop it check 1 st then 2nd then 3rd like to end of the loop
# 6)same for alculate the average of student's height

# __________________________________________________________________________#
# calculate the total height of all students
total_of_student_height = 0

for height in student_height:
    total_of_student_height += height
print(total_of_student_height)

# __________________________________________________________________________#

# calculate the average of student's height

no_of_students = 0
for students in student_height:
    no_of_students += 1
    # here loop run as in input no_of _students example students in stduents_height list is =[123,456,677] here 3 no then loop three time  then no_of_students=3
print(no_of_students)

average_height = round(total_of_student_height / no_of_students)
print("the average height is :", average_height)
