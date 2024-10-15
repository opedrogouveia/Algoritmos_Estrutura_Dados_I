class Student():
    def __init__(self, name, registration):
        self.id = None
        self.name = name
        self.registration = registration
        
    def __str__(self):
        txt = "\n----------------------\n"
        txt += "\n Student: " + self.name
        txt += "\n Registration Number: " + self.registration
        return txt