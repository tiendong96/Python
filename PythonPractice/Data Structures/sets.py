#set is an unordered collection of unique items, we cannot have duplicates.
numbers = [1,1,2,3,4]
first = set(numbers)
second = {1, 5}
# second.add(5)
# second.remove(5)
# len(second)
print(first | second) #can use union of the two sets and return a new set that are either in both first or second set
print (first & second) #return a new set that includes items that are in both first and second
print(first - second) #difference between two sets
print(first ^ second) #symmetric difference in first or second but not both

#set does not support indexing

if 1 in first:
    print("yes")