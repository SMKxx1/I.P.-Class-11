a = int(input("Enter the value of the first number: "))
b = int(input("Enter the value of the second number: "))
c = int(input("Enter the value of the third number: "))

if a > b and a > c:
    if b > c:
        print("The Smallest number: ",c)
        print("The Next higher number: ",b)
        print("The Highest number: ",a)
    else:
        print("The Smallest number: ",b)
        print("The Next higher number: ",c)
        print("The Highest number: ",a)

elif b > a and b > c:
    if a > c:
        print("The Smallest number: ",c)
        print("The Next higher number: ",a)
        print("The Highest number: ",b)
    else:
        print("The Smallest number: ",a)
        print("The Next higher number: ",c)
        print("The Highest number: ",b)

else:
    if a > b:
        print("The Smallest number: ",b)
        print("The Next higher number: ",a)
        print("The Highest number: ",c)
    else:
        print("The Smallest number: ",a)
        print("The Next higher number: ",b)
        print("The Highest number: ",c)
