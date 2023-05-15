#Козырнов Александр | ИУ7-12Б |
#Программа для нахождения максимальных элементов в строках, которые указаны в списке.
#Нахождение среднего арифметического всех максимальных элементов, найденных раннее

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
        D[i].append(float(input(f"Введите {i+1}-й элемент {j+1}-й строки: ")))
    print()

I = []
j = 1
print("Вводите строки матрицы, в которых нужно найти максимум: ")
while True:
    el = input(f"Введите {j}-й элемент массива I: ")
    if el:
        I.append(int(el))
        j += 1
    else:
        break

R = []
average = 0
count_average = 0
for p in range(len(I)):
    if 0 <= I[p]-1 < n:
        max_el = None
        for j in range(m):
            if max_el is None or D[I[p]-1][j] > max_el:
                max_el = D[I[p]-1][j]
        count_average += 1
        average += max_el
        R.append(max_el)
average = average/count_average

print("\nВведенная матрица D: ")
for p in range(n):
    for j in range(m):
        print(f"{D[p][j]:^12.6g}",end="")
    print()

print()
for (p,el) in enumerate(I):
    print(f"{p+1:2}-й элемент списка I: {el:<7.5g}")
print()
    
for (p,el) in enumerate(R):
    print(f"{p+1:2}-й элемент списка R: {el:<7.5g}")
print(f"\nСреднее арифмитическое всех максимальных элементов равно {average:<7.5g}")
