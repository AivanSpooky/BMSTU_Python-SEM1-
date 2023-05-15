#Козырнов Александр | ИУ7-12Б |
#Программа для формирования матрицы из массивов нахождение среднего арифмитического и чисел, меньших его, в каждой строке матрицы

from math import sin,cos

D = []
i = 1
while True:
    el = input(f"Введите {i}-e значение массива D: ")
    if el:
        D.append(float(el))
        i += 1
    elif len(D) < 1:
        print("\nДобавьте еще элементов в список D")
    else:
        print()
        break

F = []
i = 1
while True:
    el = input(f"Введите {i}-e значение массива F: ")
    if el:
        F.append(float(el))
        i += 1
    elif len(F) < 1:
        print("\nДобавьте еще элементов в список F")
    else:
        print()
        break
n = len(D)
m = len(F)

#3аполняем матрицу А
A = []
for i in range(n):
    A.append([])
    for j in range(m):
        A[i].append(sin(D[i])*cos(F[j]) + cos(D[i])*sin(F[j]))

#Ищем среднее арифметическое положительных чисел в каждой строке матрицы А
AV = []
for i in range(n):
    average = 0
    k = 0
    for j in range(m):
        if A[i][j] > 0:
            average += A[i][j]
            k += 1
    if k > 0:
        AV.append(average/k)
    else:
        AV.append(0)

#Ищем количество элементов, меньших ср. арифм. в соответственных строках
L = []
for i in range(n):
    k = 0
    for j in range(m):
        if AV[i] > A[i][j]:
            k += 1
    L.append(k)

print("\nВведенная матрица и столбцы AV и L:\n ")
for i in range(n):
    for j in range(m):
        print(f"{A[i][j]:^12.6g}",end="")
    print(f"{'':5}|  {AV[i]:^12.6g} {L[i]:^12.6g}")
