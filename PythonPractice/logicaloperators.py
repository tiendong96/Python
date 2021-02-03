#if applicant has high income AND good credit
#   eligible for loan

#if applicant has high income OR good credit
#   eligible for loan

# and
# or
# not

#if applicant has high income AND good credit AND doesn't have a criminal record
#   Eligible for loan

def loan(income, credit, criminalRecord):
    if(income >= 100000 and credit > 500):
        print("Eligible for loan")
    if(income >= 100000 or credit > 500):
        print("Eligible for loan")
    if(income >= 100000 and credit > 500 and criminalRecord == False):
        print("Eligible for loan")

if __name__ == '__main__':
    income =  120000 #60000 #100000
    credit = 678 #345
    criminalRecord = False
    loan(income, credit, criminalRecord)