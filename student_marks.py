students = {}
n = int(input("Enter the number of students: "))

for i in range(n):
    name = input(f"\nEnter the name of student {i+1}: ")
    marks = []

    for j in range(3):
        mark = int(input(f"Enter mark {j+1} of {name}: "))
        marks.append(mark)

    total = sum(marks)
    average = total / 3

    # Correct grade conditions
    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    elif average >= 60:
        grade = 'D'
    else:
        grade = 'E'
    students[name] = {
        "Marks": marks,
        "Total": total,
        "Average": average,
        "Grade": grade
    }
# Print student details AFTER all data is collected
print("\n---- Student Details ----")
print("Name\tMarks\t\tTotal\tAverage\tGrade")

for name, info in students.items():
    print(f"{name}\t{info['Marks']}\t{info['Total']}\t{info['Average']:.2f}\t{info['Grade']}")
