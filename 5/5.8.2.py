a = 1
count = 0

while a <= 40:
    if count % 2 == 0:
        print(a,end=" ")
    else:
        print("-",a,sep="",end=" ")
    a += 3
    count += 1
 
