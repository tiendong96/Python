#Write a python program to get a string form a given string where all occurrences of its first char have been changed to '$', except the first char itself
#sample: Restart
#expected: Resta$t

def change_char(str1):
  char = str1[0]
  str1 = str1.replace(char, '$')
  str1 = char + str1[1:]

  return str1

print(change_char('restart'))

#my version that is shorter
def moneySign(word):
    return word[0] + word[1:].replace(word[0], '$')

print(moneySign('restart'))