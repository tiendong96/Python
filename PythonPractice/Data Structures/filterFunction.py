items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

#filter this list and only get the items with price >= 10

filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)