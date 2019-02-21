words = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',0:'zero'}

a = int(input("Enter a number between 0 and 9: "))

if a < 0 or a > 9:
    print("Invalid")
else:
    print(words[a])
 
