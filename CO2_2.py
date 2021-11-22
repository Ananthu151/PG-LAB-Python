n=int(input("Enter the Number:"))
a=0
b=1
c=0
f=0
while(f<n):
    a=b
    b=c
    c=a+b
    f=f+1
    print(c ,end=" ")
