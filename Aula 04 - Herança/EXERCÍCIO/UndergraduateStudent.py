from Student import Student

class UndergraduateStudent(Student):
    def __init__(self, name, registration, semester, education = "Undergraduate"):
        super().__init__(name, registration)
        self.education = education
        self.semester = semester
        
    def __str__(self):
        txt = super().__str__()
        txt += "\n Education: " + self.education
        txt += "\n Semester: " + str(self.semester)
        return txt