l,b=int(input("Enter L and B of rectangle:")),int(input())
rarea=lambda l,b:l*b
print("Area of Rectangle is:",rarea(l,b))
s=int(input("Enter Side of square:"))
sarea=lambda s:s*s
print("Area of Square is:",sarea(s))
s1,h=int(input("Enter Lenght and height  of triangle ")),int(input())
tarea=lambda s1,h:0.5*s1*h
print("Area of Triangle is:",tarea(s1,h))

