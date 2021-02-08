#given a list of numbers, print the even numbers and finally print how many even numbers were found

count = 0
for num in range(1,10):
    if(num % 2 == 0):
        #if num has 0 remainder means that it's divisible by 2 evenly
        print(num)
        count += 1
print(f'We have {count} even numbers!')