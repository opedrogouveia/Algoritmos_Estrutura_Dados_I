from Student import Student

class HighSchoolStudent(Student):
    def __init__(self, name, registration, year, education = "High School"):
        super().__init__(name, registration)
        self.education = education
        self.year = year
        
    def __str__(self):
        txt = super().__str__()
        txt += "\n Education: " + self.education
        txt += "\n Year: " + str(self.year)
        return txt