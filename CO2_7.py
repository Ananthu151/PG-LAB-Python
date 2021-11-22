str=input("Enter the String")
n=len(str)
if(str[n-3:]=="ing"):
    str1=str.replace("ing","ly")
    print(str1)
else:
    str2=str+"ing"
    print(str2)

