#write code that looks at a string of words and finds the most repeated character

from pprint import pprint

sentence = "This is a common interview question"

#the best way to do this is using key:value pairs 
#here I am setting up an empty dictionary to keep track of everything
char_dictionary = {}

#traverse the string 
for char in sentence:
    #if character exists in dictionary, increment the value
    if char in char_dictionary:
        char_dictionary[char] += 1 #if char exists in dictionary, wherever the char is found index-wise increment 1
    else:
        char_dictionary[char] = 1

#because dictionaries and sets are unordered collections, we can't sort it
#so to sort it, we need to make each key:value a tuple and put it into a list

char_dictionary_sorted = (sorted( #I call sorted() to create tuples from char_dictionary
    char_dictionary.items(), 
    key=lambda kv:kv[1],  #lambda function that takes key value pair and returns value
    reverse=True))

print(char_dictionary_sorted[0])