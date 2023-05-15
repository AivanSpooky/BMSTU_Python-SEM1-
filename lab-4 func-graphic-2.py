# Смирнов Иван ИУ7-12Б Лабработа №4 "График"
# Вариант 45
# Написать программу, которая для заданных по варианту функций выведет таблицу
# значений этих функций на некотором отрезке и построит график одной из них.
# В конце программа выводит значение выражения: sqrt(|min_f1*min_f2|)


# Модуль math
import math as m

eps = 0.0000001   # погрешность для сравнения вещественных чисел

# Ввод начального, конечного значения аргумента и шага разбиения
while True:
    p_0, p_n, h = (float(i) for i in input("Введите начальное, конечное \
значение аргумента и шаг разбиения через пробел: ").split())
    if h <= 0:
        print("Введите положительный шаг")
    elif abs(p_0-p_n) - h > eps:
        break
    else:
        print("Введите диапазон аргументов и шаг так, чтобы посчиталось больше \
1 значения")

# Считаем значения функций на заданном отрезке с шагом h используя цикл while
# И выводим результаты в виде таблицы
# p_0, p_n = min(p_0, p_n), max(p_0, p_n)

i = p_0   # вводим счетчик
min_f1 = 2.3*p_0**4 + 1.5*p_0**3 + 6.45*p_0**2 - 24.647*p_0 + 1  # min f1
max_f1 = 2.3*p_0**4 + 1.5*p_0**3 + 6.45*p_0**2 - 24.647*p_0 + 1  # max f1
max_f2, min_f2 = 21.987 - 10.112*2**p_0, 21.987 - 10.112*2**p_0  # max-min f2

str_len = 80  # Длинна строки
print(f"-"*(str_len-1))
print("|"+" "*12+"p"+" "*12+"|"+" "*11+"f1"+" "*12+"|"+" "*11+"f2"+" "*12+"|")
print(f"-"*(str_len-1))
#print(f"|{0.1415152:7.5g} | {0:7.5g} | {0.1415152:7.5g}|")
# Считаем значения f1 и f2 для каждого x и выводим в табл.
if p_0 > p_n:
    while p_n-i <= eps:
        if abs(i) < eps:
            i = 0
        f1 = 2.3*i**4 + 1.5*i**3 + 6.45*i**2 - 24.647*i + 12  #значение f1
        f2 = 21.987 - 10.112*2**i  #значение f2
        # Ищем минимальное значение f1 (для доп задания)
        if f1 < min_f1:
            min_f1 = f1
        if f1 > max_f1:
            max_f1 = f1
        # Ищем максимальное и минимальное значение f2
        if f2 > max_f2:
            max_f2 = f2
        elif f2 < min_f2:
            min_f2 = f2
        print(f"|{i:<{m.ceil(25)}.5g}", end="")
        print(f"|{f1:<{m.ceil(25)}.5g}", end="")
        print(f"|{f2:<{m.ceil(25)}.5g}|")
        #print(f"|{i:6.5g} | {f1:6.5g} | {f2:6.5g}|")
        i -= h
    p_0, p_n = i+h, p_0
else:
    while i-p_n <= eps:
        if abs(i) < eps:
            i = 0
        f1 = 2.3*i**4 + 1.5*i**3 + 6.45*i**2 - 24.647*i + 12  #значение f1
        f2 = 21.987 - 10.112*2**i  #значение f2
        # Ищем минимальное значение f1 (для доп задания)
        if f1 < min_f1:
            min_f1 = f1
        if f1 > max_f1:
            max_f1 = f1
        # Ищем максимальное и минимальное значение f2
        if f2 > max_f2:
            max_f2 = f2
        elif f2 < min_f2:
            min_f2 = f2
        print(f"|{i:<{m.ceil(25)}.5g}", end="")
        print(f"|{f1:<{m.ceil(25)}.5g}", end="")
        print(f"|{f2:<{m.ceil(25)}.5g}|")
        #print(f"|{i:6.5g} | {f1:6.5g} | {f2:6.5g}|")
        i += h
print(f"-"*(str_len-1))
# Вводим количество засечек на оси ординат
while True:
    cell_count = int(input("Введите количество засечек на оси y (от 4 до 8): "))
    if 4 <= cell_count <= 8:
        break

# Построение графика f2
cell_size = m.ceil(80/(cell_count+1))  # Размер клетки
print(" "*cell_size, end="")
i = 0  # Счетчик

r = (max_f2 - min_f2)/(cell_count-1)  # Разность арифм прогрессии
while i < cell_count:
    # Выводим значения функции
    if i+1 == cell_count:
        print(f"{(max_f2):<{cell_size}.2g} ", end="")
    else:
        print(f"{(min_f2+r*i):<{cell_size}.3g} ", end="")
    i += 1
print("")

i = p_0 # Счетчик
dot_eps = (max_f2 - min_f2)/(cell_size*(cell_count-1))  # Погрешность точки
#print(dot_eps)
while i-p_n <= eps:  # Перебираем все аргументы
    f2 = 21.987 - 10.112*2**i  # Значение f2
    if abs(i) < eps:
        i = 0
    print(f"{i:<{cell_size-1}.5g}|", end="")  # Аргумент
    # Вывод точек для всех аргументов с погрешностью dot_eps
    filled_space_count = 0  # Количество заполненых клеток
    j = 0  # Счетчик
    dot_found = False  # Поставлена ли точка с данным аргументом
    x_found = False  # Поставлена ли ось абсцисс
    # Пока заполняются клетки в строке
    while filled_space_count <= str_len - cell_size: 
        # Примерная погрешность
        approx_eps = abs((21.987 - 10.112*2**i) - (min_f2+r/(cell_size+1)*j))
        # Точка близка к оси ох
        if (21.987 - 10.112*2**i)<0 and abs(min_f2+r/(cell_size+1)*(j+1)) <= \
dot_eps and not(x_found) and not(dot_found):
            print(f"*", end="") 
            dot_found = True 
            
        elif approx_eps <= dot_eps - approx_eps and not(dot_found): # Точка?
            print(f"*", end="") 
            dot_found = True  
        elif abs(min_f2+r/(cell_size+1)*j) <= dot_eps and not(x_found):  # ох?
            print(f"|", end="") 
            x_found = True   
        else:  # Ничего не нашли - ставим пробел
            print(" ", end="") 
        j += 1
        filled_space_count += 1
    print("")  # Конец строки
    
    i += h
print(f"Доп задание. Значение = {abs((min_f1*min_f2))**0.5:8.5g}")
