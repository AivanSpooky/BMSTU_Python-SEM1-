# Смирнов Иван ИУ7-12Б Лабработа №4 "График"
# Вариант 45

# Модуль math
import math as m

# Ввод начального, конечного значения аргумента и шага разбиения
p_0, p_n, h = (float(i) for i in input("Введите начальное, конечное значение аргумента и шаг разбиения через пробел: ").split())

# Считаем значения функций на заданном отрезке с шагом h используя цикл while
# И выводим результаты в виде таблицы
i = p_0   # вводим счетчик
eps = 0.00001   # погрешность
max_f2, min_f2 = -999999, 999999  # max-min
print(f"--------------------------------\n", end="")
print(f"|   p     |   f1     |   f2    |\n", end="")
print(f"--------------------------------\n", end="")
#print(f"|{0.1415152:7.5g} | {0:7.5g} | {0.1415152:7.5g}|")
while i-p_n <= eps:
    f1 = 2.3*i**4 + 1.5*i**3 + 6.45*i**2 - 24.647*i + 12  #значение f1
    f2 = 21.987 - 10.112*2**i   #значение f2
    max_f2 = max(max_f2, f2)  # максимальное значение f2
    min_f2 = min(min_f2, f2)  # минимальное значение f2
    print(f"|{i:8.5g} | {f1:8.5g} | {f2:8.5g}|")
    i += h
print(f"--------------------------------\n")

# Вводим количество засечек на оси ординат
while True:
    cell_count = int(input("Введите количество засечек на оси ординат (от 4 до 8): "))
    if 4 <= cell_count <= 8:
        break

# Построение графика f2
cell_size = m.ceil(80/(cell_count+1))
print(cell_size)
print(" "*cell_size, end="")
i = 0  # счетчик
r = (max_f2 - min_f2)/(cell_count-1)  #разность арифм прогрессии
while i < cell_count:
    print(f"{(min_f2+r*i):<{cell_size}.5g} ", end="")
    i += 1
print("")

i = p_0  #счетчик
dot_eps = 0.3   # погрешность точки
while i-p_n <= eps:
    f2 = 21.987 - 10.112*2**i   #значение f2
    print(f"{i:<{cell_size-1}.5g}|", end="")  # аргумент
    
    # Вывод точек для всех аргументов с погрешностью dot_eps
    j = 0
    dot_found = False  # поставлена ли точка с данным аргументом
    x_found = False  # поставлена ли ось абсцисс
    while (min_f2+r/cell_size*j) - max_f2 - 2*r <= eps:
        approx_eps = abs((21.987 - 10.112*2**i) - (min_f2+r/(cell_size+1)*j))  # Примерная погрешность
        #print((21.987 - 10.112*2**i), approx_eps)
        if abs((min_f2+r/cell_size*j)) <= dot_eps and not(x_found):
            print(f"|", end="") 
            x_found = True   # Нашли ось абсцисс
        elif approx_eps <= dot_eps and not(dot_found):
            print(f"*", end="") 
            dot_found = True  # Нашли расположение точки
        else:
            print(" ", end="")
        j += 1
    print("")
    
    i += h