# if it's hot 
#   It's a hot day
#   Drink plenty of water
# Otherwise if it's cold
#   It's a cold day
#   Wear warm clothes
# otherwise
#   It's a lovely day

def ifconditions(hot, cold):
    is_hot = hot
    is_cold = cold
    if(is_hot == True):
        print("It's a hot day")
        print("drink plenty of water")
    elif(is_cold == True):
        print("It's a cold day")
        print("Wear warm clothes")
    else:
        print("It's a lovely day")
    print("Enjoy your day")

if __name__ == '__main__':
    hot = False
    cold = False
    ifconditions(hot,cold)
