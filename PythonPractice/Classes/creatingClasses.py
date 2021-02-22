#Class: blueprint for creating new objects
#Object: instance of a class

# Class: Human
# Objects: John, Mary, Jack

class Point: #Pascqal naming convention
    def draw(self): 
        print("draw")


point = Point()
print(type(point)) #__main__ name of our module

print(isinstance(point,Point)) #we have an object and we need to know if it's an instance of an object of a class

