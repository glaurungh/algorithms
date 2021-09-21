
cache=dict()

def f(n):
    if n in cache.keys():
        return cache[n]
    if n<=1:
        cache[n]=n
        return n
    cache[n] = f(n-2)+f(n-1)
    return cache[n]

print(f(5))
print(f(10))
print(f(20))
print(f(35))
print(f(100))
print(f(150))
print(f(200))
print(f(300))
