# Notes for advance python 
# By : Divyansh


# Class and Multiple Inheritance in a class 
class student():
    def __init__ (self, name):
        self.name=name
    
    def printDetails (self):
        print(self.name," am a student")

class youtuber():
    def __init__ (self, name):
        self.name=name
    
    def printDetails (self):
        print(self.name," am a youtuber")

class person(student, youtuber):
    def printDetails(self):
        student.printDetails(self)
        youtuber.printDetails(self)

p= person("dee")
p.printDetails()


        


