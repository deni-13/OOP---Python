#%%classes
name="Messi" #lesson 1
age=23
class Empl(object):  
    #attributes age,adress ,behavior
    
    
    pass

employee1=Empl()
#lesson 2:
#%%attributes
class Footballer():
    age=34
f1=Footballer()


print(f1)     #memory adress
print(f1.age)  #attribute printed

f1.age=45
print(f1.age) #age s changed --> it s not good


#%%methods lesson 3:

class Square():
    edge=4 
    def area(self): #edge defined w self other edge is invisible
        
        area=self.edge*self.edge
        print(area)
s1 =Square()
print(s1.edge)
print(s1.area())


#%%functions:
class Person():
    age=55
    salary=1000
    #method
    def ageSalary(self):
        print(self.age/self.salary)
        #--------------------------------
        #function  : outside of the class
def ageS(age,salary):
    print(age/salary)    
    
e1=Person()
e1.ageSalary()
    
ageS(13, 100)



#%%constructor -- def __ init__


# class Ani(object):
#     name="dog"
#     age=3
    
#     def getAge(self):
#         return self.age

# a1=Ani()
# a1_age=a1.getAge()  
# print(a1.getAge())  
    

#-------------------
    
    

class Anm(object):
    def __init__(self,name,age,breed):
        self.name=name
        self.age=age
        self.breed=breed
    
    def getAge(self):
        return self.age

a1=Anm("dog",3,"spaniel")
a2=Anm("bird", 4, "parrot")

print(a1.getAge())  
print(a1.breed) #breed is got
print(a2.name)
    

#constructor is required to make a instance






