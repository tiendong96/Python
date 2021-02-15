from array import array 
numbers = array('i', [1,2,3]) #typecode: a string that determines the type of objects in your array, google python3 typecode. It will display a table of typecodes in Python. 'b' signed character etc etc
#we can remove and append like a list
numbers.remove(2)
numbers.pop()
numbers.append(3)
#because the type of this array is of type integer, we can not use methods to add other types.
#numbers[0] = 1.0 will return an error

#use array only if youre using large sequence of numbers and encountering performance problems, by default use tuples and lists by default
print(numbers)

