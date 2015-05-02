def squared(x):
    return x ** 2

def factorial(x):
    counter = 1
    result = 1
    while counter <= x:
        result *= counter
        counter += 1
    return result
print(factorial(5))
print(squared(3))

def numbere_items(items):
    count = 0
    for item in items:
        count += 1
    return count
a = [1,2,3]
print(numbere_items(a))

def member(x,xs):
    found = False
    for memb in xs:
        if memb == x:
            found = True
        return found
a = 1
b = [1,2,3]
print(member(a,b))

def grades_that_pass(students,grades,limit):
    result = []
    index = 0
    for grade in grades:
        student = students[index]
        if grade >= limit:
                result = result + [student]
        index += 1
    return result
students = ["Rado", "Ivo", "Maria", "Nina"]
grades = [3, 4.5, 5.5, 6]

result = grades_that_pass(students, grades, 4.0)
print(result)


