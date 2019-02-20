a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

if b > a:
    t = a
    a = b
    b = t

else:
    pass


if (a-b) <= 0.001:
    print("Close")

else:
    print("Not close")
