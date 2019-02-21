L = input("Enter the elements of L (put a space after each element): ")
M = input("Enter the elements of M (put a space after each element): ")
N = []
L,M = L.split(" "),M.split(" ")

for i in L:
    L[L.index(i)] = eval(i)

for i in M:
    M[M.index(i)] = eval(i)

if len(L) < len(M):
    t = L
    L = M
    M = t
else:
    pass

count = 0
for i in M:
    N.append(M[count] + L[count])
    count += 1
print(N)
