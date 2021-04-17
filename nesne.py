
integer =22
string1 = "ronaldo"

#classes

employee_name ="messi"
employe_age=33
# her biri calısan için degisken mi atıcaz???


class Employee(object): #class ici nesne yaz
    #attribute= age adres 
    #behavior pass verebilme
    
    pass #syntax hatası olmasın

#class dısındayım
employee1=Employee()
    
    
#%% attribute
class Footballer:
    footbal_club="barca"
    age=30

f1 = Footballer()


print(f1)
print(f1.age)
print(f1.footbal_club)
f1.footbal_club="real madrid"
print(f1.footbal_club)



#%% methods 

class Square(object):
    
        edge = 5 #meter #classobjec
        area=0
        
        def area1(self): #behavior
            self.area=self.edge*self.edge
            print("area:",self.area)
            #############
s1=Square() 
 

print(s1)
print(s1.edge)
print(s1.area1())

s1.edge= 7
s1.area1()


#%%


class Emp(object):
    age=25
    salary=1000 
    
    def ageSalaryRatio(self):
        a=self.age/self.salary
        print("method",a)
        
        
e1=Emp()
e1.ageSalaryRatio() #klassicin

def ageSalaryRatio(age,salary):
    a=age/salary
    print("function",a)

        


ageSalaryRatio(30,3000)
 
#%% fonksiyonlar
pi=3.14
r=5
area=pi*r**2

def findArea(pi,r): #sadece method parametresi 
    #area=pi*r**2
    print(area)
   #print dısında baska bisey 
    return area
sonuc1=findArea(pi,r) 

sonuc2=findArea(pi,10)

print(sonuc1+sonuc2)


