import random

def insert_sort(a:list):
    """ Returns new sorted list based on given list
        Using N2 method: Insert
    """
    for i in range(len(a)):
        for j in range(i):
            if a[j]>a[i] :
                a[i],a[j] = a[j],a[i]


def choise_sort(a:list):
    """ 
       Choise sort
    """
    for i in range(len(a)-1):
        min_index=i
        for j in range(i+1,len(a)):
            if a[j] < a[min_index]:
                min_index=j
        if min_index != i:
            a[i], a[min_index] = a[min_index], a[i]


def bubble_sort(a:list):
    for i in range(1,len(a)):
        for j in range(len(a)-i):
            if a[j] > a[j+1] :
                a[j],a[j+1] = a[j+1],a[j]


def count_sort(a:list):
    digit = 100
    f = [0]*digit
    for i in range(len(a)):
        f[a[i]]+=1
    a.clear()
    for i in range(digit):
        a+=[i]*f[i]


a=[random.randint(1,10) for x in range(20)]
print(a)
count_sort(a)
print(a)
