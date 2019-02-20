n = int(input("Enter the range: "))
m = int(input("Enter the dividing number: "))

for i in range(1,n+1):
    if i % m == 0:
        if i % 2 == 0:
            print(i,"is divisible by",m,"and is an even number")
        else:
            print(i,"is divisible by",m,"and is an odd number")
    else:
        if i % 2 == 0:
            print(i,"is not divisible by",m,"and is an even number")
        else:
            print(i,"is not divisible by",m,"and is an odd number")
