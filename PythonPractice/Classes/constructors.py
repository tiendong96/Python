class Point:
    default_color = "red"

    def __init__(self, x, y): #magic method for creating constructor, always have self for convention
        self.x = x #instance attributes
        self.y = y 

    def draw(self):
        print(f"Point ({self.x}, {self.y})")

Point.default_color = "yellow"

point = Point(1, 2)
print(point.default_color)
print(Point.default_color)
print(point.x)
point.draw()

#self is a reference to the current object
#when calling methods of an object we never have to supply values for the parameter, python interpreter does that for us

another = Point(3,4)
print(another.default_color)
another.draw()