#Daniel Ogunlana
#27/02/2015
#Records
#Revision Exercise 2

class StudentTestScore:
    def __init__(self):
        self.name = None
        self.test_score = None

student_test_score = StudentTestScore()

students = []
for count in range(3):
    students.append(StudentTestScore())

for student in students:
    student_test_score.name = input("Please enter your name: ")
    student_test_score.test_score = int(input("Please enter your test score: "))

for each in students:
    print(each)
