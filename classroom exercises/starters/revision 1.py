#Daniel Ogunlana
#27/02/2015
#Records
#Revision Exercise 1

class StudentTestScore:
    def __init__(self):
        self.name = None
        self.test_score = None

student_test_score = StudentTestScore()
student_test_score.name = input("Please enter your name: ")
student_test_score.test_score = int(input("Please enter your test score: "))

print("Your name is {0}".format(student_test_score.name))
print("Your score is {0}".format(student_test_score.test_score))
