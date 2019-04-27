def main():
  p = eval(input("Enter the amount of loan: "))
  r = eval(input("Enter the interest rate: "))
  n = eval(input("Enter the duration in month: "))
  if valid(p,n,r) == True:
    monthlyPaid = round (monthlyCal(p, r, n),2)
    interestPaid = interestCal(n, monthlyPaid, p)
  else:
    print("------- ENTER POSITIF NUMBER -------")
    main()

  print("Monthly Payment: RM {0:0,.2f} ".format(monthlyPaid))
  print("Total interest paid: RM  {0:0,.2f}".format(interestPaid))

def valid(p,n,r):
  if p >= 0 and n >= 0 and r >= 0 and r <= 100:
    return True
  else:
    return False

def monthlyCal (p, r, n):
  r = r/(12*100)
  monthlyPayment = (p*r)/(1-((1+r)**-n))
  return monthlyPayment

def interestCal (n, monthlyPayment, p):
  interest = n * monthlyPayment - p
  return interest

main()
