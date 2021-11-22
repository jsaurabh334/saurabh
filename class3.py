# class me:
#     def __init__(self,name,age,salary) :
#         self.name=name
#         self.age=age
#         self.salary=salary

#     def printdet(self):
#         print(f"{self.name} {self.age} {self.salary}")



# saurabh= me("saurabh",22,15000)
# # print(f"{saurabh.name} {saurabh.age} {saurabh.salary}")

# saurabh.printdet()



class computer:
     def __init__(self,schoolname,studentname,age,section):
         self.schoolname = schoolname
         self.studentname = studentname
         self.age = age
         self.section = section

     def details(self):
        print(f"{self.schoolname} {self.studentname} ")

aryan= computer("dav","aryan",20,"A")
# print(aryan.schoolname,aryan.studentname,aryan.age)
aryan.details()




