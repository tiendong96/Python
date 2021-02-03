# if name is less than 3 characters long
#   name must be at least 3 characters
# otherwise if it's more than 50 characters long
#   name can be a maximum of 50 characters
# otherwise
#   name looks good!
#   greet person


def yourName(name):
    #in java you use object.length or .length() to find length of given value
    #in python you use len()
    if(len(name) < 3):
        print("Name must be at least 3 characters.")
    elif(len(name) > 50):
        print("Name can be a maximum of 50 characters.")
    else:
        print("Name looks good!")
        print(f'Hello {name}!')

if __name__ == '__main__':
    name = input("What is your name?: ")
    yourName(name)