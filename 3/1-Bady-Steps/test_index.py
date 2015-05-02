def grades_that_pass(students, grades, limit):
    result = []
    index = 0

    for grade in grades:
        student = students[index]
        
        if grade >= limit:
            result = result + [student]
        
        index += 1

    return result
students = ["Ivan", "Grigor", "Ivailo"]
grades = [4.0,4.5,6.0]
limit = 4.5
print(grades_that_pass(students,grades,limit))