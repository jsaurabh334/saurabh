class classname:
    age=24
    def _println(self):
        print(f"saurabh is here {self.age} yrs old and he is {self.surname}")


saurabh= classname()
saurabh.age=22
saurabh.surname="jain"
print(saurabh.age) #this is how you call an instance variable 
rohan= classname()
print(rohan.age) #this is how you call a class variable 

saurabh._println()



