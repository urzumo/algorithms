# поиск ряда чисел Фибоначчи (числовая последовательность, 
# первые два числа которой являются 0 и 1, 
# а каждое последующее за ними число является суммой двух предыдущих)
def fibonacci_nums(a, b, n):
    '''
    Функция fibonacci_nums формирует ряд чисел Фибоначчи, 
    начинающийся с чисел a и b, размером n
    '''
    for i in range(n):
        print(b)
        a, b = b, a + b
