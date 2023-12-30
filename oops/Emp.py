class Employee:
    company='Tesla'
    CEO='ELON MUSK'

    def insert_member(self,name,age,sal,eid):
        self.name=name
        self.age=age
        self.sal=sal
        self.eid=eid

bhanu=Employee()
bindu=Employee()
dhoni=Employee()

Employee.insert_member(bhanu,'bhanu',22,50000,'tes01')
Employee.insert_member(bindu,'bindu',21,45000,'tes02')
dhoni.insert_member('Dhoni',45,1000000,'tes03')