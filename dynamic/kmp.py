def pi(s: str):
    p=[0]*len(s)
    j,i=0,1
    while i<len(s):
        if s[i]==s[j]:
            p[i]=j+1
            i+=1
            j+=1
        elif j==0:
            p[i]=0
            i+=1
        else:
            j=p[j-1]
    return p


def search_kmp(string, substring):
    """
    Ищет построку в строке.
    Возвращает индекс первого вхождения подстроки
    или -1, если данная подстрока не найдена
    """

    found = -1
    i,j=0,0
    while i<len(string) and j < len(substring):
        if string[i] == substring[j]:
            if j == len(substring)-1:
                found = i+1-len(substring)
                break
            i+=1
            j+=1
        else:
            j=pi(substring)[j-1]
            i+=1
    return found



s = input('Строка: ')
sub = input('Подстрока: ')
print("Пи-функция для построки: \n",pi(sub))
f = search_kmp(s,sub)
if f==-1:
    print('Подстрока не входит в данную строку')
else:
    print("Подстрока найдена, индекс вхождения: ",f)

