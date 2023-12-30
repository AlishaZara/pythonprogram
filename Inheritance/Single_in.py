class Base:
    a=10
    b=20
    def __init__(self,c):
        self.c=c

class derived(Base):
    def __init__(self,c,d,e):
        Base.__init__(self,c)
        self.d=d
        self.e=e
    
obj=derived(6,56,58)