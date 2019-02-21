#7.5 (a)

def a():
    List = []
    for i in range(50):
        List.append(i)
    print("7.5 (a):",List)
    print()


#7.5 (b)

def b():
    List = []
    for i in range(1,51):
        List.append(i**2)
    print("7.5 (b)",List)
    print()


#7.5 (c)

def c():
    List = []
    char = 97
    for i in range(1,27):
       List.append(chr(char)*i)
       char += 1
    print(List)

a(),b(),c()
