# Stepic task:
# https://stepik.org/lesson/13240/step/8?unit=3426
#
# Первая строка входа содержит число операций 1 ≤ n ≤ 10^5
# Каждая из последующих nn строк задают операцию одного из следующих двух типов:
# Insert x, где 0 ≤ x ≤ 10^9 — целое число;
# ExtractMax.
# Первая операция добавляет число x в очередь с приоритетами, 
# вторая — извлекает максимальное число и выводит его.

_container = []
N = 0

def get_parent_index(i):
    return (i - 1) // 2

def has_parent(i):
    global N
    return get_parent_index(i) >= 0 and get_parent_index(i) < N

def get_left_child_index(i):
    return i * 2 + 1

def has_left_child(i):
    global N
    return get_left_child_index(i) < N

def get_right_child_index(i):
    return i * 2 + 2

def has_right_child(i):
    global N
    return get_right_child_index(i) < N

def get_max_child_index(i):
    global _container
    if not has_right_child(i):
        return get_left_child_index(i)
    else:
        if _container[get_left_child_index(i)] >= _container[get_right_child_index(i)]:
            return get_left_child_index(i)
        else:
            return get_right_child_index(i)

def heap_extract_max():
    global N
    global _container
    max_item = _container[0]
    if N > 1:
        _container[0] = _container.pop()
        N -= 1
        i = 0
        mci = get_max_child_index(i)
        while has_left_child(i) and _container[i] < _container[mci]:
            _container[i], _container[mci] = _container[mci], _container[i]
            i = mci
            mci = get_max_child_index(i)
    else:
        _container = []
        N = 0
    #print(_container)
    return max_item

def heap_insert(n):
    global N
    global _container
    _container.append(n)
    N += 1
    i = N - 1
    while has_parent(i) and _container[i] > _container[get_parent_index(i)]:
        _container[i], _container[get_parent_index(i)] = _container[get_parent_index(i)], _container[i]
        i = get_parent_index(i)
    #print(_container)


import sys


n = int(sys.stdin.readline())
for i in range(n):
    s = sys.stdin.readline()
    if s.startswith("Insert"):
        _, number = list(s.split())
        heap_insert(int(number))
    elif s.startswith("ExtractMax"):
        print(heap_extract_max())
