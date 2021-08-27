# x = [(1,2),(3,3)]
def calculate_gpa(grades_list) -> float:
    total_unit = sum([unit for (_, unit) in grades_list])
    total_grade = sum([grade*unit for (grade, unit) in grades_list])
    return total_grade/ total_unit