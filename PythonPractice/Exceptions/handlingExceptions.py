try:
    age = int(input("Age: "))
except ValueError as ex: 
    print("You did not enter a valid age.")
    print(ex)
    print(type(ex))
else:
    print("No exceptions were thrown")