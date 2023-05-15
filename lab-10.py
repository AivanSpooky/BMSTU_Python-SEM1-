"""
Смирнов Иван ИУ7-12Б Лабработа№10 "Вычисление приближённого значения интеграла"
Программа вычисляет приближённое значение интеграла по заданной в программе
формуле двумя способами (метод серединных прямоугольников и метод парабол).
"""

# Первообразная функция
def greater_func(x):
    return x**5/5+x**4/4-x**3*2/3+x**2/2-5*x

# Функция
def function(x):
    return x**4 + x**3 - 2*x**2 + x - 5

# Метод серединных прямоугольников
def middle_rectangles(start, end, n):
    global eps
    step = (end-start)/n  # Шаг итерации для N разбиений
    i = start+step  # Счетчик
    mid_rect_summ = 0
    while i - end < eps:
        mid_rect_summ += function((i + i-step)/2)*step
        i += step
    return mid_rect_summ

# Метод парабол
def parabola(start, end, n):
    if n % 2 == 1:
        return "-"
    h = (end-start)/(n)
    par_summ = function(start) + function(end)
    for i in range(1, n):
        if i%2 != 0:
            par_summ += 4*function(start + i*h)
        else:
            par_summ += 2*function(start + i*h)
    return par_summ * h / 3

# Абсолютная погрешность
def absolute_error(method):
    global real
    return abs(method - real) if abs(method - real) != 0 else 1e-10

# Относительная погрешность
def relative_error(abs_err):
    global real
    return abs(abs_err / real) if real != 0 else "-"


# Ввод начала и конца отрезка интегрирования, а также N1 и N2 - количество
# разбиений отрезка интегрирования.
while True:
    try:
        start = float(input("Введите начало отрезка интегрирования: "))
        break
    except Exception:
        print("Произошла ошибка ввода данных. Вы точно ввели число?")
while True:
    try:
        end = float(input("Введите конец отрезка интегрирования: "))
        if end <= start:
            print(f"Конец должен быть больше старта ({start})")
        else:
            break
    except Exception:
        print("Произошла ошибка ввода данных. Вы точно ввели число?")
while True:
    try:
        n1 = int(input("Введите количество разбиений отрезка интегрирования (N1): "))
        if n1 <= 0:
            print("Введите положительное количество разбиений")
        else:
            break
    except Exception:
        print("Произошла ошибка ввода данных. Вы точно ввели целое число?")
while True:
    try:
        n2 = int(input("Введите количество разбиений отрезка интегрирования (N2): "))
        if n2 <= 0:
            print("Введите положительное количество разбиений")
        else:
            break
    except Exception:
        print("Произошла ошибка ввода данных. Вы точно ввели целое число?")

# Вычисляем примерное значение интеграла методом серединных прямоугольников
eps = 1e-8  # Погрешность для сравнения вещественных чисел
n1_midrect = middle_rectangles(start, end, n1)  # Итеграл для N1 разбиений
n2_midrect = middle_rectangles(start, end, n2)  # Итеграл для N2 разбиений

# Вычисляем примерное значение интеграла методом парабол
n1_parabola = parabola(start, end, n1)  # Итеграл для N1 разбиений
n2_parabola = parabola(start, end, n2)  # Итеграл для N2 разбиений

# Вывод таблицы
print("\n\n")
print(f"{'':<32}|{'N1':<16}|{'N2':<16}")
print(f"-"*66)
print(f"{'Метод серединных прямоугольников':<30}|{n1_midrect:<16.8f}|{n2_midrect:<16.8f}")
print(f"-"*66)
print(f"{'Метод парабол':<32}|{n1_parabola:<16.8f}|{n2_parabola:<16.8f}")

# Подсчет абсолютной и относительной погрешности для каждого из методов
real = greater_func(end)-greater_func(start)  # Реальное значение интеграла
if real < eps:
    real = 0

