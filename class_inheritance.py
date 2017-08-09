# QUESTION1
# # Write the Python code for a class for which each instantiation is a student with the attributes of Name, Gender, Year, and GPA.
# # Include in the class a method called IsFreshman() which returns True/False depending if the student is in year 1.
#
#
# # EXAMPLE USE
# # The following use of the class should produce the output below.
# Student1 = StudentBody("Mary", "Female", 1, 2.9)
# Student2 = StudentBody("Bill", "Male", 3, 3.1)
# Student3 = StudentBody("Jill", "Female", 3, 3.4)
# Student4 = StudentBody("Jack", "Male", 3, 2.9)
#
# print(Student1.IsFreshman())
# print(Student2.IsFreshman())
#
#
# # OUTPUT
# # True
# # False
#
#
#
# # QUESTION 2
# # Create a subclass of the StudentBody class created in #1 called MathStudentBody which adds
# # a new attribute MathSATScore and a new method CombinedSATandGPA that adds the MathSATScore to the GPA*100
#
#
# # EXAMPLE USE
# # The following use of the class should produce the output below.
# # The following use of the class should produce the output below.
# Student1 = MathStudentBody("Debbie", "Female", 1, 2.9, 740)
# Student2 = MathStudentBody("Eddie", "Male", 3, 3.1, 680)
#
# print(Student1.CombinedSATandGPA())
# print(Student2.CombinedSATandGPA())
#
# # OUTPUT
# 1030.0
# 990.0

class  StudentBody:
    def __init__(self,n,g,y,gpa):
        self.n=n
        self.g=g
        self.y=y
        self.gpa=gpa
    def IsFreshman(self):
        return self.y==1

class  MathStudentBody(StudentBody):
    def __init__(self,n,g,y,gpa,m):
        StudentBody.__init__(self,n,g,y,gpa)
        self.m=m
    def CombinedSATandGPA(self):
        return self.gpa*100 + self.m

Student1 = StudentBody("Mary", "Female", 1, 2.9)
Student2 = StudentBody("Bill", "Male", 3, 3.1)
Student3 = StudentBody("Jill", "Female", 3, 3.4)
Student4 = StudentBody("Jack", "Male", 3, 2.9)

print(Student1.IsFreshman())
print(Student2.IsFreshman())


Student1 = MathStudentBody("Debbie", "Female", 1, 2.9, 740)
Student2 = MathStudentBody("Eddie", "Male", 3, 3.1, 680)
print(Student1.CombinedSATandGPA())
print(Student2.CombinedSATandGPA())