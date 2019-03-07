def Future_value(p,r,n,t):
    FV = p*(1+r/n)**(n*t)
    FV = round(FV)
    print("The future value is:",FV)
    return FV

def Present_value(r,FV,n,t):
    PV = FV / (1+r/n)*t*n
    PV = round(PV)
    print("The present value is:",PV)
    return PV

def Total_compound_interest(p,r,n,t):
    TCI = p*(1+r/n)**(n*t) - p
    TCI = round(TCI)
    print("The Total Compound Interest is:",TCI)

p = int(input("Enter the principal value: "))
r = int(input("Enter the rate: "))
r = r/100
n = int(input("Enter the number of times the interest is compounded: "))
t = int(input("Enter the number of years the money is invested: "))

FV = Future_value(p,r,n,t)

PV = Present_value(r,FV,n,t)

Total_compound_interest(p,r,n,t)