# Считаем абсолютную и относительную погрешности для каждого из методов
abs_err_1_n1 = absolute_error(n1_midrect)
abs_err_1_n2 = absolute_error(n2_midrect)
abs_err_2_n1 = absolute_error(n1_parabola)
abs_err_2_n2 = absolute_error(n2_parabola)

rel_err_1_n1 = relative_error(abs_err_1_n1)
rel_err_1_n2 = relative_error(abs_err_1_n2)
rel_err_2_n1 = relative_error(abs_err_2_n1)
rel_err_2_n2 =  relative_error(abs_err_2_n2)

# Выводим погрешности для соответствующих методов и количества итераций
print(f"\n\nМетод серединных прямоугольников")
if real == 0:
    print(f"Для {n1} разбиений:")
    print(f"Абс. погрешность: {abs_err_1_n1:<10.5g} Отн. погрешность: {rel_err_1_n1:<10.5}")
    print(f"Для {n2} разбиений:")
    print(f"Абс. погрешность: {abs_err_1_n2:<10.5g} Отн. погрешность: {rel_err_1_n2:<10.5}")
    print(f"\nМетод парабол")
    print(f"Для {n1} разбиений:")
    print(f"Абс. погрешность: {abs_err_2_n1:<10.5g} Отн. погрешность: {rel_err_2_n1:<10.5}")
    print(f"Для {n2} разбиений:")
    print(f"Абс. погрешность: {abs_err_2_n2:<10.5g} Отн. погрешность: {rel_err_2_n2:<10.5}")
else:
    print(f"Для {n1} разбиений:")
    print(f"Абс. погрешность: {abs_err_1_n1:<10.5g} Отн. погрешность: {rel_err_1_n1:<10.5g}")
    print(f"Для {n2} разбиений:")
    print(f"Абс. погрешность: {abs_err_1_n2:<10.5g} Отн. погрешность: {rel_err_1_n2:<10.5g}")
    print(f"\nМетод парабол")
    print(f"Для {n1} разбиений:")
    print(f"Абс. погрешность: {abs_err_2_n1:<10.5g} Отн. погрешность: {rel_err_2_n1:<10.5g}")
    print(f"Для {n2} разбиений:")
    print(f"Абс. погрешность: {abs_err_2_n2:<10.5g} Отн. погрешность: {rel_err_2_n2:<10.5g}")    

# Находим наиболее точный метод и сохраняем его в переменной accurate_method
# Метод сер. прям. - 1; Метод парабол - 2.
print("\nНаиболее точный метод:")
most_accurate = min(abs_err_1_n1, abs_err_1_n2, abs_err_2_n1, abs_err_2_n2)
eps = most_accurate/2
if abs_err_1_n1 - most_accurate < eps:
    print(f"Метод серединных прямоугольников для {n1} итераций")
    accurate_method = 1
elif abs_err_1_n2 - most_accurate < eps:
    print(f"Метод серединных прямоугольников для {n2} итераций")
    accurate_method = 1
elif abs_err_2_n1 - most_accurate < eps:
    print(f"Метод парабол для {n1} итераций")
    accurate_method = 2
else:
    print(f"Метод парабол для {n2} итераций")
    accurate_method = 2

# Находим при скольких итераций менее точный метод достигнет точности более точного
n = 1
current_accuracy = None  # Точность для текущего n
next_accuracy = None  # Точность для 2*n
if accurate_method == 1:
    while current_accuracy == None or abs(current_accuracy - next_accuracy) > eps:
        current_accuracy, next_accuracy = next_accuracy, parabola(start, end, n)
        n *= 2
else:
    while current_accuracy == None or abs(current_accuracy - next_accuracy) > eps:
        current_accuracy, next_accuracy = next_accuracy, middle_rectangles(start, end, n)
        n *= 2

# Вывод необходимого количества итераций
print(f"\nДля достижения максимальной точности менее точным методом необходимо \
{n} итераций")