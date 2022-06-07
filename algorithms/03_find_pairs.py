# поиск парных значений
def find_pairs(l, x):
    '''
    Функция find_pairs ищет пары чисел в списке l,
    сумма которых равна x
    '''
    pairs = []
    for i, v1 in enumerate(l):
        for inx, v2 in enumerate(l[i+1:]):
            if v1 + v2 == x:
                pairs.append((v1, v2))
    return pairs
