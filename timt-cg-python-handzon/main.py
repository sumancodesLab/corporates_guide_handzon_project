def calculate_result(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average


name = input("Enter student name: ")

marks = []
for i in range(3):
    mark = float(input(f"Enter marks of subject {i + 1}: "))
    marks.append(mark)

total, average = calculate_result(marks)

print("\n----- Student Result -----")
print("Student Name:", name)
print("Total Marks:", total)
print("Average Marks:", round(average, 2))

if average >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")