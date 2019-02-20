count = int(input("Enter the number of employees: "))
ages = []
for i in range(1,count+1):
    print("Enter the age of the employee",i)
    age = int(input("> "))
    ages.append(age)

Range_1 = 0
Range_2 = 0
Range_3 = 0

for i in ages:
    if i >= 26 and i <= 35:
        Range_1 += 1
    elif i >= 36 and i <= 45:
        Range_2 += 1
    elif i >= 46 and i <= 55:
        Range_3 += 1
    else:
        pass

print("Number of employees between the age of 26 and 35 are",Range_1)
print("Number of employees between the age of 36 and 45 are",Range_2)
print("Number of employees between the age of 46 and 55 are",Range_3)
    
