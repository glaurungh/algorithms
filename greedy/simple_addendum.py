# https://stepik.org/lesson/13238/step/11?unit=3424
#
# По данному числу 1≤n≤10^9 найдите максимальное число k,
# для которого n можно представить как сумму k различных натуральных слагаемых. 
# Выведите в первой строке число k, во второй — k слагаемых.

n = int(input())

def get_items(n):
    items = []
    if n == 0 or n == 1 or n == 2:
        return [n,]
    else:
        i = 1
        cumsum = 1
        items.append(i)
        while n-cumsum > (i+1)*2:
            i+=1
            cumsum += i
            items.append(i)
        items.append(n-cumsum)
        return items

items = get_items(n)
print(len(items))
print(*items)