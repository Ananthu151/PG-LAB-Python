class bank:
    def __init__(self,ac,name,atype,bal=0):
        self.ac=ac
        self.name=name
        self.atype=atype
        self.bal=bal
    def deposit(self,bal):
        self.bal+=bal
    def  withdraw(self,bal):
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
amount=int(input("Enter the Amount to Deposit:"))
b1.deposit(amount)
amount1=int(input("Enter the Amount to Withdraw:"))
b1.withdraw(amount1)
b1.display()

           
