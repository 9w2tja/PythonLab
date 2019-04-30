def main():
    inputAge = int(input("Enter your age: "))
    inputMonths = int(input("Enter number of months of service: "))

    #print(retiredAge(inputAge))
    #print(monthService(inputMonths))
    #print(canRetied(inputAge, inputMonths))
    
    if canRetied(inputAge, inputMonths) == True:
        inputFirstSalaries = float(input("Enter first of three highest salaries: "))
        inputSecondSalaries = float(input("Enter second of three highest salaries: "))
        inputThirdSalaries = float(input("Enter third of three highest salaries: "))

        #print(averageSalary(inputFirstSalaries, inputSecondSalaries, inputThirdSalaries))
        ave = averageSalary(inputFirstSalaries, inputSecondSalaries, inputThirdSalaries)

        #print(monthService(inputMonths))
        yrs = monthService(inputMonths)

        #print(perRate(yrs))
        p = perRate(yrs)

        #print(pension(p, ave))
        amountPension = pension(p, ave)
        print("Annual pension: ${0:0,.2f}".format(amountPension))

    else:
        print("--- Can Retire at age 55 with at least 20 years of service ---")
        main()

def retiredAge(age):
    if age >= 55:
        return True
    else:
        return False

def monthService(month):
    return month/12

def canRetied(age, month):
    if retiredAge(age) == True:
        if monthService(month) >= 20:
            return True
        else:
            return False
    else:
        return False
        
def averageSalary(first, second, third):
    return (first + second + third)/3

def perRate(year):
    rate = ((1.5 * 5) + (1.75 * 5) + (2.0 * (year - 10))) /100
    return maxRate(rate)

def maxRate(rate):
    if rate <=.8:
        return rate
    else:
        return .8

def pension(p, ave):
    return p * ave

main()
