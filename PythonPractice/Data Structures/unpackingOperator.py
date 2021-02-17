numbers = [1,2,3]
print(numbers)
#what if we want 1 2 3, we can achieve this with unpacking
print(*numbers) #in java it's like ...

#useful for lists
values1 = list(range(5))
values2 = [*range(5), *"Hello"] #we can unpack any iterable
print(values1)
print(values2)

first = [1,2]
second = [3]
values = [*first, "a", *second, *"Hello"]
print(values)

#for dictionaries
first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z" : 1} 
print(combined)

#we can use unpacking operator to take out values in any iterable