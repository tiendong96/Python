#there may be times when youre working with infinite streams of data and you shouldn't be storing all the values into memory
#more efficient to use a generator object
#gen objects are iterable, and each iteration they spit out a new value, so they do not store into memory
from sys import getsizeof #to get the size of object

values = [x * 2 for x in range(10)] 
for x in values:
    print(x)
print(type(values))
print()

#by changing the square brackets to parentheses
values2 = (x * 2 for x in range(10)) 
for x in values:
    print(x)
print(type(values2))
print()

#we can see that the size stays consistent no matter the range we give it
values3 = (x * 2 for x in range(1000000000000000000000)) 
print("gen:", getsizeof(values3))

values3 = [x * 2 for x in range(100000)] 
print("list:", getsizeof(values3))


