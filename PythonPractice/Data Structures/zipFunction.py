list1 = [1,2,3]
list2 = [10,20,30]

# how do we combine the lists into a single list like below?
# [(1,10),(2,20),(3,30)]

print(list(zip("abc", list1,list2)))

