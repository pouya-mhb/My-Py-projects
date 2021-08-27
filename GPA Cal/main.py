from calculators import calculate_gpa
from inputs import prompt_scores

scores = prompt_scores()
gpa = calculate_gpa(scores)
print ("===========================")
print("Your grades \n")
for index,(grade, unit) in enumerate(scores):
    #print(grade,unit)
    print (f"{index+1}:\t{grade}\t{unit}")
print("===========================")
print("your GPA : ", gpa)
