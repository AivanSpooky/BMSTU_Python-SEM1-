"""
Смирнов Иван ИУ7-12Б Лабработа №11 "Исследование методов сортировки"
Программа сортирует массив для доказательства корректности работы алгоритма
Далее вводятся 3 массива различных размеров (случайный, отсортированный, 
отсортированный в обр. порядке) и составляется таблица замеров времени их 
сортировки.
"""

# Импортируем модуль time для замеров времени
# Импортируем модуль random для создания случайного списка
import time as t
import random as r

# Функция для создания размера списка (для части №2 с таблицей)
def create_n(num):
    while True:
        try:
            n = int(input(f"Введите размерность (списка) N{num}: "))
            if n <= 0:
                print("Введите положительную длину списка!")
            else:
                break
        except Exception:
            print("Произошла ошибка ввода данных. Вы точно ввели целое число?")
    return n

# Функция для введения списка
def create_list(n, mode=None):
    ls = [0]*n
    if mode == "sorted":
        for i in range(n):
            ls[i] = i+1
    elif mode == "reverse-sorted":
        for i in range(n-1, -1, -1):
            ls[i] = n-i
    elif mode == "random":
        for i in range(n):
            ls[i] = r.randint(-n, n)
    else:
        print(f"\nВведите элементы массива из {n} элемeнтов")
        for i in range(n):
            while True:
                try:
                    ls[i] = int(input(f"Введите {i+1}-й элемент массива: "))
                    break
                except Exception:
                    print("Произошла ошибка ввода данных. Вы точно ввели целое число?")
    return ls

# Функция для сортировки списка (методом простых вставок)
def insertionsort(ls, table_list=False):
    if table_list:
        k = 0
    for i in range(1, len(ls)):
        cur = ls[i]
        j = i - 1
        while j >= 0 and cur < ls[j]:
            ls[j+1] = ls[j]
            j -= 1
        ls[j+1] = cur
        if table_list and j+1 != i:
            k += 1
    if table_list:
        return k
    return ls


# Начало программы. Вводится первый список для сортировки
# Создается новый отсортированный список
# Выводятся исходный и отсортированный списки
n = create_n("")
ls1 = create_list(n)
print(f"\nИсходный список:")
for i in range(len(ls1)):
    print(f"{i+1}-й элемент: {ls1[i]}")
    
ls1 = insertionsort(ls1)
print(f"\nПолученный список:")
for i in range(len(ls1)):
    print(f"{i+1}-й элемент: {ls1[i]}")

# Вводятся размерности N1, N2, N3
print("\nВведите три размерности:\n")
n1 = create_n(1)
n2 = create_n(2)
n3 = create_n(3)

# Заполняется таблица
print()
print(f"-"*83)
print(f"|{' ':<15}|{f'{n1} элементов':21}|{f'{n2} элементов':21}|{f'{n3} элементов':21}|")
print(f"-"*83)
print(f"|{' ':<15}|{'время':10}|{'перестан.':10}|{'время':10}|{'перестан.':10}|{'время':10}|{'перестан.':10}|")
print(f"-"*83)

print(f"|{'Упорядоченный':<15}|", end='')
for i in (n1, n2, n3):
    ls = create_list(i, "sorted")
    start_time = t.time()
    inserts = insertionsort(ls, True)
    end_time = t.time()
    print(f"{end_time-start_time:<10.5g}|{inserts:<10}|", end='')
print(f"\n|{'список':<15}|{' ':10}|{' ':10}|{' ':10}|{' ':10}|{' ':10}|{' ':10}|")
print(f"-"*83)

print(f"|{'Случайный':<15}|", end='')
for i in (n1, n2, n3):
    ls = create_list(i, "random")
    start_time = t.time()
    inserts = insertionsort(ls, True)
    end_time = t.time()
    print(f"{end_time-start_time:<10.5g}|{inserts:<10}|", end='')
print(f"\n|{'список':<15}|{' ':10}|{' ':10}|{' ':10}|{' ':10}|{' ':10}|{' ':10}|")
print(f"-"*83)

print(f"|{'Упорядоченный':<15}|", end='')
for i in (n1, n2, n3):
    ls = create_list(i, "reverse-sorted")
    start_time = t.time()
    inserts = insertionsort(ls, True)
    end_time = t.time()
    print(f"{end_time-start_time:<10.5g}|{inserts:<10}|", end='')
print(f"\n|{'в обратном':<15}|{' ':10}|{' ':10}|{' ':10}|{' ':10}|{' ':10}|{' ':10}|", end='')
print(f"\n|{'порядке':<15}|{' ':10}|{' ':10}|{' ':10}|{' ':10}|{' ':10}|{' ':10}|")
print(f"-"*83)