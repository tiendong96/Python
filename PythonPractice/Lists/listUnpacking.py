numbers = [1,2,3,4,4,4,4,4]
first, second, third, *other = numbers
print(first)
print(second)
print(third)
print(other)

letters = ["a","b","c"]
items = (0, "a")
index, letter = items
for letter in enumerate(letters):
    print(letter[0], letter[1]) 
    
print()

for index, letter in enumerate(letters):
    print(index, letter)
