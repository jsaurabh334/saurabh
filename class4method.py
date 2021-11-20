class me:
    no_holiday=8
    def __init__(self,name,age,salary) :
        self.name=name
        self.age=age
        self.salary=salary

    def printdet(self):
        print(f"{saurabh.name} {saurabh.age} {saurabh.salary}")

    @classmethod

    def noh(cls,newleaves):
        cls.no_holiday=newleaves



saurabh= me("saurabh",22,15000)
rohan= me("saurabh",22,15000)
# print(f"{saurabh.name} {saurabh.age} {saurabh.salary}")

saurabh.noh(18)
print(rohan.no_holiday)
