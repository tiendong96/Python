def save_user(**user):
    print(user["name"])

#instead of arbitrary values
#we can send arbitrary keyword argument
save_user(id=1, name='John', age=22)
#python will package them into a dictionary and we can get various values of key and values