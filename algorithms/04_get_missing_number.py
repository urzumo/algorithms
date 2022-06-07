# поиск отсутствующих чисел в непрерывном числовом ряду
def get_missing_number(data):
    return set(range(data[len(data)-1])[1:]) - set(data)
