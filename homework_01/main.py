"""
Домашнее задание №1
Функции и структуры данных
"""

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def power_numbers(*args):
    return [i**2 for i in args]


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def filter_numbers(nums, type):
    if type == ODD:  # Нечетные числа
        return [num for num in nums if num % 2 == 1]
    elif type == EVEN:  # Четные числа
        return [num for num in nums if num % 2 == 0]
    elif type == PRIME:  # Простые числа
        return list(filter(is_prime, nums))
    else:  # Другое значение
        return []
