# функция быстрой сортировки
def qsort(l):
    if l == []: return []
    return (qsort([x for x in l[1:] if x < l[0]]) + l[0:1] +
            qsort([x for x in l[1:] if x > l[0]]))
