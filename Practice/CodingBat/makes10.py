#Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

def makes10(a,b):
    return ((a == 10 or b == 10) or (a + b == 10))

if __name__ == '__main__':
    print(makes10(9,10)) #true
    print(makes10(9,9)) #false
    print(makes10(1,10)) #true