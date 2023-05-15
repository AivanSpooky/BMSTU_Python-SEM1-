# Смирнов Иван ИУ7-12Б   Тетраэдр (дана длина ребра a, найти высоту h, S и V, 
# радиусы описанной и вписанной сфер).

# Ввод ребра + проверка на положительность введеного числа
a = 0
while a <= 0:    
    a = float(input("Введите длину ребра тетраэдра(положительное число): "))
    
# Вычисление
h = a * (6 ** 0.5) / 3            # вычисление высоты тетраэдра
S = a ** 2 * (3 ** 0.5)            # вычисление площади поверхности тетраэдра
V = a ** 3 * (2 ** 0.5) / 12            # вычисление объема тетраэдра
R = a * (6 ** 0.5) / 4            # вычисление радиуса описанной около тетраэдра сферы
r = a * (6 ** 0.5) / 12            # вычисление радиуса вписаноой в тетраэдр сферы

# Вывод полученных значений (с отображением данных в 5 значащих цифр)
print(f"Высота тетраэдра: {h:.5g}")
print(f"Площадь поверхности тетраэдра: {S:.5g}")
print(f"Объем тетраэдра: {V:.5g}")
print(f"Радиус описанной около тетраэдра сферы: {R:.5g}")
print(f"Радиус вписанной около тетраэдра сферы: {r:.5g}")