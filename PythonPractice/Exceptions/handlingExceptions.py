try:
    age = int(input("Age: "))
    xfactor = 10/age
except(ValueError, ZeroDivisionError): #can add many exceptions to one line if the message is going to be the same, or else, you'll have to change each message
    print("You didn't enter a valid age.")
# except ZeroDivisionError:
#     print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown")

#when python excutes the try block, if any of the code throws an exception it will ignore other exceptions 
