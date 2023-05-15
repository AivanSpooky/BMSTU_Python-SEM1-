# Смирнов ИУ7-12Б Программа по блок-схеме

#ввод коэффициентов квадратного уравнения
a = float(input("Введите коэффициент а: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

#вычисление корней
if a == 0:        # если а = 0, то получаем линейное уравнение, иначе квадратное
    if b == 0:
        if c == 0:
            print("Уравнение имеет бесконечное количество корней")
        else:
            print("Уравнение не имеет корней")    
    else:
        x = -c/b if c != 0 else 0        # единственный корень линейного уравнения
        print(f"X = {x:.5g}")
else:
    d = b**2-4*a*c        # считаем дискриминант квадратного уравнения
    if d < 0:
        print("Уравнение не имеет корней")
    elif d == 0:
        x = -b/(2*a)        # единственный корень квадратного уравнения
        print(f"X = {x:.5g}")
    else:
        x1 = (-b+(d**0.5))/(2*a)
        x2 = (-b-(d**0.5))/(2*a)        # два корня квадратного уравнения
        print(f"X1 = {x1:g}\nX2 = {x2:g}")

        
    
    
