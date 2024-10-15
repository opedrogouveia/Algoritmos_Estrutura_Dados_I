from Student import Student
from HighSchoolStudent import HighSchoolStudent
from UndergraduateStudent import UndergraduateStudent

def printStudent(self):
        print(self)
        
s1 = Student("Ethan Johnson", "87432901-5")
s2 = HighSchoolStudent("Emily Davis", "56321094-8", 3)
s3 = UndergraduateStudent("Michael Brown", "39048712-6", 5)

printStudent(s1)
printStudent(s2)
printStudent(s3)