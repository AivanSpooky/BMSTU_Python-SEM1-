"""
Смирнов Иван Лабработа№12 "Работа с текстом"
"""

# Функция для нахождения длины максимальной строки
def max_letter_count(ls):
    max_count = 0
    cur_count = 0
    for i in ls:
        cur_count += len(i)
        if i[-1] == "." or i[-1] == "!" or i[-1] == "?":
            if cur_count > max_count:
                max_count = cur_count
            cur_count = 0
        else:
            cur_count += 1
    return max_count

# Функция для создания предложений из списка строк
def make_sentences_list(ls):
    sentences_list = []
    cur_sentence = ""
    for i in ls:
        #if "\n" in i:
            #new_i = ""
            #for j in range(len(i)):
                #new_i += i[j] if i[j] != "\n" else ""
            #i = new_i
        cur_sentence += i
        if i[-1] == "." or i[-1] == "!" or i[-1] == "?":
            sentences_list.append(cur_sentence)
            cur_sentence = ""
        else:
            cur_sentence += " "
    return sentences_list

# Выравнивание строк
def alignment(ls, key):
    max_len = 0
    sum_len = 0
    for i in ls:
        if len(i) > max_len:
            max_len = len(i)
        sum_len += len(i)
    
    if key != "center":
        print(f"-"*(max_len+2))
        for i in ls:
            if key == "left":
                print(f"|"+f"{i:<{max_len}}"+f"|")
            elif key == "right":
                print(f"|"+f"{i:>{max_len}}"+f"|")
        print(f"-"*(max_len+2))
    else:
        string_len = sum_len//len(ls) + sum_len//(2*len(ls))
        print(f"-"*(string_len+4))
        add_string = ""
        for ind, s in enumerate(ls):
            while True:
                if add_string != "":
                    s = add_string + " " + s
                #print(s)
                if len(s) >= string_len or s[-1] == ".":
                    print(f"| "+f"{s[:string_len]:<{string_len}}"+f" |")
                    if len(s) == string_len:
                        break
                    add_string = s[string_len:]
                    if s[-1] == "." and ind == len(ls)-1:
                        print(f"| "+f"{add_string:<{string_len}}"+f" |")
                    break
                else:
                    add_string = s
                    break
        print(f"-"*(string_len+4))

def deleteword(ls, replace=False):
    if replace:
        word = input("\nВведите слово, которое требуется заменить (все вхождения)\nв тексте: ")
        replace_word = input("\nВведите новое слово, (слово, которое будет в измененном тексте): ")
    else:
        word = input("\nВведите слово, которое требуется удалить (все вхождения)\nиз текста: ")
    end_ind = None
    for ind, s in enumerate(ls):
        end_ind = None
        del_words_indexes = []
        for i in range(len(s)):
            if s[i] == word[0] and end_ind == None:  # Нашли первую букву удаляемого слова
                start_ind = i
                end_ind = i
                continue
            if end_ind != None:
                if s[i] == word[i-start_ind]:  # Нашли следующую букву удаляемого слова
                    end_ind += 1
                elif s[i] != word[i-start_ind] and end_ind-start_ind+1 < len(word):  # Слово прервалось - не нашли удаляемого слова
                    end_ind = None
                    continue
                if end_ind-start_ind+1 == len(word):  # Нашли полное слово
                    end_ind = None
                    if (i+1) >= len(s):
                        pass
                    elif (s[i+1] != " " and s[i+1] != "." and s[i+1] != ","):
                        continue
                    del_words_indexes.append(start_ind-1)
        if not(replace):
            for i in range(len(del_words_indexes)-1, -1, -1):
                s = s[:del_words_indexes[i]] + s[(del_words_indexes[i]+len(word)+1):]
            ls[ind] = s
        else:
            for i in range(len(del_words_indexes)-1, -1, -1):
                s = s[:del_words_indexes[i]+1] + replace_word + s[(del_words_indexes[i]+len(word)+1):]
            ls[ind] = s            
    return ls
                
def mathoperations(ls):
    for ind, s in enumerate(ls):
        mathop_indexes = []
        mathop_ind = False
        for i in range(len(s)):
            if s[i] == " ":
                if mathop_ind:
                    mathop_indexes[-1][2] += 1
                continue
            elif s[i].isdigit():
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
                mathop_ind = False
        for i in range(len(mathop_indexes)-1, -1, -1):
            if "+" in mathop_indexes[i][0]:
                result = sum(list(map(int, mathop_indexes[i][0].split("+"))))
            else:
                result = sum(list(map(int, mathop_indexes[i][0].split("-"))))
            s = s[:mathop_indexes[i][1]+1] + result + s[(mathop_indexes[i][1]+mathop_indexes[i][2]):]
        ls[ind] = s            
    return ls
    

# Cам текст
text = ["Во Франции круассаны появились в 17+70 году,", "когда туда из Вены переехала Мария-Аунтуанетта. Во второй", "половине 19-го века круассан уже упоминается как непременная",
"составляющая завтрака. Нынешние круассаны делают во множестве видов. Начиная", "от классических, из слоеного теста, которые обычно включены в континентальный завтрак в отелях, до более",
"сложных комбинаций и круассанов c начинками. Самыми", "популярными являются круассаны с шоколадной начинкой, а также с сыром и ветчиной. Круассаны", "делают из разного вида слоеного теста,",
"добавляя внутрь заварной крем или посыпая миндальной стружкой. К пустым", "круассанам обычно подают фруктовый густой джем. И, конечно же, кофе."]

# Вывод меню
while True:
    print(f"\n\nМеню действий с текстом")
    print(f"Доступные команды:")
    print(f"1 - Выравнять текст по левому краю")
    print(f"2 - Выравнять текст по правому краю")
    print(f"3 - Выравнять текст по центру")
    print(f"4 - Удалить слово из текста")
    print(f"5 - Заменить слово из текста")
    print(f"6 - Посчитать математичсекие выражения (+ и -)")
    print(f"8 - Завершить программу")
    try:
        n = int(input("Введите номер команды: "))
        if n <= 0 or n >= 9:
            print("Вы ввели несуществующий номер команды!")
        elif n == 1:
            alignment(text, key="left")
        elif n == 2:
            alignment(text, key="right")
        elif n == 3:
            alignment(text, key="center")
        elif n == 4:
            text = deleteword(text)
        elif n == 5:
            text = deleteword(text, True) 
        elif n == 6:
            text = mathoperations(text)
        elif n == 8:
            break
    except Exception:
        print("Произошла ошибка ввода данных. Вы точно ввели число?")