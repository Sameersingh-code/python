class new:
    name = "sameer"
    occupastion = "software engineer"
    salary = 99
    def info(self): #self is use to assign the value of object eg that a,b
        print(f"{self.name} is a {self.occupastion}")
        
    
#object :  creating object by class and object is  just like a copy
a = new()
a.name = "rohan" # this way we are assigning value of object
#print(a.name) # this way to print the value of object 
a.occupastion = "web developer"
b = new()
b.name = "manav"
b.occupastion = "Full stack webdev"
a.info()
b.info()
c  = new()
c.info()
# rohan is a web developer
# manav is a Full stack webdev
# sameer is a software engineer
