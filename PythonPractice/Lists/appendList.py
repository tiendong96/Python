#how to add or remove items from list

letters = ["a","b","c"]

#Add
letters.append("d") #add at the end of the list
print(letters)

letters.insert(0,"-") #add an item at a specific position
print(letters)

#Remove
letters.pop(0) #remove at the end of the list
letters.remove("b") #remove item but you dont know the index, remove the first occurence
del letters[0:3] #delete statement can remove a range of items
letters.clear() #remove everything from a list
print(letters)