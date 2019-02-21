def con():
    z = int(input("Enter the length in CM: "))
    if z >= 0:
        print(z/2.54,"Is the length in inches")
    else:
        print("Invalid")
        input()
        con()
con()
 

