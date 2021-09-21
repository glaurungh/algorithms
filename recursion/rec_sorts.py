import random

def hoar_sort(a:list):
    """ Функция сортировки методом Тони Хоара 
        возвращает отсортированный массив
    """
    N=len(a)
    # Если массив состоит только из одного элемента - вернуть его
    if N<=1: 
        return a
    # Взять граничный элемент, например, в середине
    b = a[N//2]
    # это можно сделать еще так: b = a[random.randint(0,N-1)]
    less, more = [], []
    nb = 0
    # Пройти циклом по массиву
    for i in range(N):
        if a[i] < b:
            less.append(a[i])
        elif a[i] > b:
            more.append(a[i])
        else:
            nb+=1
    a = hoar_sort(less) + [b]*nb + hoar_sort(more)
    return a


def merge(A:list, B:list):
    """ Функция осуществляет слияние двух упорядоченных списков 
        возвращает объединенный список
    """
    C=[]
    idxA = idxB = 0
    while idxA < len(A) and idxB < len(B):
        if A[idxA] <= B[idxB]:
            C.append(A[idxA])
            idxA+=1
        else:
            C.append(B[idxB])
            idxB+=1
    while idxA < len(A):
        C.append(A[idxA])
        idxA+=1
    while idxB < len(B):
        C.append(B[idxB])
        idxB+=1
    return C

def merge_sort(a:list):
    """ Функция сортировки слиянием"""
    N=len(a)
    if N <= 1:
        return a
    return merge(merge_sort(a[0:N//2]), merge_sort(a[N//2:N]))


a=[random.randint(-30,30) for x in range(20)]
print(a)
c=merge_sort(a)
print(c)
