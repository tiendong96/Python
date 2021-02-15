values = []
for x in range(5):
    values.append(x * 2)
print("Using for loop and append")
print(values)

# comprehension: [expression for item in items] -> iterate over an iterable, in each iteration we get an item, then we do something with it
print("Using list comprehension")
values = [x * 2 for x in range(5)] # this single line of code is identical to the first 3 lines
print(values)

print("set/dictionary comprehension")
#we can also use them with sets and dictionaries, just replace square brackets with curly braces
values = {x * 2 for x in range(5)} # this single line of code is identical to the first 3 lines
print(values)

#because a dictionary is not a list, it has keys and values, we have to separate it using ':'
values = {x: x * 2 for x in range(5)} # this single line of code is identical to the first 3 lines
print(values)