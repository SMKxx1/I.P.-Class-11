months = {'jan':31,'feb':28,'mar':31,'apr':30,'may':31,'jun':30,'jul':31,'aug':31,'sep':30,'oct':31,'nov':30,'dec':31}

#Part A
print("Part A")
name = input("Enter the month name (first three letters): ")
if name in months:
    print(months[name])
else:
    print("No month found.")
print()

#Part B
print("Part B")
lis = []

for i in months:
    lis.append(i)

lis.sort()

for i in lis:
    print(i)
print()

#Part C
print("Part C")
for i in months:
    if months[i] == 31:
        print(i)
    else:
        pass
print()

#Part D
print("Part D")
lis = []
for i in months:
    lis.append([months[i],i])
for i in lis:
    print(i[1],":",i[0])
print()