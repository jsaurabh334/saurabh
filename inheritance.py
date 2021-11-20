class me:
    def __init__(self,name,age,salary) :
        self.name=name
        self.age=age
        self.salary=salary

   

    @classmethod

    def from_str(cls,string1):
        param=string1.split("-")
        return cls(param[0],param[1],param[2])



saurabh= me("saurabh",22,15000)
rohan= me("saurabh",22,15000)
mohan=me.from_str("mohan-22-2000")
# print(f"{saurabh.name} {saurabh.age} {saurabh.salary}")
print(f"{mohan.name} {mohan.age} {mohan.salary}")

class me2(me):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)


sj=me2("saurabh",22,15000)

print(f"{sj.name} {sj.age} {sj.salary}")


