items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

#filter this list and only get the items with price >= 10
#we use the lambda function and send it a conditional which will return a boolean
#for the second parameter we send it the iterable
#the lambda function will apply to each item of the iterable and return the values that are true
#then by using the list() function, create a list with those values

filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)