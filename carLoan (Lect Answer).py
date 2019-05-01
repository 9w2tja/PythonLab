def main():
    (amountLoan, annualInt, payDurations)=inputs()
    monthlyPay=calcMonPay(amountLoan, annualInt, payDurations)
    totalInt=calcTotalInt(monthlyPay,amountLoan,payDurations)
    displayOutput(monthlyPay, totalInt)

def inputs():
    while True:
        inputLoan = float(input("Enter the amount of the loan" + 
                            "(minimum loan is 1000:"))
        if validateLoan(inputLoan)==True:
            break;
    while True:
        inputAnInt = float(input("Enter the annual interest rate " +
                             "(minimum annual interest is 2%):"))
        if validateInt(inputAnInt)==True:
            break;
    while True:
        inputDur= int(input("Enter the durations of payment in months" +
                        "(minimum duration of payment is 1 month):"))
        if validateMon(inputDur)==True:
            break;
    return inputLoan,inputAnInt,inputDur
    
    
def validateLoan(loan):
    if loan >= 1000 :
        return True
    else:
        return False
    
def validateInt(interest):
    if interest >= 2 and interest <=100 :
        return True
    else:
        return False
    
def validateMon(months):
    if months >=1 :
        return True
    else:
        return False
     
def calcMonPay(aLoan, aInt, payDur):
    mInt = calcMonInt(aInt)
    return (aLoan * mInt)/(1-(1+mInt)**-payDur)
     
def calcMonInt(annInt):
    return annInt/(12*100)
                                 
def calcTotalInt(monthPay,loanAmount, monthDur):
    return monthDur*monthPay-loanAmount

def displayOutput(monthlyPay, totalInt):
    print("Monthly payment of the loan is RM {0:.2f}".format(monthlyPay))
    print ("Total interest payment for the loan is {0:,.2f}".format(round(totalInt)))


main()



                           
