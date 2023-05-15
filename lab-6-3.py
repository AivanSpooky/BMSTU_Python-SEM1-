# Смирнов Иван ИУ7-12Б ЛабРабота №6 Списки Часть 1
# 3. Найти значение K-го экстремума в списке.

# Ввод данных списка
while True:
    n = int(input("Введите размер списка: "))
    if n <= 0:
        print("Введите положительную длинну списка!")
    else:
        break
a = [0] * n
for i in range(n):
    a[i] = float(input(f"Введите {i+1}-ый элемент: "))

# Вводим индекс экстремума
while True:
    k = int(input(f"Укажите индекс экстремума K: "))
    if k <= 0:
        print("Введите положительный K!")
    elif k >= n+1:
        print("Вы ввели несуществующий K для данного списка!")
    else:
        break

# Находим значение K-ого экстремума
extremums_found = 0
for i in range(1,n):
    if (a[i-1] < a[i] and a[i+1] < a[i] ) or(a[i-1] > a[i] and a[i+1] > a[i]):
        extremums_found += 1
        if extremums_found == k:
            print(f"\nЗначение {k}-ого экстремума = {a[i]:8g}")
            break
else:
    print(f"\nВ списке нет {k}-ого экстремума")