"""
Смирнов Иван ИУ7-12Б Лабработа№13 "База данных в текстовом файле"
Программа позволяет с помощью меню выполнить следующие действия:
1. Выбрать файл для работы
2. Инициализировать базу данных (создать либо перезаписать файл и заполнить
его записями)
3. Вывести содержимое базы данных
4. Добавить запись в конец базы данных
5. Поиск по одному полю
6. Поиск по двум полям
7. Выход из программы
"""
# -*- coding: cp1251 -*-
# Импортируем модули
import os.path

"""
Примерная база данных (тематика - страны)
Поля:
- код страны (3 заглавные буквы)
- континент (строка)
- площадь (число)
- является ли страна республикой (число 0-1)
"""
db = []

# Функция для нахождения максимальной длинны каждого поля
def max_len(file):
    try:
        with open(file, "r", encoding='utf-8') as f:
            pass
    except Exception:
        print("Файл нельзя прочитать.")
        return
    with open(file, "r", encoding="utf-8") as f:
        max_lens = [3, 0, 0, 0]
        f = f.readlines()
        for i in range(len(f)):
            line = f[i].split(",")
            if len(line) != 4:
                print("База данных задана неправильно! (Количество полей отлично от 4)")
                return None
            for j in range(4):
                if j > 0:
                    max_lens[j] = max(max_lens[j], len(line[j]))
        return max_lens

# Функция для вывода баз данных
def printdb(file, len_list, find_cr=None):
    allowed = True
    printed = False
    forb_words = "~!@#$%^&*()_+`1234567890-=,./<>?|{}[]"
    try:
        with open(file, "r", encoding='utf-8') as f:
            pass
    except Exception:
        print("Файл нельзя прочитать.")
        return
    with open(file, "r", encoding='utf-8') as f:
        line = f.readline()
        while line != "":
            line = line.split(",")
            if len(line) != 4:
                print("База данных задана неправильно! (Количество полей отлично от 4)")
                return
            for i in range(1, 5):
                el = line[i-1]
                if i == 1:
                    if len(el) != 3:
                        print("База данных задана неправильно! (Код страны введен некорректно)")
                        return
                    for let in el:
                        if let in forb_words:
                            print("База данных задана неправильно! (Код страны введен некорректно)")
                            return
                    line[i-1] = el.upper()
                elif i == 2:
                    for let in el:
                        if let in forb_words:
                            print("База данных задана неправильно! (Континент введен некорректно)")
                            return
                elif i == 3:
                    if not(el.isdigit()):
                        print("База данных задана неправильно! (Население введено некорректно)")
                        return
                else:
                    if el[-1] != "\n":
                        print("База данных задана неправильно!")
                        print("(Последний символ в записи должен быть переход на новую строку)")
                        return
                    el = el[:len(el)-1]
                    if not(el.isdigit()):
                        print("База данных задана неправильно! (Республика введена некорректно)")
                        return
                    elif int(el) < 0 or int(el) > 1:
                        print("База данных задана неправильно! (Республика введена некорректно)")
                        return
                    line[i-1] = el
                if find_cr != None:
                    for p in find_cr:
                        if p[0] == i:
                            if line[i-1] == p[1] and allowed:
                                allowed = True
                            else:
                                allowed = False
            if allowed:
                printed = True
                print(f"|", end="")
                for i in range(4):
                    print(f"{line[i]:^{len_list[i]+2}}|", end="")
                print()
            line = f.readline()
            allowed = True
        if not(printed):
            print("\nНичего не было выведено")

# Функция для заполнения записей
def makelines(file, atr, line_count):
    try:
        with open(file, atr, encoding="utf-8") as f:
            pass
    except Exception:
        print("Произошла ошибка с файлом (возможно права файла не позволяют сделать действия)")
        return
    with open(file, atr, encoding="utf-8") as f:
        for i in range(line_count):
            print(f"\nЗаполнение записи #{i+1}")
            line = []
            while True:
                code = input("Введите код страны: ")
                if len(code) != 3:
                    print("Вы ввели код страны некорректно!")
                    continue
                for let in code:
                    if let in forb_words:
                        print("Вы ввели код страны некорректно!")
                        break
                else:
                    code = code.upper()
                    line.append(code)
                    break
            while True:
                cont = input("Введите континент, на котором находится страна: ")
                for let in cont:
                    if let in forb_words:
                        print("Вы ввели континент некорректно!")
                        break
                else:
                    line.append(cont)
                    break
            while True:
                people = input("Введите население страны: ")
                if people.isdigit():
                    line.append(people)
                    break
                print("Вы ввели население некорректно!")
            while True:
                rep = input("Введите является ли страна республикой (0 - нет, 1 - да): ")
                if rep.isdigit():
                    rep = int(rep)
                    if rep < 0 or rep > 1:
                        print("Вы ввели значение некорректно!")
                        continue
                    line.append(str(rep))
                    break
                print("Вы ввели население некорректно!")
            f.write(",".join(line))
            line = []
            f.write("\n")         
                    

