class rectangle:
    def __init__(self,length,width):
        self.__length=length
        self.__width=width
    def __lt__(self,a2):
        area1=self.__length*self.__width
        area2=a2.__length*a2.__width
        if(area1<area2):
            return(True)
        else:
            return(False)
print("Enter the Details of Rectangle:1")
l1=int(input("Lenght:"))
w1=int(input("width:"))
r1=rectangle(l1,w1)
print("Enter the Details of Rectangle:2")
l2=int(input("Lenght:"))
w2=int(input("width:"))
r2=rectangle(l2,w2)
if(r1<r2):
    print("Rectangle 2 is larger!!")
else:
    print("Rectangle 1 is larger!!")
