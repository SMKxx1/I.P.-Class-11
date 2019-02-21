x = 0
y = 0

for i in range(1,11):
    print("Enter the Number of family members of student",i)
    f = int(input("> "))
    x += f
    print("Enter the Family income")
    f = int(input("> "))
    y += f

cc1 = (10*(x*y)-(x)*(y))/(((10*(x*x)-(x*x))*(10*(y*y)-(y*y)))**0.5)

print("The correlation coefficient is",cc)

