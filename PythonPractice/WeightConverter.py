
def converter(weight, metric):
    newWeight = 0
    if(metric.lower() == 'l'):
        newWeight = weight * .45
        print(f'You are {newWeight} kgs')
    else:
        newWeight = weight / .45
        print(f'You are {newWeight} lbs')

if __name__ == '__main__':
    weight = float(input("Weight: "))
    metric = input("(L)bs or (K)g: ")
    converter(weight, metric)