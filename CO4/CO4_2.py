class bank:
    def __init__(self,ac,name,atype,bal=0):
        self.ac=ac
        self.name=name
        self.atype=atype
        self.bal=bal
    def deposit(self,bal):
         self.bal+=bal
    def  withdraw(self,bal):
        if(self.bal==0):
            print("Insufficient Balance!!")
        else:
            self.bal-=bal
    def display(self):
        print("Account Number:",self.ac)
        print("Name:",self.name)
        print("Account Type:",self.atype)
        print("Account Balance:",self.bal)

ac=int(input("Enter Your Account Number:"))
name=input("Enter Your Name:")
atype=input("Enter  Your Account Type:(s/c)")
b1=bank(ac,name,atype)
while(True):
    print("Enter your Choice:")
    print("1:Deposit")
    print("2:Withdraw")
    print("3:View Details")
    print("4:Exit")
    c=int(input())
    if(c==1):
        amount=int(input("Enter the Amount to Deposit:"))
        b1.deposit(amount)
    if(c==2):
        amount1=int(input("Enter the Amount to Withdraw:"))
        b1.withdraw(amount1)
    if(c==3):
       b1.display()
    if(c>=4):
        break

           
