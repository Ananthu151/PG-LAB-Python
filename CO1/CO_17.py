import operator
d={1:1,2:2,3:3,4:4}
print("Dictionary in ascending order:")
da=sorted(d.items(),key=operator.itemgetter(1))
print(da);
print("Dictionary in discending order:")
dd=sorted(d.items(),key=operator.itemgetter(1),reverse=True)
print(dd);

