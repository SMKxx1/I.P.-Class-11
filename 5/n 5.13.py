List = []
count = int(input("Enter the amount of numbers to be enter: "))

for i in range(count):
    num = int(input(">>> "))
    List.append(num)
    
List.sort(reverse = True)
print("The second largest number is",List[1]) 
