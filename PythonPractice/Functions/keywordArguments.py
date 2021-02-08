def increment(number,by):
    return number + by

#in this case you won't need to result variable
#result = increment(2, 1)
print(increment(2,1)) #python will temporarily store the value in a variable created by python interpreter

#if youre working with a lot of arguments and it's not quite clear what the arguments are for
#you can assign the arguments by the parameter name
#this is called keyword arguments
print(increment(number=2,by=1))