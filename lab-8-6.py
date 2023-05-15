"""
Смирнов Иван ИУ7-12Б Лабработа №8 "Матрицы. Часть 1"
6. Выполнить транспонирование квадратной матрицы.
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

# Выполняем транспонирование квадратной матрицы
for i in range(n):
    for j in range(i, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

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