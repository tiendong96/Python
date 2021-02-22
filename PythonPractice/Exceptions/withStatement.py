try:
    #with open("app.py") as file, open("another.txt") as target: how to open multiple files  
    with open("app.py") as file:  
        print("File opened.") #with statement will automatically call file.close whether we have a finally clause or not
        #file.__enter__
        #file.__exit__ #context management protocol, we can use the object with the with statement
    age = int(input("Age: "))
    xfactor = 10/age
except(ValueError, ZeroDivisionError): 
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown")