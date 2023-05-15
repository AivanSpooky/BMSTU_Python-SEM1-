"""
Смирнов Иван ИУ7-12Б Лабработа№15 "Бинарные файлы" Часть 1
Программа реализовывает ввод 4-байтных чисел в файл (если
файл существует - перезаписывает) и выводит содержимое изменённого
файла после:
2. Добавления удвоенного числа после каждого нечетного (по значению) элемента
Для формирования записей фиксированного размера (структур) в бинарном формате
используется модуль struct.
"""

# Импортируем модули
import struct as st

file_name = "2.bin"
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
            f.write(st.pack(str_format, num))
            i += 1
        except Exception:
            print("Произошла ошибка ввода данных. Вы точно ввели целое число?") 

# Добавление удвоенного элемента после каждого нечетного (по значению) элемента
with open(file_name, "rb+") as f:
    size = fsize(file_name)
    odd_cnt = 0
    for i in range(size//len_str):
        num = st.unpack(str_format, f.read(len_str))[0]
        if num % 2 == 1:
            odd_cnt += 1
            f.seek(0, 2)
            f.write(st.pack(str_format, 0))
            f.seek(len_str*(i+1))

    for i in range((size//len_str)-1, -1, -1):
        f.seek(len_str*i)
        num = st.unpack(str_format, f.read(len_str))[0]
        if num % 2 == 1:
            f.seek(len_str*(odd_cnt-1), 1)
            f.write(st.pack(str_format, num*2))
            f.seek(-2*len_str, 1)
            f.write(st.pack(str_format, num))
            odd_cnt -= 1
        else:
            f.seek(len_str*(odd_cnt-1), 1)
            f.write(st.pack(str_format, num))


# Вывод содержимого бинарного файла:
print("\nВывод содержимого бинарного файла:")
with open(file_name, "rb") as f:
    size = fsize(file_name)
    if size == 0:
        print("- Файл пуст")
    for i in range(size//len_str):
        print(f"{i+1}-й элемент: {st.unpack(str_format, f.read(len_str))[0]}")
    
