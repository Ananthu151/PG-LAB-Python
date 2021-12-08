def factor(n):
    m=n;
    i=int(m/n)
    while(i<=m):
        if(m%i==0):
            print(i,end=" ")
        i=i+1
n=int(input("Enter the Number:"))
factor(n)
