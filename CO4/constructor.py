class pern:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def displaypern(self):
        print(self.name,self.age)
class stud(pern):
    def __init__(self,name,age,m1,m2):
        #pern.__init__(self,name,age)
        super().__init__(name,age)
        self.m1=m1
        self.m2=m2
    def displaystud(self):
        print(self.name,self.age,self.m1,self.m2)
s=stud("ANANTHU",21,99,98)
s.displaypern()
s.displaystud()
       
