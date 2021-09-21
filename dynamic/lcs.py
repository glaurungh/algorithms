a=input("Строка 1:")
b=input("Строка 2:")

# Сделаем сначала подсчет длины подстрок
f=[[0]*len(b) for i in range(len(a))]

for j in range(len(b)):
    for i in range(len(a)):
        # print(i,j)
        if i==0 or j==0:
            f[i][j] = 1 if a[i]==b[j] else 0
        else:
            f[i][j] = f[i-1][j-1]+1 if a[i]==b[j] else 0

for i in range(len(a)):
    print(*f[i])

maxF=0
maxI=maxJ=0
for j in range(len(b)):
    for i in range(len(a)):
        if f[i][j] > maxF:
            maxF = f[i][j]
            maxI = i
            maxJ = j
substr = ""

while maxI > 0 and maxJ > 0 and f[maxI][maxJ] !=0 :
    substr+=str(a[maxI])
    maxI-=1
    maxJ-=1

substr=substr[::-1]

print("Максимальная длина подстроки: "+str(maxF))
print("Подстрока: "+substr)
