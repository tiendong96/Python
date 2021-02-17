#Given a string, return a new string where the first and last chars have been exchanged.

def front_back(str):
    if len(str) <= 1:
        return str
    mid = str[1:-1]
    return str[len(str)-1] + mid + str[0]

if __name__ == '__main__':
    print(front_back('code')) #'eodc'
    print(front_back('a')) #'a'
    print(front_back('ab')) #'ba'