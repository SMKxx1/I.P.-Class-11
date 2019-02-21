while True:
    s = input("Please enter a sentence, or 'q' to quit: ")
    if s == 'q':
        break
    else:
        pass
    for i in s:
        if i.islower():
            print(i.upper(),end="")
        elif i.isupper():
            print(i.lower(),end="")
        else:
            print(" ",end="")
    print()
    
