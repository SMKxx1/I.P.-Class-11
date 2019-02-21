List = []

while True:
    a = input("Enter a number or press 'q' to stop: ")
    if a != 'q' and a.isdigit():
        List.append(eval(a))
    elif a == 'q':
        break
    else:
        print("Invalid input")

for i in List:
    if i > 10:
        List.insert(List.index(i),10)
        List.remove(i)
    else:
        pass
print(List)
        
