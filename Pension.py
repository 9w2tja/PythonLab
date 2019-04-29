yrs =0
def main():
    InputAge = int(input("Enter your age: "))
    InputNumberOfMonths = int(input("Enter number of months of service: "))
    InputFirstSalaries = float(input("Enter first of three highest salaries: "))
    InputSecondSalaries = float(input("Enter second of three highest salaries: "))
    InputThirdSalaries = float(input("Enter third of three highest salaries: "))

    yrs = round(NumberOfMonths(InputNumberOfMonths),0)

    if canRetire(InputAge, yrs) == True:
        ave = round(AverageAnnualSalary(InputFirstSalaries, InputSecondSalaries, InputThirdSalaries),2)
        p = round(minPerRate(yrs),2)
        amountPension = round(pension(p, ave),2)
        output(amountPension)
    else:
        print("--- Can Retire at age 55 with at least 20 years of service ---")
        main()
        
def canRetire(Age, Month):
    if Age >= 55 and Month >= 20:
        return True
    else:
        return False

def AverageAnnualSalary(firstS, secondS, thirdS):
    return (firstS + secondS + thirdS)/3

def NumberOfMonths(months):
    return months/12

def percentageRate(year):
    if year <= 5:
        rate = 0.015 * year
    elif year <= 10:
        rate = (0.015 * 5) + (0.0175 * (year-5))
    else:
        rate = (0.015 * 5) + (0.0175 * 5) + (0.02 * (year-10))
    return rate

def minPerRate(yearRate):
    minRate = round(percentageRate(yearRate),2)
    if minRate <= .8:
        return minRate
    else:
        return .8

def pension(p, ave):
    return p * ave
    
def output(amountPension):
    print("Annual pension: ${0:0,.2f}".format(amountPension))

main()

