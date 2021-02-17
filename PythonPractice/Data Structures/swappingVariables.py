x = 10
y = 11

# z = x #old value of x stored in z
# x = y 
# y = z

# print('x', x)
# print('y', y)

#in python we can swap without the need for a third variable
x, y = y, x #on the right side you're defining a tuple. (y, x) on the left side we are unpacking x gets assigned to y and y gets assigned to x
print('Without third variable: ')
print('x', x)
print('y', y)