#OOPS in python 

class Student:
    name = "Dhruv Sharma"   #class variable
    age = 21               #class variable
    is_adult = True        #class variable

    def __init__(self, admission_no):
        self.admission_no = admission_no


student_1 = Student("22SCSE1550018")
print(student_1.admission_no)   #instance variable

student_2 = Student("22SCSE1550019")
print(student_2.admission_no)