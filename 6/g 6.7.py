dic = {1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX',10:'X',20:'XX',30:'XXX',40:'XL',50:'L',60:'LX',70:'LXX',80:'LXXX',90:'XC',100:'C',200:'CC',300:'CCC',400:'CD',500:'D',600:'DC',700:'DCC',800:'DCCC',900:'CM',1000:'M',2000:'MM',3000:'MMM',4000:'MMMM',5000:'MMMMM',6000:'MMMMMM',7000:'MMMMMMM',8000:'MMMMMMMM',9000:'MMMMMMMMM'}
num = int(input("Enter a number below 9999: "))
if num < 10000:
    t = num
    rom = ''
    count = 1

    while t:
        r = t%10**count
        rom = dic[r] + rom
        t = (t//10**count) * 10**count
        count += 1
    print(rom)
else:
    print("Invalid number")
