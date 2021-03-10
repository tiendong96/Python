#write a program which accepts the user's first and last name and prints them in reverse order wiht a space between them

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
reversed_name = first_name + " " + last_name

print(f'Hello {first_name} {last_name}, your name printed in reverse is: {reversed_name[::-1]}')

#optimized and shorter lines of code

name = input("Enter your name: ")

print(f'Hello {name[::-1]}')