# In this challenge, the user enters a string and a substring. 
# You have to print the number of times that the substring occurs in the given string. 
# String traversal will take place from left to right, not from right to left.
# https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(string, sub_string):
    count = 0 #generic counter
    for i in range(len(string)): #traverse through the string with the range = length of string in which case is 7
        if string[i:].startswith(sub_string): #using the iterator, see if it starts with the substring. ABCDCDC start with CDC? no , next iteration, BCDCDC? no, CDCDC? yes
            count += 1 #increment if found
    return count

if __name__ == '__main__':
    string = input().strip() #ABCDCDC
    sub_string = input().strip() #CDC
    count = count_substring(string, sub_string)
    print(count) #2