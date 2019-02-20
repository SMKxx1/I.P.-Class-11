List = []
count = int(input("Enter the length of the list: "))

for i in range(count):
    num = int(input(">>> "))
    List.append(num)

Sum = 0

for i in List:
    Sum += i

avg = Sum/len(List)

print("The average is",avg)
 
