#Козырнов Александр | ИУ7-12Б |
#Замена в символьной матрице всех гласных букв на точку '.'

D = []
n = int(input("Введите количество строк матрицы D: "))
m = int(input("Введите количество столбцов матрицы D: "))
while n <= 1 or m <= 1:
    if n <= 1:
        n = int(input("\nВведите количество строк матрицы D: "))
    else:
        m = int(input("\nВведите количество столбцов матрицы D: "))

print()
for i in range(n):
    D.append([])
    for j in range(m):
        D[i].append(input(f"Введите {i+1}-й элемент {j+1}-й строки: "))
    print()

lenght = 0  #<---Переменная для красивого вывода матрицы
for i in range(n):
    for j in range(m):
        if len(D[i][j]) > lenght:
            lenght = len(D[i][j])

print("\nВведенная матрица")
for i in range(n):
    for j in range(m):
        print(f"{D[i][j]:{lenght+5}}",end='')
    print()

#Замена гласных английских букв на точки
for i in range(n):
    for j in range(m):
        s = ''
        for k in D[i][j]:
            if k.lower() in "aeyuio":
                s += "."
            else:
                s += k
        D[i][j] = s

print("\nПолученная матрица")
for i in range(n):
    for j in range(m):
        print(f"{D[i][j]:{lenght+5}}",end='')
    print()
