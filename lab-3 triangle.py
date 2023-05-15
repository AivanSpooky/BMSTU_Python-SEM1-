# Смирнов ИУ7-12Б Лаб. работа №3 - Треугольник

# ввод координат точек треугольника
x_a = int(input("Введите координату x точки A: "))
y_a = int(input("Введите координату у точки A: "))
x_b = int(input("Введите координату x точки B: "))
y_b = int(input("Введите координату у точки B: "))
x_c = int(input("Введите координату x точки C: "))
y_c = int(input("Введите координату у точки C: "))

# считаем стороны AB BC AC по координатам
ab = ((x_a - x_b)**2+(y_a - y_b)**2)**0.5
bc = ((x_b - x_c)**2+(y_b - y_c)**2)**0.5
ac = ((x_a - x_c)**2+(y_a - y_c)**2)**0.5
print(f"\nСтороны треугольника: AB={ab:.5f} BC={bc:.5f} AC={ac:.5f}")

# считаем длину биссектрисы, проведенной из наибольшего угла
max_side = max(ab, bc, ac)
if max_side == ab:   # угол С - наибольший?
    bisector = (bc*ac*(bc+ac+ab)*(bc+ac-ab))**0.5/(bc+ac)
elif max_side == bc:   # угол A - наибольший?
    bisector = (ab*ac*(ab+ac+bc)*(ab+ac-bc))**0.5/(ab+ac)
else:   # угол B - наибольший
    bisector = (ab*bc*(ab+bc+ac)*(ab+bc-ac))**0.5/(ab+bc)
print(f"Длина биссектрисы, проведенной из наибольшего угла равна {bisector:.5f}")

# определяем, является ли треугольник тупоугольным
if ab**2>(bc**2+ac**2) or bc**2>(ab**2+ac**2) or ac**2>(ab**2+bc**2):
    print(f"Треугольник является тупоугольным")
else:
    print(f"Треугольник не тупоугольный")
    
# ввод координат новой точки K
x_k = int(input("\nВведите координату x новой точки K: "))
y_k = int(input("Введите координату y новой точки K: "))

# определяем, где находится точка относительно треугольника
cond1 = (x_a - x_k)*(y_b - y_a) - (x_b - x_a)*(y_a - y_k) # относительно ab
cond2 = (x_b - x_k)*(y_c - y_b) - (x_c - x_b)*(y_b - y_k) # относительно bc
cond3 = (x_c - x_k)*(y_a - y_c) - (x_a - x_c)*(y_c - y_k) # относительно ac
# print(cond1, cond2, cond3)
if (cond1<0 and cond2<0 and cond3<0) or (cond1>0 and cond2>0 and cond3>0):
    print(f"\nТочка лежит внутри треугольника")
    # считаем стороны AK BK CK
    ak = ((x_a - x_k)**2+(y_a - y_k)**2)**0.5
    bk = ((x_b - x_k)**2+(y_b - y_k)**2)**0.5
    ck = ((x_k - x_c)**2+(y_k - y_c)**2)**0.5
    
    # считаем полупериметры полученных треугольников ABK, BCK, ACK
    p_abk = (ab+ak+bk)/2
    p_bck = (bc+bk+ck)/2
    p_ack = (ac+ak+ck)/2
    
    # считаем высоты треугольников ABK, BCK, ACK проведенных из K (расстояния)
    height_to_ab = 2/ab*(p_abk*(p_abk-ab)*(p_abk-ak)*(p_abk-bk))**0.5
    height_to_bc = 2/bc*(p_bck*(p_bck-bc)*(p_bck-bk)*(p_bck-ck))**0.5
    height_to_ac = 2/ac*(p_ack*(p_ack-ac)*(p_ack-ak)*(p_ack-ck))**0.5
    distance = min(height_to_ab, height_to_bc, height_to_ac) # минимум из высот
    print(f"Расстояние от точки K до ближайшей стороны равно {distance:.5f}")
    
elif cond1==0 or cond2==0 or cond3==0:
    print(f"\nТочка лежит на стороне треугольника")
    print(f"Расстояние от точки до ближайшей стороны равно 0")
else:
    print(f"\nТочка лежит вне треугольника")