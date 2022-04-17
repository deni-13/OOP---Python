#%%encapsulation
#method or variables are restricted using encapsulation

class BankAccount:
    def __init__(self, name, money, address):
        self.name = name # globalL
        self.__money = money # private
        self.address = address
    # get and set
    def getMoney(self):
        return self.__money
    def setMoney (self, amount):
        self._money = amount
    def increase(self):
        self.__money=self.__money+500
p1 = BankAccount ("messi", 100, "barcelona")
p2 = BankAccount("neymar", 2000, "paris")
print("get method:",p1.getMoney())
p1.setMoney(5000)
print(p1.getMoney())
p1.increase()
print("after raise: ",p1.getMoney())
             
#__increase --> private


#%% inheritance

class Animal:
    def __init__(self):
        print("animal is created")
        
    def stri(self):
        print( "animal")
    def walk(self):
        print("animal walk")
        
class Monkey(Animal):
    def __init__(self):
        super().__init__()
        print("yeAa")
        
    def climb(self):
        print("yes yes")
class Bird(Animal):
    def _init_(self):
        super ()._init_()
        print("bird is created")
    def fly(self):
        print("fly")


m1=Monkey()

m1.stri() #parent method s used for child method
m1.climb()
b1=Bird()
b1.fly()
b1.stri() #__super() ile bunu kullanaildik
#%%abstracts #ortak fonk tutarlar
#super clas- parent 
#sub class -child
from abc import ABC, abstractmethod
class Animal(ABC): # super class
   @abstractmethod
   def walk(self): pass
   @abstractmethod
   def run(self): pass

class Bird(Animal):# sub class-- abstarctta methodları burda kullanmak zorundayız subtada  

    def _init_(self):
      print("bird") 
    def walk(self): 
         print("walk")
     
    def run(self):
        print("run")
b1 = Bird()



#%%overriding  -->geecersiz kılma:
    
    
class An:
    def tostring(self):
        print("animal")
class Monkey(An):
    def tostring(self):
        print("monkey")



a1=An()
a1.tostring()
m1=Monkey()
m1.tostring() #inheritance olmasına ragmen uzerine yazdık




#%%polymorphism --! subtaki method super classtada kullanılıyor overriding gibi ayni

class Emp:
    def rraise(self):
        raise_rate=0.1
        return 100 + raise_rate*100
class CE(Emp):
    def rraise(self):
        raise_rate=0.2
        return 100 + raise_rate*100
class EE(Emp):
    def rraise(self):
        raise_rate=0.3
        return 100 + raise_rate*100
    
    
e1=Emp()
ce=CE()
ee=EE()

    
    
li=[ce,ee] 
for i in li:
    i.rraise()








