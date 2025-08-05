# Function to calculate grade
def calculate_grade(marks):
    total = sum(marks)  # keyword: sum
    average = total / len(marks)
    
    # Keyword: if, elif, else
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"

# Function to check pass/fail
def is_pass(marks):
    for mark in marks:  # keyword: for
        if mark < 40:
            return False
    return True

# List to store student records (type: list of dicts)
students = []

# Keyword: while loop to enter data
while True:
    name = input("Enter student name (or type 'done' to finish): ")
    if name.lower() == 'done':
        break  # keyword: break

    # Get marks for 3 subjects
    marks = []
    for i in range(1, 4):
        mark = int(input(f"Enter marks for subject {i}: "))
        marks.append(mark)  # keyword: append

    # Store in dictionary
    student = {
        "name": name,           # type: str
        "marks": marks,         # type: list of int
        "average": sum(marks)/len(marks),  # type: float
        "grade": calculate_grade(marks),   # type: str
        "pass": is_pass(marks)             # type: bool
    }

    students.append(student)

# Final report
print("\n--- Student Report ---")
for s in students:
    status = "Pass" if s["pass"] else "Fail"
    print(f"Name: {s['name']}, Avg: {s['average']:.2f}, Grade: {s['grade']}, Status: {status}")
