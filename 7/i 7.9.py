#7.9 (a)
print("<<<: PART 'A' :>>>")
string = input("Enter the line: ")
s = string
s = s.split(" ")
long = ''

for i in s:
    if len(i) > len(long):
        long = i
    else:
        pass
print()
print("\"",string,"\"",sep="")
print("The longest string in the line is",long)
print()
input()


#7.9 (b)
print("<<<: PART 'B' :>>>")
print()
print(string)
print()
count = 1
List = string.split(" ")
for i in List:
    List[List.index(i)] = str(count) + ": " + i
    count += 1
print(List)
num = input("Choose the word: ")

for i in List:
    if num + ':' in i:
        print(i)
    else:
        pass
