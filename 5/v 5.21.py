x = 0
List = []

for i in range(1,11):
    print("Enter the score in the match",i)
    f = int(input("> "))
    List.append(f)
    x += f
    
mean = x/10

u = 0
for i in List:
    u += (i - mean) ** 2

sd = (u/10)**0.5
sd = round(sd,2)
print("Standard deviation is",sd)
