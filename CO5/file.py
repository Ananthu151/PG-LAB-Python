f1=open("firstfile.txt","w")
f1.write("This is my first file in python.\nwant to work with file\nThis is my third line")
f1.close()
f1=open("firstfile.txt","r")
print("Name of File:",f1.name)
print("Close of File:",f1.closed)
print("Mode of File:",f1.mode)
print(f1.read())
f1.seek(0,0)
#print(f1.read(50))
print("///////////////////////////")
print(f1.readline())
print("--------------------")
print(f1.readline())
f1.seek(0,0)
ff=f1.readlines()
print(ff)
print("No. of lines",len(ff))
f1.seek(0,0)
import os
#os.rename("firstfile.txt","secfile.txt")
print(f1.name)
f1.close()

