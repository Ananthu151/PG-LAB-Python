class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return(self.length*self.breadth)
    def perimeter(self):
        return(2*(self.length+self.breadth))
print("Enter the details of Rectangle 1:")
l1=int(input("Length:"))
b1=int(input("Breadth:"))
print("Enter the details of Rectangle 2:")
l2=int(input("Length:"))
b2=int(input("Breadth:"))
r1=rectangle(l1,b2)
r2=rectangle(l2,b2)
print("Rectangle 1: Area: ",r1.area()," , Perimeter: ",r1.perimeter())
print("Rectangle 2: Area: ",r2.area()," , Perimeter: ",r2.perimeter())
print("-------------------------")
if(r1.area()>r2.area()):
    print("Rectangle 1 is Bigger!!")
else:
    print("Rectangle 2 is Bigger!!")
