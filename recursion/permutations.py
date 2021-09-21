def generate_numbers(N:int, M:int, prefix = None):
    """ Генерирование  чисел длиной M 
        в N-ричной системе счисления
    """
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for i in range(N):
        generate_numbers(N,M-1,prefix + [i])



def generate_permutations(N:int, M:int=-1, prefix = None):
    """ Генерирование перестановок из N чисел в M позициях"""
    M = M if M != -1 else N # По умолчанию M=N
    prefix = prefix or []
    if M == 0:
        print(*prefix)
        return
    for number in range(1,N+1):
        if number in prefix:
            continue
        generate_permutations(N,M-1,prefix + [number])


#generate_permutations(4,3)
generate_permutations(5)

