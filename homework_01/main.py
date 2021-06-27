"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    return [i**i for i in args]


"""
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
"""


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(*nums, filt):
    if filt == 'odd':  # Нечетные числа
        return [num for num in nums if num % 2 == 1]
    elif filt == 'even':  # Четные числа
        return [num for num in nums if num % 2 == 0]
    elif filt == 'prime':  # Простые числа
        nums2 = []
        for num in nums:
            for i in range(2, num):
                if num % i == 0:
                    break
                else:
                    nums2.append(num)
                    break
        return nums2
    else:  # Другое значение
        return []


"""
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
"""
