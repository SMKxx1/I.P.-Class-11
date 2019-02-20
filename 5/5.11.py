n = int(input("Enter a number > 20: "))


if n > 20:
    for i in range(11,n+1):
        if i % 3 == 0 and i % 7 == 0:
            print(i,'TipsyTopsy')
        elif i % 3 == 0:
            print(i,'Tipsy')
        elif i % 7 == 0:
            print(i,'Topsy')
        else:
            print(i)
else:
    print("Number is smaller then or equal to 20")
 
