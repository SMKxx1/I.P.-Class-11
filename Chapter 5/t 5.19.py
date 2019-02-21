temp = float(input("Enter the Temperature in Celsius: "))

if temp < -273.15:
    print("Invalid: Temperature is below absolute 0")
elif temp == -273.15:
    print("The Temperature is absolute 0")
elif temp < 0 and temp > -273.15:
    print("The Temperature is below freezing")
elif temp == 0:
    print("The Temperature is at freezing point")
elif temp > 0 and temp < 100:
    print("The Temperature is in the normal range")
elif temp == 100:
    print("The Temperature is at boiling point")
else:
    print("The Temperature is above boiling point")
 
