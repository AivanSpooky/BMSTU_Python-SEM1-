"""
Смирнов Иван ИУ7-12Б Лабработа №8 "Матрицы. Часть 1"
5. Найти максимальное значение в квадратной матрице над главной диагональю и
минимальное - под побочной диагональю
"""

# Ввод квадратной матрицы
while True:  # Кол-во строк матрицы
    n = int(input("Введите количество строк и столбцов квадратной матрицы: "))
    if n <= 0:
        print("Введите положительное количество строк и столбцов!")
    else:
        break
matrix = [[0]*n for i in range(n)]
# Вводим элементы матрицы
for i in range(n):
    for j in range(n):
        matrix[i][j] = int(input(f"Введите {j+1}-ый элемент {i+1}-ой строки: "))

# Найдем максимальное значение над главной диагональю
max_over_main = None  # Макс. элемент над главной диагональю
for i in range(n):
    for j in range(i+1, n):
        if max_over_main is None or matrix[i][j] > max_over_main:
            max_over_main = matrix[i][j]
# Найдем минимальное значение под побочной диагональю
min_under_side = None  # Мин. элемент под побочной диагональю
for i in range(n):
    for j in range(n-i, n):
        if min_under_side is None or matrix[i][j] < min_under_side:
            min_under_side = matrix[i][j]

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
# Выводим полученные значения
print(f"\n{max_over_main} - максимальное число над главной диагональю")
print(f"{min_under_side} - минимальное число под побочной диагональю")