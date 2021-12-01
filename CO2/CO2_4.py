from math import sqrt as s
for i in range(1000,10000):
    if s(i)==int(s(i)) and i%2==0:
        print(i,end=" ")
