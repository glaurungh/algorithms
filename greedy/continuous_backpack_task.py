# https://stepik.org/lesson/13238/step/10?unit=3424
#
# Первая строка содержит количество предметов 1 ≤ n ≤ 10^3
# и вместимость рюкзака 0 ≤ W ≤ 2⋅10^6
# Каждая из следующих n строк задаёт стоимость 0 <= c[i] <= 2*10^6
# и объём 0 <= w[i] <= 2*10^6 предмета (n, W, c[i], w[i] — целые числа). 
# Выведите максимальную стоимость частей предметов 
# (от каждого предмета можно отделить любую часть, стоимость и объём при этом пропорционально уменьшатся), 
# помещающихся в данный рюкзак, с точностью не менее трёх знаков после запятой.
#

n, W = list(map(int, input().split()))
c, w = [], []
cost_factor = []
cost = 0
weight = 0
for i in range(n):
    cc, ww = map(float, input().split())
    c.append(cc)
    w.append(ww)
    cost_factor.append(c[i] / w[i])

while weight < W and len(cost_factor)>0:
    max_index = cost_factor.index(max(cost_factor))
    if w[max_index] < (W - weight):
        weight += w[max_index]
        cost += c[max_index]
    else:
        cost += (W - weight) * cost_factor[max_index]
        weight += (W - weight)
    w.pop(max_index)
    c.pop(max_index)
    cost_factor.pop(max_index)

print(f"{cost:.3f}")