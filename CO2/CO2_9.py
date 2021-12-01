n=int(input("Enter the limit:"))
i=0
j=0
for i in range(0,n):
    for j in range(0,i):
        print("*",end="")
    print()
for i in range(n,0,-1):
    for j in range(0,i):
        print("*",end="")
    print()
