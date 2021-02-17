""" 
Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
"""

def diff21(n):
    num = 0
    if n > 21:
        num = abs(2*(n-21))
    else:
        num = abs(n-21)
    return num

if __name__ == '__main__':
    print(diff21(19)) #2
    print(diff21(10)) #11
    print(diff21(21)) #0
    

