"""
Смирнов Иван ИУ7-12Б Лабработа №8 "Матрицы. Часть 1"
2. Переставить местами строки с наибольшим и наименьшим количеством
отрицательных элементов.
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

# Найдем строки, содержащую наибольшее и наименьшее количество отрицательных
max_neg = None  # Максимальное количество отрицательных
ind_max_neg = 0  # Индекс строки, содержащей максимальное количество отрицательных
min_neg = None  # Максимальное количество отрицательных
ind_min_neg = 0  # Индекс строки, содержащей максимальное количество отрицательных
for i in range(len(matrix)):
    neg_count = 0  # Количество отрицательных в строке
    for elem in matrix[i]:
        if elem < 0:  # Нашли отрицательное - добавляем в счетчик
            neg_count += 1
    if max_neg is None or neg_count > max_neg:  # Нашли новое наиб. кол-во отрицательных
        max_neg = neg_count
        ind_max_neg = i
    if min_neg is None or neg_count < min_neg:  # Нашли новое наим. кол-во отрицательных
        min_neg = neg_count
        ind_min_neg = i
# Поменяем данные строки местами
matrix[ind_max_neg], matrix[ind_min_neg] = matrix[ind_min_neg], matrix[ind_max_neg]

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