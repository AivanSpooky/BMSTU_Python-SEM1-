"""
Смирнов Иван Лабработа№12 "Работа с текстом"
Написать программу для выполнения некоторых операций с текстом. Вводить текст не
требуется, он должен быть задан в исходном тексте программы в виде списка строк
(при выводе на экран каждый элемент этого списка должен начинаться с новой
строки). С помощью меню команд необходимо реализовать 7 действий над текстом:
1 - Выровнять текст по левому краю.
2 - Выровнять текст по правому краю.
3 - Выровнять текст по ширине.
4 - Удаление всех вхождений заданного слова.
5 - Замена одного слова другим во всём тексте.
6 - Вычисление арифметических выражений над целыми числами внутри текста
(+ и -).
7 - Найти (вывести на экран) и затем удалить слово
Наиболее часто встречающееся слово в каждом предложении.
8 - Выход из программы
"""

# Функция для создания предложений из списка строк
def make_sentences_list(ls):
    sentences_list = []
    cur_sentence = ""
    for i in ls:
        if ("." in i and i[-1] != ".") or i.count(".")>1:
            while "." in i:
                dot_ind = i.index(".")
                cur_sentence += i[:dot_ind+1]
                sentences_list.append(cur_sentence)
                i = i[(dot_ind+1):]
                cur_sentence = ""
            cur_sentence = i + " "
        elif i[-1] == ".":
            cur_sentence += i
            sentences_list.append(cur_sentence)
            cur_sentence = ""
        else:
            cur_sentence += i
            cur_sentence += " "
    return sentences_list

# Функция для вывода наиболее часто встечающихся слов в каждом предложении
# Слово состоит из 3 и более букв
def freq_occur_word(ls, text):  #ls - список предложений
    forbidden_words = [".", ",", " ", "(", ")", " ",
                       "1", "2", "3", "4", "5", "6",
                       "7", "8", "9", "0", "+", "-"]
    freq_occur_words = []
    for i, s in enumerate(ls):
        s = s.replace(".", "")
        s = s.replace(",", "")
        s = s.strip()
        words = s.split(" ")
        words_count = {}
        wrong_word = False
        for j in range(len(words)):
            wrong_word = False
            for fw in forbidden_words:
                if fw in words[j] or words[j]=="":
                    wrong_word = True
                    break
            if wrong_word:
                continue
            if not(words[j] in list(words_count.keys())):
                words_count[words[j]] = 1
            else:
                words_count[words[j]] += 1
        if len(words_count.values()) == 0:
            print(f"В {i+1}-м предложении слово ничего не было удалено")
            freq_occur_words.append("!!!")
            continue
        max_count = max(words_count.values())
        for n in list(words_count.keys()):
            if words_count[n] == max_count:
                print(f"В {i+1}-м предложении слово '{n}' {max_count} раз")
                freq_occur_words.append(n)
                break
    return freq_occur_words

