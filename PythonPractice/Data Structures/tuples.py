point = 1
print(type(point)) #<class 'int'>

point2 = 1,
print(type(point2)) #<class 'tuple'>

point3 = (1,2) + (3,4) #concatenate
print(point3) 

point4 = (1,2) * 3 #repeat
print(point4)

point5 = tuple("Hello World")
print(point5)

#we can treat tuples like lists
point6 = (1,2,3,10)
w,x,y,z = point6
if 10 in point6:
    print("exists")
point6[0] = 10

#where do we use tuples
#when we deal with a sequence of numbers that we don't want to mess up 