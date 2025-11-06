#[Nyari Mushaikwa]





#Students Grades tracker

grades = []

subjects = ["Maths", "English", "Science", "Computing"] #creating the 1 dimensional list

for student in range(3):

    studentRecord = []
    studentName = input("Enter student name: ")
    studentRecord.append(studentName)

    for subject in subjects:

        grade = int(input(f"Enter {subject} grade (40-100):"))
# using a while loop so the grade will be showing the correct numbers in the range

        while grade < 40 or grade > 100:
            grade = int(input(f"Invalid! Enter {subject} grade between 40 and 100:"))
        studentRecord.append(grade)

print("\nGrades for 5 students (Maths, English, Science, Computing):") #shows the students grade
for student in grades:
    print(student)
    
# Creating a 1D list for average grade above 70

avgGradesStudents = []


for students in grades:

    sumGrades = sum(student[1:]) # the ':' uses splicing so it takes whatever is afterwards from the list
    avgGrade = sumGrades / 4
    if (avgGrade > 70):
        avgGradeStudents.append(student[0])


print(avgGradesStudents)

    
