#Given two int values, return their sum. Unless the two values are the same, then return double their sum.

def sum_double(a,b):
    c = 0
    if a == b:
        c = 2* (a + b)
    else:
        c = a + b
    return c

if __name__ == '__main__':
    print(sum_double(a=1, b=2)) #3
    print(sum_double(a=3, b=2)) #5
    print(sum_double(a=2, b=2)) #8