# Выравнивание строк
def alignment(ls, key):
    max_len = 0
    sum_len = 0
    for ind, i in enumerate(ls):
        ls[ind] = " ".join((ls[ind].strip()).split())
        if len(ls[ind]) > max_len:
            max_len = len(ls[ind])
        sum_len += len(ls[ind])
    print(f"-"*(max_len+2))
    if key != "width":  # Выравнять по правому или левому краю
        for ind, s in enumerate(ls):
            if key == "left":
                s = s.ljust(max_len, " ")
                print(f"|"+f"{s}"+f"|")
                ls[ind] = s
            elif key == "right":
                s = s.rjust(max_len, " ")
                print(f"|"+f"{s}"+f"|")
                ls[ind] = s
    else:  # Выравнять по ширине
        add_string = ""
        for ind, s in enumerate(ls):
            if len(s) < max_len:
                spaces = s.count(" ")
                ex_spaces = max_len - len(s)
                words = s.split(" ")
                if len(words) == 1:
                    print(f"|"+f"{s:^{max_len}}"+f"|")
                    continue
                # Количество пробелов между словами можно сделать одинаковым
                if ex_spaces % spaces == 0:
                    s = ""
                    for i_i, i in enumerate(words):
                        if i_i + 1 < len(words):
                            s = s + i + " "*(ex_spaces//spaces+1)
                        else:
                            s = s + i
                else:
                    s = ""
                    i = ex_spaces
                    word_num = 0
                    while word_num < len(words):
                        if i > (ex_spaces//spaces) and word_num + 1 < len(words):
                            s = s + words[word_num] + " "*(ex_spaces//spaces+1)
                            i -= ex_spaces//spaces
                        else:
                            s = s + " "*i + words[word_num]
                            i = 0
                        word_num += 1
            ls[ind] = s
            print(f"|"+f"{s}"+f"|")
    print(f"-"*(max_len+2))

# Функция для удаления определенного слова
# В функции реализовано несколько типов удаления
# 1 - Удаление слова из всего текста
# 2 - Замена слова на другое во всем тексте
# 3 - Удаление слова в определенном предложении (все вхождения)
def deleteword(ls, replace=False, word_found=None, sent=None):
    forbidden_words = [".", ",", " ", "(", ")", " ",
                       "1", "2", "3", "4", "5", "6",
                       "7", "8", "9", "0", "+"]
    punctuation = [".", ",", " "]
    if word_found != None:  # Заранее знаем удаляемое слово
        word = word_found
        word = word.strip()
    elif replace:  # Если слово необходимо заменить на другое
        ch = True
        while ch:
            word = input("\nВведите слово, которое требуется заменить (все вхождения)\nв тексте: ")
            word = word.strip()
            check = lambda x: x in word
            for i in forbidden_words:
                if check(i) or word.isdigit() or word == "":
                    print("Вы ввели не слово!")
                    break
            else:
                ch = False
                break
        ch = True
        while ch:
            replace_word = input("\nВведите новое слово, (слово, которое будет в измененном тексте): ")
            replace_word = replace_word.strip()
            check = lambda x: x in replace_word
            for i in forbidden_words:
                if check(i) or replace_word.isdigit() or replace_word == "":
                    print("Вы ввели не слово!")
                    break
            else:
                ch = False
                break
    elif replace == False:  # Обычное удаление слова
        ch = True
        while ch:
            word = input("\nВведите слово, которое требуется удалить (все вхождения)\nиз текста: ")
            word = word.strip()
            check = lambda x: x in word
            for i in forbidden_words:
                if check(i) or word.isdigit() or word == "":
                    print("Вы ввели не слово!")
                    break
            else:
                ch = False
                break
    end_ind = None
    sent_num = 0
    for ind, s in enumerate(ls):
        end_ind = None
        del_words_indexes = []
        for i in range(len(s)):
            if s[i] == ".":
                sent_num += 1
            if s[i] == word[0] and end_ind == None:  # Нашли первую букву удаляемого слова
                start_ind = i
                end_ind = i
                if len(word) != 1:
                    continue
            if end_ind != None:
                #print(s, len(s), word, i, i-start_ind)
                if end_ind-start_ind+1 == len(word):  # Нашли полное слово
                    end_ind = None
                    #print(s[i], s[start_ind:start_ind+len(s)], "-", s[start_ind-1], s[start_ind-1] not in punctuation, word)
                    if ((i+1==len(s) or s[i+1] not in punctuation) or (start_ind == 0 or s[start_ind-1] not in punctuation)) or (word_found != None and sent_num != sent):
                        continue
                    del_words_indexes.append(start_ind)
                    continue
                elif s[i] == word[i-start_ind]:  # Нашли следующую букву удаляемого слова
                    end_ind += 1
                    if end_ind-start_ind+1 == len(word) and i+1 == len(s):  # Нашли полное слово
                        end_ind = None
                        del_words_indexes.append(start_ind)
                elif s[i] != word[i-start_ind] and end_ind-start_ind+1 < len(word):  # Слово прервалось - не нашли удаляемого слова
                    end_ind = None
                    continue 
                if end_ind != None and end_ind-start_ind+1 == len(word):  # Нашли полное слово
                    end_ind = None
                    #2print(s[i], s[i+1] not in punctuation, "-", s[start_ind-1], s[start_ind-1] not in punctuation, word)
                    if word_found != None:
                        if ((i+1==len(s) or s[i+1] not in punctuation) and (start_ind == 0 or s[start_ind-1] not in punctuation)) or (word_found != None and sent_num != sent):
                            continue
                        del_words_indexes.append(start_ind)
                        continue
                    else:
                        if ((i+1==len(s) or s[i+1] not in punctuation) or (start_ind == 0 or s[start_ind-1] not in punctuation)):
                            continue
                        del_words_indexes.append(start_ind)
                        continue
        if not(replace):  # Если заменяем слово
            for i in range(len(del_words_indexes)-1, -1, -1):
                s = s[:del_words_indexes[i]] + s[(del_words_indexes[i]+len(word)):]
            ls[ind] = s
        else:  # Если просто удаляем слово
            for i in range(len(del_words_indexes)-1, -1, -1):
                s = s[:del_words_indexes[i]] + replace_word + s[(del_words_indexes[i]+len(word)):]
            ls[ind] = s            
    return ls
       
# Функция для вычисления математических операций (+ и -) в тексте                
def mathoperations(ls):
    for ind, s in enumerate(ls):
        mathop_indexes = []
        mathop_ind = False
        for i in range(len(s)):
            #if s[i] == " ":
                #if mathop_ind:
                    #mathop_indexes[-1][2] += 1
                #continue
            if s[i].isdigit():
                if mathop_ind:
                    mathop_indexes[-1][0] += s[i]
                    mathop_indexes[-1][2] += 1
                else:
                    mathop_indexes.append([s[i], i, 1])
                    mathop_ind = True
            elif s[i] in "+-" and mathop_ind:
                mathop_indexes[-1][0] += s[i]
                mathop_indexes[-1][2] += 1
            else:
                if len(mathop_indexes) > 0:
                    if ("+" in mathop_indexes[-1][0] or "-" in mathop_indexes[-1][0]) \
                       and mathop_indexes[-1][0][-1].isdigit():
                        pass
                    else:
                        mathop_indexes.pop()
                mathop_ind = False
        # Заменяем все операции на их результаты
        for i in range(len(mathop_indexes)-1, -1, -1):
            math_str = mathop_indexes[i][0]
            result = 0
            for j in range(len(math_str)):
                if mathop_indexes[i][0][j] == "+":
                    result += int(math_str[:j])
                    math_str = " "*(j+1) + math_str[j+1:]
                elif mathop_indexes[i][0][j] == "-" and j != 0:
                    result += int(math_str[:j])
                    math_str = " "*(j) + math_str[j:]
            result += int(math_str)
            # Замена самой строчки
            s = s[:mathop_indexes[i][1]] + str(result) + s[(mathop_indexes[i][1]+mathop_indexes[i][2]):]
        ls[ind] = s  
    return ls
    

# Cам текст
text = ["Во Франции круассаны появились в 1770 году,", 
        "когда туда из Вены переехала Мария—Аунтуанетта. Во второй", 
        "половине 19-го века круассан уже упоминается как непременная",
"составляющая завтрака. Нынешние круассаны круассаны делают во множестве видов. Начиная", 
"от классических, из слоеного теста, которые обычно включены в континентальный завтрак в отелях, до более",
"сложных комбинаций и круассанов c начинками. Самыми",
"популярными являются круассаны с шоколадной начинкой, а также с сыром и ветчиной. Круассаны",
"делают из разного вида слоеного теста,",
"добавляя внутрь заварной крем или посыпая миндальной стружкой. К пустым",
"круассанам обычно подают фруктовый густой джем. И, конечно же, кофе. Кста 2 плюс 2 равно 1+1-1+3."]

# Вывод меню
while True:
    print(f"\n\nМеню действий с текстом")
    print(f"Доступные команды:")
    print(f"1 - Выравнять текст по левому краю и вывести")
    print(f"2 - Выравнять текст по правому краю и вывести")
    print(f"3 - Выравнять текст по ширине и вывести")
    print(f"4 - Удалить слово из текста")
    print(f"5 - Заменить слово из текста")
    print(f"6 - Посчитать математичсекие выражения (+ и -)")
    print(f"7 - Вывести и удалить наиболее часто встречающееся слово в каждом предложении.")
    print(f"8 - Завершить программу")
    try:
        n = int(input("Введите номер команды: "))
        
    except Exception:
        print("Произошла ошибка ввода данных. Вы точно ввели число?")
    if n <= 0 or n >= 9:
            print("Вы ввели несуществующий номер команды!")
    elif n == 1:
        alignment(text, key="left")
    elif n == 2:
        alignment(text, key="right")
    elif n == 3:
        alignment(text, key="width")
    elif n == 4:
        text = deleteword(text)
    elif n == 5:
        text = deleteword(text, True) 
    elif n == 6:
        text = mathoperations(text)
    elif n == 7:
        print("\nПрограмма удалила:")
        sent = make_sentences_list(text)
        words_list = freq_occur_word(sent, text)
        for i in range(len(words_list)):
            text = deleteword(text, False, words_list[i], i) 
    elif n == 8:
        break
