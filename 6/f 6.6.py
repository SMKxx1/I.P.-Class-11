s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

if len(s1) < len(s2):
    t = s1
    s1 = s2
    s2 = t
else:
    pass
print(s2)

length = len(s1)

length = length/2

count = length
count1 = 0
if length % 2 == 0:
    count = length
    count1 = 0
    for i in range(0,length):
        tac = str(length) + '+' + str(count)
        tac = tac + '-' + str(count1)
        print('\t'*count1,s1[count1],'\t'*eval(tac),s1[count1 - (count1*2) - 1])
        count -= 1
        count1 += 1
else:
   length += 0.5
   length = round(length)
   List = []
   for i in s1:
       List.append(i)
   s1 = List
   mid = s1.pop(length)
   s1 = ''.join(s1)
   length = length - 1
   for i in range(0,length):
        count = round(count)
        tac = str(length) + '+' + str(count)
        tac = tac + '-' + str(count1)
        print('\t'*count1,s1[count1],'\t'*eval(tac),s1[count1 - (count1*2) - 1])
        count -= 1
        count1 += 1
   print('\t'*count1,"",mid)
