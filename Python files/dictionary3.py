student_grades={'bob':85,'john':92,'charlie':67}
student_grades['david']=78
student_grades['bob']=96
del student_grades['charlie']
print("Bob grade:", student_grades['bob'])
for student, grade in student_grades.items():
    print(f"{student}:{grade}")
if "Eve" in student_grades:
    print("Eve's grade:", student_grades["Eve"])
else:
    print("Eve is not in the dictionary")
