class Sample:
    __a=30
    b=40

    def __init__(self,c,d):
        self.__c=c
        self.d=d

    def __update_c(self,new):
        self.c=new

class child(Sample):
    pass