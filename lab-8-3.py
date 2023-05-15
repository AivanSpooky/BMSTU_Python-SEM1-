"""
Смирнов Иван ИУ7-12Б Лабработа №8 "Матрицы. Часть 1"
3. Найти столбец, имеющий минимальную разницу между модулями суммы отрицательных
и положительных элементов
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

# Найдем столбец, имеющий минимальную разницу между модулями суммы отрицательных
# И положительных элементов 
min_dif = None
ind_min_dif = 0
for i in range(m):
    dif = 0
    for line in matrix:
        dif -= line[i]
    if min_dif is None or dif < min_dif:
        min_dif = dif
        ind_min_dif = i

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
# Выводим полученный столбец
print(f"{ind_min_dif+1}-ый столбец имеет минимальную разницу между модулями суммы \
отрицательных и положительных элементов, равную {min_dif}")