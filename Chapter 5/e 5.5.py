a = int(input("Enter the length of side 1: "))
b = int(input("Enter the length of side 2: "))
c = int(input("Enter the lenght of side 3: "))

if a+b > c and b+c > a and c+a > b:
    print("It can form a triangle")
else:
    print("It can't form a triangle")
