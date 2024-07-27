class Customer:
    def __init__(self, name, membershipType):
        self.name = name
        self.membershipType = membershipType


#create object data
c = Customer("nafees", "Gold")


print(c.name)


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


#store objects of class dog in a list

d = [Dog("same", 3), Dog("sally", 5)]

print(d[0].age)

d[1].age = 1 #we can change values directly too./ here age is cahnged fro m 5 to 1

print(d[1].age)



############################################# modifying methods ################################################

class Customer2:
    def __init__(self,name,membershipType):
        self.name = name
        self.membershipType = membershipType

    def changeName(self, newName):
        #invoke API call
        #update a database
        #charge the customer
        #pretty much any functionalty can be added
        self.name = newName 
        
    def __str__(self):
        return self.name + " " + self.membershipType
    
    def printAllCustomer(c2):
        for c in c2:
            print(c)    
            

    def __eq__(self, other):
        if self.name == other.name and self.membershipType == other.membershipType:
            return True
        else:
            return False
    
    __repr__ = __str__
    
c2 = [Customer2("karim", "platinum"), Customer2("jodu", "silver")]

print(c2[1]) # gives us output =   <__main__.Customer2 object at 0x0000027a293cba30> 
# to negate this. and to print entire customer data together in a string we can add def --str-- method above

Customer2.printAllCustomer(c2)

print(c2[1] == c2[0])  #def--eq-- #returns false becasuse not equal

print(c2) # needs line  __repr__ = __str__ and the def--str--method 




