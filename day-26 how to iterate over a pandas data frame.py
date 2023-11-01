import pandas
Student_dict = {
    "student": ["Angela", "Harshad", "Den"],
    "score": [56, 23, 78]
}

# ----------------------------------------------------------
# looping through dictionaries
# for (key, value) in Student_dict.items():
#     print(value)
# ----------------------------------------------------------

student_data_frame = pandas.DataFrame(Student_dict)
# print(student_data_frame)

# ----------------------------------------------------------
# looping through over Data frame
# for (key, value) in student_data_frame.items():
#    print(value)
# ----------------------------------------------------------

# loop through rows of a data frame

for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)
