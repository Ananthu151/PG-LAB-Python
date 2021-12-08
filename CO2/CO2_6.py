n=input("Enter the String")
f={}
for i in n:
    if i in f:
        f[i]=f[i]+1
    else:
        f[i]=1
print("Count:",f)
