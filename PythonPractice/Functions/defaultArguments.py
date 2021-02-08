#making part of the parameter(s) optional

def increment(number, by=1):
    return number + by

print(increment(2)) #if we call the function like this, the default value assigned in the function will be used: by=1 
#this is called default arguments

print(increment(2,5)) #notice how here it'll use the value of 5 instead of default value 1
#when using default arguments, make sure that the default arguments come after the required parameter
# def increment(number, by=1, anotherVariable) will NOT work 
print(increment(2,5))
