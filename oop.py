class Factory:
    def __init__(self, material, zips, pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets

    def show(self):
        print(f"The object details are {self.material}, {self.zips}, {self.pockets} ")

    

    

reebok= Factory("leather",3,2)
reebok.show()
print(f"The factory reebok material is {reebok.material} and Zips are: {reebok.zips} and pockets are: {reebok.pockets}")




class Animal:
 
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Hello my name is {self.name} " )


lion = Animal("lion")
lion.show()


class Human(Animal):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age

    
    def show(self):
        print(f"Hello my name is {self.name} and my age is {self.age}")

person1  = Human("person1","person2")
person1.show()
animal1= Animal("animal1")
animal1.show()


def decorate(func):
    def wrapper(a,b):
        print("I will print before")
        func(a,b)
        print("i will print after")
    return wrapper   



@decorate
def addition (a,b):
    print(f"Hello here i am and the addition is {a+b}")

addition(12,15)
