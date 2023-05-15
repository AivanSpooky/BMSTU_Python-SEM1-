# Смирнов Иван ИУ7-12Б ЛабРабота №6 Списки Часть 1
# 5. Поменять местами элементы (Первый нулевой и минимальный отрицательный)

# Ввод данных списка
while True:
    n = int(input("Введите размер списка: "))
    if n <= 0:
        print("Введите положительную длинну списка!")
    else:
        break
a = [0] * n
for i in range(n):
    a[i] = int(input(f"Введите целый {i+1}-ый элемент: "))

# Ищем минимальный отрицательный элемент
if min(a) >= 0:
    print("В списке нет отрицательных элементов!")
    exit()
else:
    min_below_zero = a.index(min(a))

# Ищем первый нулевой элемент
first_zero = -1
for i in range(n):
    if a[i] == 0:
        first_zero = i
        break
if first_zero == -1:
    print("В списке нет нулевых элементов!")
    exit()

# Меняем элементы местами
a[first_zero], a[min_below_zero] = a[min_below_zero], a[first_zero]

# Выводим полученный список
print("\nПолученный список:")
for i, el in enumerate(a):
    print(f"{i+1}-ый элемент: {el}")