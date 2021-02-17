# def multipy(x, y):
#     return x * y

# multipy(2,3)
#if we wanted to use more values like multiply (2,3,4,5) there isn't the correct amount of arguments for the function
#to solve this problem replace x,y with a single parameter. in this case replace it with *numbers. Giving it a plural 
#name indicates that it is a collection of arguments and prefix it with an asterisk

#[2,3,4,5] is a list and (2,3,4,5) is a tuple (a collection of objects) we cannot modify this tuple
#tuples are iterable like a list

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

value = multiply(2,3,4,5)
print(value)