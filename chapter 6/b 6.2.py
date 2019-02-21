s = input("Enter the string: ")
Sum = 0
digits = ''

for i in s:
    if i.isdigit():
        digits = digits + " " + i
        Sum += eval(i)
    else:
        pass

if digits == '':
    print(s,"has no digits")
else:
    print(s,"has digits",digits,"and there sum is",Sum)        
    
