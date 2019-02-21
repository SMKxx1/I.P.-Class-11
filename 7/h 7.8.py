series = int(input("Enter the range: "))

n1 = 1
n2 = 1
count = 0

if series <= 0:
   print("Please enter a positive integer")
elif series == 1:
   print("Fibonacci sequence upto",series,":")
   print(n1)
else:
    while count < series:
        print(n1,end=" , ")
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
