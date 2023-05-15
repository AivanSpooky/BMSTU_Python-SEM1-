#Козырнов Александр | ИУ7-12Б |
#Перемножение двух матриц (элементы в i-й строке матрицы A умножаются на соответствующие элементы в i-й строке матрицы B)


n = int(input("Введите количество строк матрицы A и В: "))
m = int(input("Введите количество столбцов матрицы A и В: "))
while n <= 1 or m <= 1:
    if n <= 1:
        n = int(input("\nВведите количество строк матрицы A и В: "))
    else:
        m = int(input("\nВведите количество столбцов матрицы A и В: "))
A = []
print()
for i in range(n):
    A.append([])
    for j in range(m):
        A[i].append(float(input(f"Введите {i+1}-й элемент {j+1}-й строки: ")))
    print()

B = []
print()
for i in range(n):
    B.append([])
    for j in range(m):
        B[i].append(float(input(f"Введите {i+1}-й элемент {j+1}-й строки: ")))
    print()

#Создаем пустую матрицу
C = []
print()
for i in range(n):
    C.append([])
    for j in range(m):
        C[i].append(0)

#Перемножаем (по правилу, описанному в задании)
for i in range(n):
    for j in range(m):       
        C[i][j] = A[i][j] * B[i][j]


print("Матрица C")
for i in range(n):
    for j in range(m):
        print(f"{C[i][j]:12.7g}",end="")
    print()

#Сложение стобцов матрицы C и добавление результатов в список V
V = []
for j in range(m):
    s = 0
    for i in range(n):
        s += C[i][j]
    V.append(s)

print()
for (i,el) in enumerate(V):
    print(f"{i+1}-й элемент в списке V равен {el:<7.6g}")
