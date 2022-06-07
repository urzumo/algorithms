# ищет все пермутации 
def get_permutations(l):
    '''
    Фукнция get_permutations возвращает итератор с последовательными перестановками 
    из элементов входной последовательности. Является альтернативой встроенной функции
    itertools.permutations(iterable, r=None)
    '''
    if len(l) <= 1: 
        return set(l)
    smaller = get_permutations(l[1:])
    perms = set()
    for x in smaller:
        for pos in range(0, len(x)+1):
            perm = x[:pos] + l[0] + x[pos:]
            perms.add(perm)
    return perms
