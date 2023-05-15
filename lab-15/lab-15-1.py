"""
Смирнов Иван ИУ7-12Б Лабработа№15 "Бинарные файлы" Часть 1
Программа реализовывает ввод 4-байтных чисел в файл (если
файл существует - перезаписывает) и выводит содержимое изменённого
файла после:
1. Удаления всех нулевых элементов (за один проход по файлу)
Для формирования записей фиксированного размера (структур) в бинарном формате
используется модуль struct.
"""

# Импортируем модули
import struct as st

file_name = "1.bin"
str_format = 'i'
len_str = st.calcsize(str_format)

# Функция для нахождения размера бинарного файла
def fsize(file):
    with open(file, "rb"):
        f.seek(0, 2)
        size = f.tell()
        f.seek(0)
    return size

# Создание бинарного файла и заполнения его числами
with open(file_name, "wb") as f:
    while True:
        try:
            n = int(input("Введите количество чисел: "))
            if n <= 0:
                print("Пожалуйста, введите положительное количество чисел!")
            else:
                break
        except Exception:
            print("Произошла ошибка ввода данных. Вы точно ввели целое число?")
    i = 0
    while i < n:
        try:
            num = int(input(f"Введите {i+1}-е число: "))
            bin_str = st.pack(str_format, num)
            f.write(bin_str)
            i += 1
        except Exception:
            print("Произошла ошибка ввода данных. Вы точно ввели целое число?") 

# Удаление из бинарного файла нулевых элементов 
with open(file_name, "rb+") as f:
    size = fsize(file_name)
    zero_cnt = 0
    for i in range(size//len_str):
        num = st.unpack(str_format, f.read(len_str))[0]
        if num == 0:
            zero_cnt += 1
        else:
            f.seek(-len_str*(zero_cnt+1), 1)
            f.write(st.pack(str_format, num))
            f.seek(len_str*(i+1))
    f.truncate(len_str*(n-zero_cnt))

# Вывод содержимого бинарного файла:
print("\nВывод содержимого бинарного файла:")
with open(file_name, "rb") as f:
    size = fsize(file_name)
    if size == 0:
        print("- Файл пуст")
    for i in range(size//len_str):
        print(f"{i+1}-й элемент: {st.unpack(str_format, f.read(len_str))[0]}")
    
