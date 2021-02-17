items = [
    ("Product1",10),
    ("Product2",9),
    ("Product3",12),
]

prices = list(map(lambda item: item[1], items))
# comprehension formula: [expression for item in items]
prices = [item[1] for item in items]

filtered = list(filter(lambda item: item[1] >= 10, items))

#comprehension formula: [expression for item in items]
filtered = [item for item in items if item[1] >= 10] #iterate through each of the items and then item will iterate through each of those if condition is valid