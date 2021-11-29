n=[]
s=int(input("Enter a limit of numbers:"))
print("Enter  values:")
for i in range(0,s):
    n.append(int(input()))
print("\nThe list after assinging:\n")
for i in range(0,len(n)):
    if n[i]>=100:
        print("over")
    else:
        print(n[i]) 
