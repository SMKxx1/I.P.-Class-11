s = input("Enter an integer and a string: ")
s = s.split(" ")
List = []


if s[0].isdigit:

    for i in s[1]:
        if i.isdigit():
            List.append(i)
        else:
            pass
    
    if List != []:
        List = ''.join(List)
        Sum = s[0] + "+" + List
        Sum = eval(Sum)
    else:
        pass

    print(s[0],"+",List,"=",Sum)
    
else:
    print("The integer at the beginning is missing")
