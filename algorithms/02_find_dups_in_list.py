# поиск и вывод дубликатов в листе
# возвращает список дубликатов
def find_dupes(data):
    dups, seen = set(), set()
    for element in data:
        if element in seen:
            dups.add(element)
        seen.add(element)
    return list(dups)
