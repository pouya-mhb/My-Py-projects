# this code calculates gpa of your grades 

course_count = int(input("How many course ? : "))
grade_list = []
unit_list=[]
calculated_grade_list=[]

for course_number in range(0, course_count):
    course_grade = float(input("please enter each course grade : "))
    grade_list.append(course_grade)
    course_unit = float(input("please enter each course unit : "))
    unit_list.append(course_unit)
    calculated_grade = grade_list[course_number]*unit_list[course_number]
    calculated_grade_list.append(calculated_grade)

gpa = sum(calculated_grade_list)/sum(unit_list)

print ("===========================")
print("Your grades \n")
for printed_grades in grade_list:
    print(printed_grades)
print("===========================")
print("Your calculated grades \n")
for cal_printed_grades in calculated_grade_list:
    print (cal_printed_grades)
print("===========================")
print("your GPA : ", gpa)
