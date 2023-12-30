class Car:
    name="car"
    def __init__(self,name,milege,price,color):
        self.name=name
        self.milege=milege
        self.price=price
        self.color=color

class Supra(Car):
    pass

class BMW(Car):
    pass

c1=Supra("supra mk4",10,50000,"black")
c2=BMW("bmw m4",15,5000000,"white")