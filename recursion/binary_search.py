import random

def is_sorted(A:list,ascending=True):
    """ Determinies is list sorted or not """
    flag = 2*int(ascending)-1
    for i in range(len(A)-1):
        if flag*A[i]>flag*A[i+1]:
            return False
    return True


def left_bound(A:list,item):
    """ Find left boundary in the sorted list """
    assert is_sorted(A), "The list should be sorted before"
    left = -1
    right = len(A)
    while right-left>1:
        middle=(left+right)//2
        if a[middle]<item : # right: <=
            left=middle
        else:
            right=middle
    return left #right: return right


a = [random.randint(-10,10) for i in range(20)]
print(a)
print("Sorted" if is_sorted(a) else "Not sorted")
a.sort()
print(a)
print("Sorted" if is_sorted(a) else "Not sorted")
#a.reverse()
#print(a)
#print("Reverse sorted" if is_sorted(a,ascending=False) else "Not sorted")
i = random.randint(-10,10)
lb = left_bound(a,i)
print("Left boundary for item {} is [{}]".format(i,lb))
