a=int(input("Enter the quantity: "))

if a < 10:
    p = 120

elif a < 100:
    p = 100

else:
    p = 70    

print("The total bill amount is",p*a) 
