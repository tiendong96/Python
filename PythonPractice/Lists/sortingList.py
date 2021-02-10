# numbers = [3,51,2,8,6]
# #numbers.sort() #ascending
# #numbers.sort(reverse=True) #descending
# print(sorted(numbers, reverse=True))
# print(numbers)

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]
#we create a function that helps us later to sort the the list by the price. 
#here we are returning the price and then passing it to the sort() metho
def sort_items(items):
    return items[1]

#by using sort_items() we can pass it as a key to sort() which will go through each of the item's passed (price) and sort it in ascending values
items.sort(key=sort_items)
print(items)