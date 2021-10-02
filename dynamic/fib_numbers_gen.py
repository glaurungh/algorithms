def fibgen(N):
    yield 0
    yield 1
    n,l = 1,0
    for i in range(2,N+1):
        yield n+l
        n,l = n+l,n

g = fibgen(100)
for i in g:
    print(i)
