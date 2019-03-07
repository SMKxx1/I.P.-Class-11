dic = {}
print("Type 'stop' to stop")
while True:
    prod = input("Enter the product name: ")
    if prod == 'stop':
        break
    else:
        pass
    pric = int(input("Enter the price: "))
    dic[prod] = pric
    print()

print()

print("Type 'stop' to stop")
while True:
    chk = input("Enter the product name: ")
    if chk == 'stop':
        break
    else:
        pass
    if chk in dic:
        print(dic[chk])
        print()
    else:
        print("No such product!!")
        print()