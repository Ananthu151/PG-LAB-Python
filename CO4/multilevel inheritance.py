class student:
    def getstudent(self):
        self.name=input("Enter your name:")
        self.age=input("Enter your age:")
        self.gender=input("Enter you gender")

class test(student):
    def getmark(self):
        self.studentclass=input("Enter you class:")
        print("Enter the marks:")
        print("1:Maths")
        self.m1=int(input())
        print("2:Python")
        self.m2=int(input())
        print("3:DS")
        self.m3=int(input())
class marks(test):
    def display(self):
        print("\nName:",self.name)
        print("Age:",self.age)
        print("Gender:",self.gender)
        print("Class:",self.studentclass)
        print("Total Marks:",self.m1+self.m2+self.m3,"/300")
m=marks()
m.getstudent()
m.getmark()
m.display()
