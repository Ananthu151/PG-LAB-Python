class point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __del__(self):
        print("Distroyed",self)

pt1=point(5,3)
pt2=point(0,0)

print(id(pt1),id(pt2))
del pt1
del pt2
