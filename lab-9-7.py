x = int(input("Введите количество строк массива: "))
y = int(input("Введите количество столбцов массива: "))
z = int(input("Введите глубину массива: "))

while x < 1 or y < 1 or z < 1:
    if x < 1:
        x = int(input("Введите количество строк массива: "))
    elif y < 1:
        y = int(input("Введите количество столбцов массива: "))
    else:
        z = int(input("Введите глубину массива: "))

print()
A = []
for i in range(z):
    A.append([])
    for j in range(y):
        A[i].append([])
        for k in range(x):
            A[i][j].append(input(f"Введите значение в {j+1}-ю строку {k+1}-й элемент на {i+1}-й глубине: "))
        print()
    print()

#Выводим матрицу по XZ
cut = int(input(f"\n\nВведите срез массива по второму индексу (1-{y}): ")) - 1  #<--- По какому индексу делать срез
while cut >= y or cut < 0:
    cut = int(input(f"\n\nВведите срез массива по второму индексу (1-{y}): ")) - 1

for i in range(x):
    for j in range(z):
        print(f"{A[i][cut][j]:12}",end='')
    print()
