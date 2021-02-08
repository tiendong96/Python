def greet():
    print("Hello")
    print("Welcome aboard!")

greet()

#generic function, notice how there are no parameters or arguments

#notice how this function has parameters requesting for 2 inputs
def greet(first_name, last_name):
    print(f'Hello {first_name} {last_name}')
    print("Welcome aboard!")

#now when we send arguments, the program will look for the functions with the correct parameters
greet('Tien','Dong')

# 1 - Perform a task, good for if you need to print to the terminal
#greet()

# 2 - Returns a value, if you need that value to be used elsewhere
#round(1.9)
def get_greeting(name):
    return f"Hi {name}"

message = get_greeting("Tien")
print(message)
# file = open("content.txt","w")
# file.write(message)


