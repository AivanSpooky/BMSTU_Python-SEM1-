"""
Смирнов Иван ИУ7-12Б Лабработа №8 "Матрицы. Часть 1"
4. Переставить местами столбцы с максимальной и минимальной суммой
элементов.
"""

# Ввод матрицы
while True:  # Кол-во строк матрицы
    m = int(input("Введите количество строк матрицы: "))
    if m <= 0:
        print("Введите положительное количество строк!")
    else:
        break
while True:  # Кол-во столбцов матрицы
    n = int(input("Введите количество столбцов матрицы: "))
    if n <= 0:
        print("Введите положительное количество столбцов!")
    else:
        break
matrix = [[0]*n for i in range(m)]
# Вводим элементы матрицы
for i in range(m):
    for j in range(n):
        matrix[i][j] = int(input(f"Введите {j+1}-ый элемент {i+1}-ой строки: "))

# Найдем столбцы с максимальной и минимальной суммой элементов
max_sum = None  # Макс. сумма элементов столбца
ind_max_sum = 0  # Индекс столбца с макс. суммой
min_sum = None  # Мин. сумма элементов столбца
ind_min_sum = 0  # Индекс столбца с мин. суммой
for i in range(m):
    summ = 0
    for line in matrix:
        summ += line[i]
    if max_sum is None or summ > max_sum:
        max_sum = summ
        ind_max_sum = i
    if min_sum is None or summ < min_sum:
        min_sum = summ
        ind_min_sum = i
# Поменяем данные столбцы местами
for i in range(n):
    matrix[i][ind_max_sum], matrix[i][ind_min_sum] = matrix[i][ind_min_sum], matrix[i][ind_max_sum]

# Определяем максимальную длину элемента матрицы для её форматированного вывода
max_len = len(str(matrix[0][0]))  # Макс. длина элемента матрицы
for line in matrix:
    max_len = max(max_len, len(str(max(line))), len(str(min(line))))
# Выводим матрицу
print("\nПолученная матрица:")
for line in matrix:
    print("", end="|")
    for elem in line:
        print(str(elem).ljust(max_len + max_len//2+1," "), end="|")
    print("")