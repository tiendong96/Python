#Price of a house is $1M 
# If buyer has good credit
#   need to put 10% down
# Otherwise
#   they need to put 20% down
# Print the down payment

def downpayment(price, creditScore):
    down_payment = 0
    if(creditScore >= 700):
        down_payment = price * .1
    else:
        down_payment = price * .2
    print(f'You have paid ${down_payment}.')

if __name__ == '__main__':
    price = 1000000
    creditScore = 10
    downpayment(price, creditScore)
