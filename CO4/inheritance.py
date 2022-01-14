class student:
    def getstu(self,rno,name,cor,rank):
        self.roll=rno
        self.name=name
        self.cor=cor
        self.rank=rank
    def displayStudent(self):
        print("RollNo:",self.roll)
        print("Name:",self.name)
        print("Cource:",self.cor)
        print("Rank:",self.rank)
   
class Test(student):
    def getmarks(self,m):
        self.mark=m
    def displaymarks(self):
        print("Marks:",self.mark)
s=Test()
s.getstu(1,"Anandhu","MCA",12)
s.getmarks(100)
s.displayStudent()
s.displaymarks()
