"""
Смирнов Иван ИУ7-12Б Лабработа№13 Защита
С помощью введенного пользователем файла с целочисленной матрицей (корректно заданной)
создать новый файл output.txt с транспонированной матрицей. Данные из исходной
матрицы хранятся построчно (не целиком).
"""

import os

file = input("Введите файл для транспонирования матрицы: ")
try:
    if file == "output.txt":
        print("Пожалуйста, введите другое имя файла!")
        exit(1)
    f = open(file, "r")
    line = f.readline().strip()
    n = None
    m = 0
    while line != "":
        nums = line.split(" ")
        for i in nums:
            if i == "":
                print("Ошибка ввода данных (возможно в файле присутствуют лишние пробелы)")
                exit(1) 
            if not(i.isdigit()):
                print("Ошибка ввода данных (в матрице есть элемент, который не является целым числом)")
                exit(1)
        if n == None:
            n = len(nums)
        if len(nums) != n:
            print("Ошибка ввода данных (матрица не является квадратной)")
            exit(1)
        line = f.readline().strip()
        m += 1
    if n == None:
        print("Ошибка ввода данных (возможно файл пустой или состоит из пробельных символов)")
        exit(1) 
    if m != n:
        print("Ошибка ввода данных (матрица не является квадратной)")
        exit(1)
    f.close()
except Exception:
    print("Файл не удается открыть (возможно его не существует или нет прав на открытие).")
    exit(1)   
if os.path.exists("output.txt"):
    try:
        os.remove("output.txt")
    except Exception:
        print("Произошла ошибка. (файл output.txt был поврежден, удалите его)")
        exit(1)
        
        
f1 = open("output.txt", "w")
f = open(file, "r") 
l = 0
while l < n:
    for i in range(n):
        line = f.readline().strip().split(" ")
        f1.write(line[l] + " ")
    f1.write("\n")
    l += 1
    f.seek(0)
print("Транспонированная матрица выведена в файл output.txt")
f.close()
f1.close()