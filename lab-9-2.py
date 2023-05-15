#Козырнов Александр | ИУ7-12Б |
#Поворот квадратной матрицы на 90 градусов по часовой и против часовой

n = -1
while n < 2:
    n = int(input("Введите размерность матрицы: "))
print()

A = []
for i in range(n):
    A.append([])
    for j in range(n):
        A[i].append(int(input(f"Введите {j+1}-й элемент {i+1}-й строки: ")))
    print()

print("\nВведенная матрица: ")
for i in range(n):
    for j in range(n):
        print(f"{A[i][j]:12.6g}",end="")
    print()

#Поворачиваем матрицу по часовой
for i in range(n//2):
    for j in range(i, n-1-i):
        A[i][j], A[j][n-1-i], A[n-1-i][n-1-j], A[n-1-j][i] = \
        A[n-1-j][i], A[i][j], A[j][n-1-i], A[n-1-i][n-1-j]

print("\nПромежуточная матрица: ")
for i in range(n):
    for j in range(n):
        print(f"{A[i][j]:12.6g}",end="")
    print()

#Поворачиваем матрицу против часовой
for i in range(n//2):
    for j in range(i, n-1-i):
        A[n-1-j][i], A[i][j], A[j][n-1-i], A[n-1-i][n-1-j] = \
        A[i][j], A[j][n-1-i], A[n-1-i][n-1-j], A[n-1-j][i]

print("\nПолученная матрица: ")
for i in range(n):
    for j in range(n):
        print(f"{A[i][j]:12.6g}",end="")
    print()
