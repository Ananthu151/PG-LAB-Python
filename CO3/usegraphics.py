from graphics import rectangle
from graphics import circle
c=1
s=1
while(c>0):
    print("Enter the Choice:")
    print("1:Rectangle")
    print("2:Circle")
    print("3:Exit")
    x=int(input())
    if(x==1):
        while(s>0):
            print("Enter the Choice:")
            print("1:Area")
            print("2:Perimeter")
            print("3:Exit")
            s=int(input())
        
            if(s==1):
                l=int(input("Enter the length:"))
                b=int(input("Enter the breadth"))
                print("The Area is :",rectangle.area(l,b))
            if(s==2):
                l=int(input("Enter the length:"))
                b=int(input("Enter the breadth"))
                print("The Area is :",rectangle.perimeter(l,b))
            if(s>2):
                break
    if(x==2):
        while(s>0):
            print("Enter the Choice:")
            print("1:Area")
            print("2:Perimeter")
            print("3:Exit")
            s=int(input())
        
            if(s==1):
                l=int(input("Enter the Radius"))
                print("The Area is :",circle.area(l))
            if(s==2):
                l=int(input("Enter the Radius:"))
                print("The Area is :",circle.perimeter(l))
            if(s>2):
                break
        
    if(x>2):
        break
     
        
    
