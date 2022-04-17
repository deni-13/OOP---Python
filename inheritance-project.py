class Website:
    "parent"
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    def loginInfo(self):
        print(self.name + " " + self.surname )


class W1(Website):
    "child"
    def __init__(self,name,surname,ids):  #methodları kopyaladık inheritance
        Website.__init__(self, name, surname)     
        self.ids=ids
         
    def login(self):
        print(self.name+ " "+self.surname+ " "+ self.ids)
             
         
         
p1 = Website("name","surname")
p2=W1("name","surname","1223")