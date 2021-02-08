for item in ['Tien', 'Sarah', 'Ivan', "Jen"]:
    print(item)

for i in range(1,10):
    print(i)

nums = [1,2,3,4,5,6,7,8]
for i in enumerate(nums):
    print(i)

prices = [10,20,30]
total = 0
for price in prices:
    total += price
print(f'Total: {total}')

for x in range(4):
    for y in range(3):
        print(f'({x},{y})')