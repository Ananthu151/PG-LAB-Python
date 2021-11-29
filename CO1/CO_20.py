num = [7,8, 120, 25, 44, 20, 27]
print( "Original list:",num)
n=[]
for x in num:
    if x%2!=0:
        n.append(int(x))
num=n
print("Final result:",n)
