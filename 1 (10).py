class Student:
    #static variables
    def St_fn(self):
        return "called class"  #for all objects returned
    def __init__(self,name,dep,age,sch):
        self.name = name
        self.dep=dep
        self.age=age
        self.sch=sch

st1=Student("John","History",22,"Uni")
st2=Student("Janet","Chemistry",21,"Uni")
print(st1.name)
print(st2.name)

print(st1.St_fn())

    