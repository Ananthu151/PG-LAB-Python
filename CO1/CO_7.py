lst=[4,7,3,78,46,478,43]
lst1=[45,65,3,68,65,7,78]
s=int(0) 
c=int(0)

if len(lst)==len(lst1):
  print("same length") 
else:
  print("Different length")

for i in range(0,len(lst) and len(lst1)): 
  s=s+lst[i]
  c=c+lst1[i]
if(s==c):
  print("Equal sum")
else:
  print("Not same sum")

print("Elements in Same:") 
l=[]
for i in range(0,len(lst)):
  for j in range(0,len(lst1)):
    if lst[i]==lst1[j]:
        l.append(lst[i] and lst1[j]) 
    else:
      continue
print(l)
