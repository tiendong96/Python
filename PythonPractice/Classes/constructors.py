class Point:
    def __init__(self, x, y): #magic method for creating constructor, always have self for convention
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")

point = Point(1, 2)
print(point.x)
point.draw()
#self is a reference to the current object,