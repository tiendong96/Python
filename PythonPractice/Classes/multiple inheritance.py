class Employee:
    def greet(self):
        print("Employee greet")

class Person:
    def greet(self):
        print("Person greet")

class Manager (Employee, Person): #multiple inheritance
                                  #this is bad because someone could come in and change the order of the inheritance and change the behavior
    pass

m = Manager()
m.greet()

# the code below shows a good example of multiple inheritance. This is good because both classes supply different methods
# so whether it's a flying fish or a swimming bird, it doesn't matter the order of inheritance
class Flyer:
    def fly(self):
        pass

class Swimmer:
    def swim(self):
        pass

class FlyingFish(Flyer, Swimmer):
    pass
