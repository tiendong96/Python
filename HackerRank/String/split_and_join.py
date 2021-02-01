# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

def split_and_join(line):
    line = line.split(" ") #splits input into a list of words
    print(line)
    line = "-".join(line) #joins the list of words with a hyphen
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)