#class methods

import re


class Student:
    def __init__(self,name,gpa,dep):
        self.name = name
        self.gpa=gpa
        self.dep  = dep
    def Honour(self):  #methods
        if self.gpa > 3:
            return "Congratulations win the Honour card"
        else:
            return "not" 
    def engineering(self):   
        deps=["ceng","eee","me","ce","chee"]
        for dep in deps:
            if self.dep in deps:
                return "engineering"
            else:
                return "not"
st1=Student("Jonathan",3.5,"history")
st2=Student("Amy",2.8,"ceng")


print(st2.Honour())
print(st1.engineering())