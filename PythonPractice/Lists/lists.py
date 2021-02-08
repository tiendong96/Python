# names = ['John','Bob','Tien', 'Amanda']
# print(names[2:]) #print starting at index 2
# print(names[:2]) #print ending at index 2
# names[2] = 'Dong'
# print(names)

#Write a program to find the largest number in a list

def largestNum(list):
    #with inbuilt functions
    # maxNum = max(list)
    # return maxNum

    #without inbuilt functions
    maxNum = list[0]

    for i in list[1:]:
        if maxNum < i:
            maxNum = i
        firstNum = i
    print(f'The largest number is: {maxNum}')


if __name__ == '__main__':
    list = [4,8,6,34,64,12,7,2,25]
    largestNum(list)