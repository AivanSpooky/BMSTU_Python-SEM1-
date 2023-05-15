"""
Смирнов Иван ИУ7-12Б Лабработа №8 "Матрицы. Часть 1"
1. Найти строку, имеющую наибольшее среднее арифметическое.
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

# Найдем строку, содержащую наибольшее среднее арифметическое
max_average = -1  # Максимальное среднее
ind_max_average = 0  # Индекс строки, содержащей максимальное среднее
for i in range(len(matrix)):
    summ = 0  # Суммируем элементы строки
    for elem in matrix[i]:
        summ += elem
    if summ/n > max_average:  # Нашли новое наибольшее среднее?
        max_average = summ/n
        ind_max_average = i

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
# Вывод строки, содержащей наибольшее среднее арифметическое
print(f"\n{ind_max_average+1}-ая строка содержит наибольшее среднее арифметическое элементов, равное {max_average:8g}")