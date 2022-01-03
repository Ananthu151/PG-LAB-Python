class time:
    def __init__(self,hour,minute,second):
        self.__hour=hour
        self.__minute=minute
        self.__second=second
    def __add__(self,t2):
        h=self.__hour+t2.__hour
        m=self.__minute+t2.__minute
        if(m>60):
            q=int(m/60)
            r=m%60
            h=h+q
            m=r
        s=self.__second+t2.__second
        if(s>60):
            q1=int(s/60)
            r1=s%60
            m=m+q1
            s=r1
        return(h,m,s)
print("Enter Time 1:")
h1=int(input("Hour:"))
m1=int(input("Minute:"))
s1=int(input("Second:"))
t1=time(h1,m1,s1)
print("Enter Time 2:")
h2=int(input("Hour:"))
m2=int(input("Minute:"))
s2=int(input("Second:"))
t2=time(h2,m2,s2)
h,m,s=t1+t2
print("Sum of two Times:",h,":",m,":",s)

