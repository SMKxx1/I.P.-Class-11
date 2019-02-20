s = input("Enter a sentence: ")
count = 0

for i in s:
    if i.isalnum() == False:
        count += 1
    else:
        pass

per = (count/len(s))*100
per = round(per,2)

print()
print(s)
print()
print("The sentence has",len(s.split(' ')),"words")
print()
print("The length of the sentence is",len(s))
print()
print(per,"% characters are alphanumeric")
