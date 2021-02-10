items = [
    ("Product1",10),
    ("Product2", 9),
    ("Product3", 12),
]

x = map(lambda item: item[1], items) #lambda transforms each item in the original list, map function will iterate the iterable and call the lambda function on each iterable
#returns another iterable
print(x)

for item in x:
    print(item)

#we can convert the map to a list
prices = list(map(lambda item: item[1], items)) #lambda transforms each item in the original list, map function will iterate the iterable and call the lambda function on each iterable
print(prices)
