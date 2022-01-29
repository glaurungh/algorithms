# Задача https://stepik.org/lesson/13238/step/9?unit=3424
# По данным n отрезкам необходимо найти множество точек минимального размера, для которого каждый из отрезков содержит хотя бы одну из точек.
# В первой строке дано число 1 \le n \le 1001≤n≤100 отрезков. 
# Каждая из последующих nn строк содержит по два числа 0 <= l <= r <= 10^90≤l≤r≤109, задающих начало и конец отрезка. Выведите оптимальное число m точек и сами m точек. Если таких множеств точек несколько, выведите любое из них.

N = int(input())
l = []
for i in range(N):
    r = input().split()
    l.append(list(map(int, r)))

l.sort(key=lambda x: x[1])

points = []

while len(l) != 0:
    point = l[0][1]
    points.append(point)
    while len(l) and l[0][0] <= point:
        l.remove([l[0][0], l[0][1]])
                                            
print(len(points))
print(*points)
