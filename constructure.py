#constructure is a special type of fuction, we can chage the value during the program
#There is two type constructure
#default constructure
# class person:
#     def __init__(self):
#         print("Hey, I am person")
# p = person()
#parameter constructure
class idperson:
    def __init__(self,name,occ):
        self.name = name
        self.occ = occ
    def info(self):
        print(f"{self.name} is a {self.occ}")
p = idperson("rohan","engineer")
p.info()
#output : rohan is a engineer
