def grades_that_pass(students, grades, limit):
    result = []
    index = 0
    
    for grade in grades:
        student = students[index]
    if grade >= limit:
    
        result = result + [student]
    index += 1
    return result
