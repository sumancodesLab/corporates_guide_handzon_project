students = {
    "Rahul": 75,
    "Priya": 85,
    "Amit": 45,
    "Riya": 92,
    "Suman": 38
}

print("----- Student Marks -----")

for name, marks in students.items():
    print(name, ":", marks)

print("\nStudents scoring 50 or above:")

for name, marks in students.items():
    if marks >= 50:
        print(name)

highest_mark = max(students.values())

print("\nHighest Mark:", highest_mark)

for name, marks in students.items():
    if marks == highest_mark:
        print("Top Student:", name)