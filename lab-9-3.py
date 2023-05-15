#Козырнов Александр | ИУ7-12Б |
#Программа для нахождения количества элементов строки матрицы, больших чем сумма соответственной строки другой матрицы.
#Умножение матрицы на число

n = int(input("Введите количество строк D: "))
m = int(input("Введите количество строк D: "))

print()
D = []
for i in range(n):
    D.append([])
    for j in range(m):
        D[i].append(int(input(f"Введите {j+1}-й элемент {i+1}-й строки матрицы D: ")))
    print()


n1 = int(input("Введите количество строк Z: "))
m1 = int(input("Введите количество строк Z: "))
print()
Z = []
for i in range(n1):
    Z.append([])
    for j in range(m1):
        Z[i].append(int(input(f"Введите {j+1}-й элемент {i+1}-й строки матрицы Z: ")))
    print()

print("\nМатрица Z")
for i in range(n1):
    for j in range(m1):
        print(f"{Z[i][j]:12.6g}",end="")
    print()

#Считаем количество элементов в матрице D в строке, которые больше суммы всех элементов соответствующей строки Z
G = []
for i in range(n1):
    k = 0
    s = 0
    for j in range(m1):
        s += Z[i][j]
    if i < n:
        for o in range(m):
            if D[i][o] > s:
                k+=1
    G.append(k)
        
print("\nМатрица D до умножения: ")
for i in range(n):
    for j in range(m):
        print(f"{D[i][j]:12.6g}",end="")
    print()

#Ищем максимальный элемент G    
max_G = G[0]
for i in G:
    if i > max_G:
        max_G = i

#Умножаем матрицу на максимальный элемент G
for i in range(n):
    for j in range(m):
        D[i][j] = D[i][j] * max_G

print("\nМатрица D после умножения:")
for i in range(n):
    for j in range(m):
        print(f"{D[i][j]:12.6g}",end="")
    print()

print()
for (i,el) in enumerate(G):
    print(f"{i+1}-й элемент списка G равен {el}")
