#a collection of key value pair. We use it to map key to values.
#an example would be a phonebook name -> contact

point = {"x" : 1, "y" : 2} 

#we can also use the dict() function to create a dictionary

point2 = dict(x=1, y=2)

#get value associated with a key 
print(point2["x"])
point2["x"] = 10
print(point2["x"])
point2["z"] = 20
print(point2["z"])

#if we use an invalid key, we will get an error
#print(point2["a"])
#check for existance of a key
if "a" in point2:
    print(point2["a"])

#or we can use get method
print(point2.get("a", 0)) #by default get() will return None if it does not exist, the second argument is used to set the default

#to delete a key
del point2["x"]
print(point2)

#how to loop over dictionaries
for key in point2:
    print(key, point2[key])
#or 
for key, value in point2.items():
    print(key, value)