#if temperature is greater than 80 
#   it's a hot day
# otherwise if it's less than 60
#   it's a cold day
# otherwise
#   it's neither hot nor cold

#same as Java

def yourDay(temperature):
    if(temperature > 80):
        print("It's a hot day.")
    elif(temperature < 60):
        print("It's a cold day.")
    else:
        print("It's neither hot nor cold")


if __name__ == '__main__':
    temperature = 74 #in fahrenheit
    yourDay(temperature)

    
