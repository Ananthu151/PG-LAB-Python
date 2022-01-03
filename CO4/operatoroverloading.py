class timecal:
    def __init__(self,h):
        self.__h=h
    def __add__(self,a):
        print(self.__h+a.__h)
    def __lt__(self,a):
        if(self.__h<a.__h):
            return(True)
    def __gt__(self,a):
        if(self.__h>a.__h):
            return(True)
    def __eq__(self,a):
        if(self.__h==a.__h):
            return(True)
a1=timecal(10)
a2=timecal(20)
a1+a2
if(a1<a2):
    print("A1 is smaller!")
else:
    print("A2 is smaller!")
if(a1>a2):
    print("A1 is bigger!")
else:
    print("A2 is bigger!")
if(a1==a2):
    print("A1and A2 is equal !")
else:
    print("A1and A2 is not equal !")
