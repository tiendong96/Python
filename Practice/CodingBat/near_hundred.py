#Given an int n, return True if it is within 10 of 100 or 200. 
#Note: abs(num) computes the absolute value of a number.

def near_hundred(n):
    return ((abs(100 - n) <= 10) or (abs(200-n) <= 10))

if __name__ == '__main__':
    print(near_hundred(93)) #true
    print(near_hundred(90)) #true
    print(near_hundred(89)) #false