n=int(input("Enter the Final Year:"))
n1=1700
for i in range(n1,n+1):
    if(i%400==0):
        print(i,end=" ")
    else:
        if( i%100!=0 and i%4==0):
            print(i,end=" ")
            
