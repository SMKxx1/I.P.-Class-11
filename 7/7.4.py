count = int(input("Please enter the number of words: "))
a = []
for i in range(count):
    word = input(">>> ")
    a.append(word)
b = []
for i in a:
    b.append(i[1:])

print(b)

    
