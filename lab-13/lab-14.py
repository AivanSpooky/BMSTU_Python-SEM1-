"""
Смирнов Иван ИУ7-12Б Лабработа№14 "База данных в бинарном файле"
Программа позволяет с помощью меню выполнить следующие действия:
1. Выбрать файл для работы
2. Инициализировать базу данных (создать либо перезаписать файл и заполнить
его записями)
3. Вывести содержимое базы данных
4. Добавить запись в произвольное место базы данных (пользователь указывает
номер позиции, в которую должна быть вставлена запись)
5. Удалить произвольную запись из базы данных (пользователь указывает номер
удаляемой записи)
6. Поиск по одному полю
7. Поиск по двум полям
8. Выход из программы
Для формирования записей фиксированного размера (структур) в бинарном формате
используется модуль struct.
"""

# Импортируем модули
import os.path
import struct

len_str = 57
string_format = '6s40sq?'

"""
Примерная база данных (тематика - страны)
Поля:
- код страны (3 заглавные буквы)
- континент (строка)
- площадь (число)
- является ли страна республикой (число 0-1)
"""

# Функция для проверки файла на бинарность и базу данных
def check_bin(file):
    try:
        f = open(file, 'rb')
        f.seek(0, 2)
        pointer = f.tell()
        if pointer % len_str != 0:
            print("\nОшибка, это не база данных")
            f.close()
            return None
        f.close()
        return True
    except Exception:
        print("\nФайл не является бинарным (или его нельзя открыть)")
        return None

# Функция для проверки файла (на чтение) и вывод его длины
def db_size(file):
    try:
        with open(file, "rb") as f:
            f.seek(0, 2)
            size = f.tell()
            f.seek(0)
            return size
    except Exception:
        return None

# Функция для нахождения максимальной длинны каждого поля
def max_len():
    return [3, 20, 12, 1]

