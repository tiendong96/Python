first = 'John'
last = 'Smith'
message = first + ' [' + last + '] ' + "is a coder"
#John [Smith] is a coder

print(message)

#this is requires the coder to visualize what they are reading
#use formatted strings to combat this
msg = f'{first} [{last}] is a coder' #curly braces denote variables or "holes" where the compiler will add in a value
print(msg)

#self-attempt
name = 'Tien'
degree = 'Bachelors'
age = 25
language = 'Python'

myMSG = f'Hello everyone, my name is {name} I am {age} and I am currently learning {language}'
print(myMSG)