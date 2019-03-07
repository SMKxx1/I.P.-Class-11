dic = {}
lis = []
lis_avg = []

hi_rec = 0
lo_rec = 100000
hi_avg = 0
lo_avg = 100000

num = int(input("Enter the number of teams: "))
for i in range(num):
    team = input("Enter the team name: ")
    win = int(input("Enter the number of wins: "))
    loss = int(input("Enter the number of losses: "))
    dic[team] = [win,loss]
    print()

#Part a
for i in dic:
    Sum = (dic[i][0] + dic[i][1])
    avg = (dic[i][0]/Sum) * 100
    avg = round(avg)
    dic[i] = [dic[i][0],dic[i][1],avg]
    print("The average of",i,"is",avg)

#Part b
for i in dic:
    lis.append(dic[i][0])
print(lis)
print()

#Part c

for i in dic:
    if dic[i][0] < hi_rec:
        pass
    else:
        hi_rec = dic[i][0]
        hi_rec_name = i

    if dic[i][0] > lo_rec:
        pass
    else:
        lo_rec = dic[i][0]
        lo_rec_name = i

for i in dic:
    if dic[i][2] < hi_avg:
        pass
    else:
        hi_avg = dic[i][2]
        hi_avg_name = i

    if dic[i][2] > lo_avg:
        pass
    else:
        lo_avg = dic[i][2]
        lo_avg_name = i

print("The team with the highest wins is",hi_rec_name,":",hi_rec,"wins")
print()
print("The team with the lowest wins is",lo_rec_name,":",lo_rec,"wins")
print()
print("The team with the highest win average is",hi_avg_name,":",hi_avg,"%")
print()
print("The team with the lowest win average is",lo_avg_name,":",lo_avg,"%")