# Функция для вывода баз данных
def printdb(file, len_list, find_cr=None):
    allowed = True
    printed = False
    forb_words = "~!@#$%^&*()_+`1234567890-=,./<>?|{}[]"
    # try:
    #     with open(file, "rb", encoding='utf-8') as f:
    #         pass
    # except Exception:
    #     print("Файл нельзя прочитать.")
    #     return
    headers = ["Код", "Континент", "Население", "Р"]
    print(f"|{headers[0]:^5}|{headers[1]:^22}|{headers[2]:^14}|{headers[3]:^3}|")

    with open(file, "rb") as f:
        size = db_size(file)


        for _ in range(size // len_str):
            line = f.read(len_str)
            line = list(struct.unpack(string_format, line))

            line[0] = line[0].decode('utf-8')
            line[0] = line[0].replace('\x00', '')

            line[1] = line[1].decode('utf-8')
            line[1] = line[1].replace('\x00', '')

            #print(line)
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
                    if len(el) > 20:
                        print("База данных задана неправильно! (Континент введен некорректно)")
                        return
                    for let in el:
                        if let in forb_words:
                            print("База данных задана неправильно! (Континент введен некорректно)")
                            return
                elif i == 3:
                    if len(str(el)) > 12:
                        print("База данных задана неправильно! (Население введено некорректно)")
                        return
                    if type(el) != int:
                        print("База данных задана неправильно! (Население введено некорректно)")
                        return
                else:
                    if type(el) != bool or el not in (0, 1):
                        print("База данных задана неправильно! (Республика введена некорректно)")
                        return
                    line[i-1] = el
                if find_cr != None:
                    for p in find_cr:
                        if p[0] == i:
                            if (str(line[i-1]) == str(p[1]) or line[i-1] == int(p[1])) and allowed:
                                allowed = True
                            else:
                                allowed = False
            if allowed:
                printed = True
                print(f"|", end="")
                for i in range(4):
                    print(f"{line[i]:^{len_list[i]+2}}|", end="")
                print()
            allowed = True
        if not(printed):
            print("\nНичего не было выведено")

# Функция для заполнения записей
def makelines(file, atr, line_count, pos=None):
    try:
        with open(file, atr) as f:
            pass
    except Exception:
        print("Произошла ошибка с файлом (возможно права файла не позволяют сделать действия)")
        return
    with open(file, atr) as f:
        for i in range(line_count):
            print(f"\nЗаполнение записи #{i+1}")
            while True:
                code = input("Введите код страны: ")
                if len(code) != 3:
                    print("Вы ввели код страны некорректно! (Код должен состоять из 3х букв)")
                    continue
                for let in code:
                    if let in forb_words:
                        print("Вы ввели код страны некорректно!")
                        break
                else:
                    code = code.upper()
                    break
            while True:
                cont = input("Введите континент, на котором находится страна: ")
                if len(cont) > 20:
                    print("Вы ввели континент некорректно! (Должно быть не более 20 букв)")
                    continue
                for let in cont:
                    if let in forb_words:
                        print("Вы ввели континент некорректно!")
                        break
                else:
                    break
            while True:
                people = input("Введите население страны: ")
                if len(people) > 12:
                    print("Вы ввели население некорректно! (Максимум 12 цифр или не число)")
                    continue
                if people.isdigit():
                    people = int(people)
                    break
                print("Вы ввели население некорректно!")
            while True:
                rep = input("Введите является ли страна республикой (0 - нет, 1 - да): ")
                if rep.isdigit():
                    rep = int(rep)
                    if rep < 0 or rep > 1:
                        print("Вы ввели значение некорректно!")
                        continue
                    break
                print("Вы ввели население некорректно!")
            bytestr = struct.pack(string_format, code.encode("utf-8"), cont.encode("utf-8"), people, rep)
            if pos == None:
                f.write(bytestr)   
            else:  # Если необходимо добавить в определенное место
                size = db_size(file)
                if size == None:
                    print("Файл недоступен для чтения!")
                    return
                with open(file, "rb+") as f:
                    j = 0
                    f.seek(len_str*(pos-1)+len_str*j)
                    while f.tell() < size:
                        f.seek(len_str*(pos-1)+len_str*j)
                        temp = f.read(len_str)
                        f.seek(f.tell() - len_str)
                        f.write(bytestr)
                        bytestr = temp 
                        j += 1
                with open(file, "ab") as f:
                    f.write(bytestr) 

# Функция для удаления записи
def delete_line(file, pos):
    try:
        with open(file, "ab") as f:
            pass
    except Exception:
        print("Файл нельзя редактировать!")
        return
    
    # Удаляем запись с номером pos
    size = db_size(file)
    with open(file, "rb+") as f:
        j = 0
        f.seek(len_str*(pos-1)+len_str*(j+1))
        while f.tell() < size:
            f.seek(len_str*(pos-1)+len_str*(j+1))
            temp = f.read(len_str)
            f.seek(f.tell() - len_str*2)
            f.write(temp)
            j += 1
    with open(file, "ab") as f:
        f.truncate(size-len_str)

                    

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
    print(f"4 - Добавить запись в произвольное место базы данных")
    print(f"5 - Удалить запись из произвольного места базы данных")
    print(f"6 - Поиск по одному полю")
    print(f"7 - Поиск по двум полям")
    print(f"8 - Завершить программу")
    try:
        n = int(input("Введите номер команды: "))
    except Exception:
        print("Произошла ошибка ввода данных. Вы точно ввели число?")
        continue
    if n <= 0 or n >= 9:
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
        # Проверяем, что введен файл
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
        makelines(file, "wb", line_count)
    elif n == 3:
        if file == None:
            print("\nВы не выбрали файл!")
        elif check_bin(file) == None:
            pass
        else:
            print("\n")
            len_list = max_len()
            if len_list != None:
                printdb(file, len_list)
    elif n == 4:
        if file == None:
            print("\nВы не выбрали файл!")
        elif check_bin(file) == None:
            pass
        elif db_size(file) == None:
            print("\nФайл нельзя открыть!")
        else:
            print("\n")
            while True:
                try:
                    line_num = int(input("Введите номер новой записи: "))
                    if line_num <= 0 or line_num > (db_size(file)//len_str)+1:
                        print("Введите существующий номер записи!")
                        continue
                    break
                except Exception:
                    print("Пожалуйста, введите число.")
            # Добавить запись в определенное место
            makelines(file, "a", 1, line_num)
    elif n == 5:
        if file == None:
            print("\nВы не выбрали файл!")
        elif check_bin(file) == None:
            pass
        elif db_size(file) == None:
            print("\nФайл нельзя открыть!")
        elif (db_size(file)//len_str) == 0:
            print("\nФайл пустой.")
        else:
            print("\n")
            while True:
                try:
                    line_num = int(input("Введите номер записи, которую необходимо удалить: "))
                    if line_num <= 0 or line_num > (db_size(file)//len_str):
                        print("Введите существующий номер записи!")
                        continue
                    break
                except Exception:
                    print("Пожалуйста, введите число.")
            # Удаление записи из определенного места
            delete_line(file, line_num)
    elif n == 6:
        if file == None:
            print("\nВы не выбрали файл!")
        elif check_bin(file) == None:
            pass
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
            len_list = max_len()
            if len_list != None:
                printdb(file, len_list, [[num, criteria]])            
    elif n == 7:
        if file == None:
            print("\nВы не выбрали файл!")
        elif check_bin(file) == None:
            pass
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
            len_list = max_len()
            if len_list != None:
                printdb(file, len_list, [[n1, cr1], [n2, cr2]])
    elif n == 8:
        break
