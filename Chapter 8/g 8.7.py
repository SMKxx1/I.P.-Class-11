d1 = {'a':10,'b':10,'c':20,'d':40,'e':20}
count = 0

for i in d1:
    for e in d1:
        if i != e:
            if d1[i] == d1[e]:
                count += 1
            else:
                pass
        else:
            pass 
print(count)