# Stepic task:
# https://stepik.org/lesson/13246/step/4?unit=3431
#
# В первой строке даны целое число 1 ≤ n ≤ 10^5 и массив A[1…n] из n различных натуральных чисел, не превышающих 10^9, 
# в порядке возрастания, во второй — целое число 1 ≤ k ≤ 1^5 и k натуральных чисел b_1, ..., b_k, не превышающих 10^9.
# Для каждого i от 1 до k необходимо вывести индекс 1 ≤ j ≤ n, для которого A[j]=b_i A[j]=b_i
# или -1, если такого j нет.


n, *arr = list(map(int,input().split()))
k, *numbers = list(map(int,input().split()))

results = []

for item in numbers:
    l = 0
    r = n - 1
    found = False
    while l <= r:
        m = (l + r) // 2
        if arr[m] == item:
            results.append(m+1)
            found = True
            break
        elif arr[m] < item:
            l = m + 1
        else:
            r = m - 1
    if not found:
        results.append(-1)
print(*results)