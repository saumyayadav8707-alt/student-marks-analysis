# Student Marks Analysis Project
# Author: Saumya Yadav
# B.Tech CSE (Data Science and Machine Learning)

# Sample dataset of students and their marks out of 100 in 3 subjects
students_data = [
    {"name": "Aarav", "math": 85, "python": 90, "dbms": 82},
    {"name": "Diya", "math": 72, "python": 78, "dbms": 75},
    {"name": "Rohan", "math": 91, "python": 94, "dbms": 89},
    {"name": "Sneha", "math": 64, "python": 70, "dbms": 68},
    {"name": "Kabir", "math": 55, "python": 60, "dbms": 58}
]

def assign_grade(percentage):
    if percentage >= 85:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 55:
        return "C"
    else:
        return "D"

print("==================================================")
print("         STUDENT MARKS ANALYSIS REPORT            ")
print("==================================================")

percentages = []
highest_score = 0
topper_name = ""
lowest_score = 100
lowest_name = ""

for student in students_data:
    total = student["math"] + student["python"] + student["dbms"]
    percentage = round(total / 3, 2)
    grade = assign_grade(percentage)
    percentages.append(percentage)

    if percentage > highest_score:
        highest_score = percentage
        topper_name = student["name"]

    if percentage < lowest_score:
        lowest_score = percentage
        lowest_name = student["name"]

    print(f"Student: {student['name']:6} | Total: {total}/300 | Percentage: {percentage}% | Grade: {grade}")

class_average = round(sum(percentages) / len(percentages), 2)

print("--------------------------------------------------")
print("SUMMARY INSIGHTS:")
print("Total Students Analysed :", len(students_data))
print("Class Average Percentage:", f"{class_average}%")
print("Highest Performer       :", f"{topper_name} ({highest_score}%)")
print("Lowest Performer        :", f"{lowest_name} ({lowest_score}%)")
print("==================================================")
