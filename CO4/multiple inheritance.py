class  person:
    def getperson(self):
        self.name=input("Name:")
        self.age=input("Age:")
        self.gender=input("Gender:")
    def displayperson(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Gender:",self.gender)
class marks:
    def getmark(self):
        print("Marks:")
        self.m1=int(input("1:Maths"))
        self.m2=int(input("2:Python"))
        self.m3=int(input("3:DS"))
    def displaymark(self):
        print("Total mark:",self.m1+self.m2+self.m3,"/300")
class student(person,marks):
    def getstudent(self):
        self.studentclass=input("Class:")
    def displaystudent(self):
        print("Class:",self.studentclass)
s=student()
s.getperson()
s.getmark()
s.getstudent()
s.displayperson()
s.displaystudent()
s.displaymark()

