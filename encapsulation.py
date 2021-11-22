class car:
    def __init__(self) :
        self.__updatesoftware()

    def driving(self):
        print("car is driving")

    def __updatesoftware(self):
         print("software is updating")

sj= car()
sj.driving()
# sj.__updatesoftware() we cannt access private functions directly
       