# Вывод меню
f = None
file = None
# Запрещенные символы (для заполнения записей)
forb_words = "~!@#$%^&*()_+`1234567890-=,./<>?|{}[]"
while True:
    print(f"\n\nМеню действий с базой данных (в текстовом файле)")
    print(f"Доступные команды:")
    print(f"1 - Выбрать файл для работы")
    print(f"2 - Инициализировать базу данных")
    print(f"3 - Вывести содержимое базы данных")
    print(f"4 - Добавить запись в конец базы данных")
    print(f"5 - Поиск по одному полю")
    print(f"6 - Поиск по двум полям")
    print(f"7 - Завершить программу")
    try:
        n = int(input("Введите номер команды: "))
    except Exception:
        print("Произошла ошибка ввода данных. Вы точно ввели число?")
        continue
    if n <= 0 or n >= 8:
        print("Вы ввели несуществующий номер команды!")
    elif n == 1:
        # Проверяем файл на существование
        while True:
            file = input(f"\nВведите название файла для работы: ")
            if file == "0":
                file = None
                break
            elif not(os.path.exists(file)):
                print("Вы ввели несуществующий файл!")
                print("Если хотите вернуться к командам, напишите '0'")
            else:
                break
    elif n == 2:
        # Проверяем, что введен файл .txt
        while True:
            file = input(f"\nВведите файл, в котором вы хотите создать бд\n" \
                         "или перезаписать его и создать новую бд: ")
            if file.endswith(".py"):
                print("Вы не можете открыть этот файл!")
            else:
                break
        # Заполняем файл записями
        while True:
            try:
                line_count = int(input("Введите количество записей: "))
                break
            except Exception:
                print("Произошла ошибка ввода данных. Вы точно ввели число?")
        # Сделать line_count записей
        makelines(file, "w", line_count)
    elif n == 3:
        if file == None:
            print("Вы не выбрали файл!")
        else:
            print("\n")
            len_list = max_len(file)
            if len_list != None:
                printdb(file, len_list)
    elif n == 4:
        if file == None:
            print("Вы не выбрали файл!")
        else:
            print("\n")
            # Сделать запись в конец
            makelines(file, "a", 1)
    elif n == 5:
        if file == None:
            print("Вы не выбрали файл!")
        else:
            print()
            while True:
                try:
                    num = int(input("Введите номер поля (по которому совершить поиск): "))
                    if num <= 0 or num >= 5:
                        print("Пожалуйста, введите существующий номер поля! (от 1 до 4)")
                    else:
                        break
                except Exception:
                    print("Произошла ошибка ввода данных. Вы точно ввели число?")
            criteria = input("Введите критерий выбранного поля, по которому необходимо найти записи: ")
            print()
            len_list = max_len(file)
            if len_list != None:
                printdb(file, len_list, [[num, criteria]])            
    elif n == 6:
        if file == None:
            print("Вы не выбрали файл!")
        else:
            print()
            while True:
                try:
                    n1 = int(input("Введите номер 1-ого поля (по которому совершить поиск): "))
                    if n1 <= 0 or n1 >= 5:
                        print("Пожалуйста, введите существующий номер поля! (от 1 до 4)")
                    else:
                        break
                except Exception:
                    print("Произошла ошибка ввода данных. Вы точно ввели число?")
            cr1 = input("Введите критерий 1-ого поля, по которому необходимо найти записи: ")
            print()
            while True:
                try:
                    n2 = int(input("Введите номер 2-ого поля (по которому совершить поиск): "))
                    if n2 <= 0 or n2 >= 5:
                        print("Пожалуйста, введите существующий номер поля! (от 1 до 4)")
                    elif n2 == n1:
                        print("Пожалуйста, введите другой номер поля! (отличный от первого)")
                    else:
                        break
                except Exception:
                    print("Произошла ошибка ввода данных. Вы точно ввели число?")
            cr2 = input("Введите критерий 2-ого поля, по которому необходимо найти записи: ")
            len_list = max_len(file)
            if len_list != None:
                printdb(file, len_list, [[n1, cr1], [n2, cr2]])
    elif n == 7:
        break
