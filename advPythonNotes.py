# Notes for advance python 
# By : Divyansh


# Class and Multiple Inheritance in a class 
class student():        # student can be any thing
    def __init__ (self, name):
        self.name=name
    
    def printDetails (self):
        print(self.name," am a student")

class youtuber():       # youtuber can be any one
    def __init__ (self, name):
        self.name=name
    
    def printDetails (self):
        print(self.name," am a youtuber")

class person(student, youtuber):        # final inheritanc class
    def printDetails(self):
        student.printDetails(self)
        youtuber.printDetails(self)

p= person("dee")
p.printDetails()


# 2
        


