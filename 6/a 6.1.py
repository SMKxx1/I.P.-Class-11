print("Enter the number is the following format xxx-xxx-xxxx")
num = input("> ")

if len(num) == 12 and num[3] == '-' and num[7] == '-':
    if num[:3].isdigit() and num[4:7].isdigit() and num[8:].isdigit:
        print("The number is valid number")
    else:
        print("The number is Invalid number")
else:
    print("The number is Invalid number")
