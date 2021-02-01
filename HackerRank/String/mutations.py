# https://www.hackerrank.com/challenges/python-mutations/problem?h_r=next-challenge&h_v=zen
# Read a given string, change the character at a given index and then print the modified string.

def mutations(word, position, character):
    word = word[:position] + character + word[position+1:]
    return word

if __name__ == '__main__':
    word = input() #abracadabra
    i,c = input().split()
    word_new = mutations(word, int(i), c)
    print(word_new)