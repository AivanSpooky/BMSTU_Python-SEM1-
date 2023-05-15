"""
������� ���� ���������12 "������ � �������"
�������� ��������� ��� ���������� ��������� �������� � �������. ������� ����� ��
���������, �� ������ ���� ����� � �������� ������ ��������� � ���� ������ �����
(��� ������ �� ����� ������ ������� ����� ������ ������ ���������� � �����
������). � ������� ���� ������ ���������� ����������� 7 �������� ��� �������:
1 - ��������� ����� �� ������ ����.
2 - ��������� ����� �� ������� ����.
3 - ��������� ����� �� ������.
4 - �������� ���� ��������� ��������� �����.
5 - ������ ������ ����� ������ �� ��� ������.
6 - ���������� �������������� ��������� ��� ������ ������� ������ ������
(+ � -).
7 - ����� (������� �� �����) � ����� ������� �����
�������� ����� ������������� ����� � ������ �����������.
8 - ����� �� ���������
"""

# ������� ��� �������� ����������� �� ������ �����
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

# ������� ��� ������ �������� ����� ������������ ���� � ������ �����������
def freq_occur_word(ls, text):  #ls - ������ �����������
    print()
    freq_occur_words = []
    for i, s in enumerate(ls):
        s = s.replace(".", "")
        s = s.replace(",", "")
        words = s.split(" ")
        words_count = {}
        for j in range(len(words)):
            if len(words[j]) <= 1:
                continue
            if not(words[j] in list(words_count.keys())):
                words_count[words[j]] = 1
            else:
                words_count[words[j]] += 1
        max_count = max(words_count.values())
        for n in list(words_count.keys()):
            if words_count[n] == max_count:
                print(f"� {i+1}-� ����������� ����� '{n}' ����������� {max_count} ���")
                freq_occur_words.append(n)
                break
    return freq_occur_words

# ������������ �����
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

def deleteword(ls, replace=False, word_found=None):
    if word_found != None:
        word = word_found    
    elif replace:
        word = input("\n������� �����, ������� ��������� �������� (��� ���������)\n� ������: ")
        replace_word = input("\n������� ����� �����, (�����, ������� ����� � ���������� ������): ")
    elif replace == False:
        word = input("\n������� �����, ������� ��������� ������� (��� ���������)\n�� ������: ")
    end_ind = None
    for ind, s in enumerate(ls):
        end_ind = None
        del_words_indexes = []
        for i in range(len(s)):
            if s[i] == word[0] and end_ind == None:  # ����� ������ ����� ���������� �����
                start_ind = i
                end_ind = i
                continue
            if end_ind != None:
                if end_ind-start_ind+1 == len(word):  # ����� ������ �����
                    end_ind = None
                    if (s[i] != " " and s[i] != "." and s[i] != ","):
                        continue
                    del_words_indexes.append(start_ind-1)
                elif s[i] == word[i-start_ind]:  # ����� ��������� ����� ���������� �����
                    end_ind += 1
                    if end_ind-start_ind+1 == len(word) and i+1 == len(s):  # ����� ������ �����
                        end_ind = None
                        del_words_indexes.append(start_ind-1)
                elif s[i] != word[i-start_ind] and end_ind-start_ind+1 < len(word):  # ����� ���������� - �� ����� ���������� �����
                    end_ind = None
                    continue
                
        if not(replace):
            for i in range(len(del_words_indexes)-1, -1, -1):
                s = s[:del_words_indexes[i]+1] + s[(del_words_indexes[i]+len(word)+1):]
            ls[ind] = s
        else:
            for i in range(len(del_words_indexes)-1, -1, -1):
                s = s[:del_words_indexes[i]+1] + replace_word + s[(del_words_indexes[i]+len(word)+1):]
            ls[ind] = s            
    return ls

#def fast_deleteword(ls, word_list):
    #for i in range(len(word_list)):
        #for j, s in enumerate(ls):
            
                
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
                    if ("+" in mathop_indexes[-1][0] or "-" in mathop_indexes[-1][0]) and mathop_indexes[-1][0][-1].isdigit():
                        pass
                    else:
                        mathop_indexes.pop()
                mathop_ind = False
        for i in range(len(mathop_indexes)-1, -1, -1):
            if "+" in mathop_indexes[i][0]:
                result = sum(list(map(int, mathop_indexes[i][0].split("+"))))
            else:
                result = list(map(int, mathop_indexes[i][0].split("-")))
                result = result[0] - result[-1]
            s = s[:mathop_indexes[i][1]] + str(result) + s[(mathop_indexes[i][1]+mathop_indexes[i][2]):]
        ls[ind] = s  
    return ls
    

# C�� �����
text = ["�� ������� ��������� ��������� � 1770 ����,", "����� ���� �� ���� ��������� �����-�����������. �� ������", "�������� 19-�� ���� �������� ��� ����������� ��� �����������",
"������������ ��������. �������� ��������� ������ �� ��������� �����. �������", "�� ������������, �� �������� �����, ������� ������ �������� � ��������������� ������� � ������, �� �����",
"������� ���������� � ���������� c ���������. ������", "����������� �������� ��������� � ���������� ��������, � ����� � ����� � ��������. ���������", "������ �� ������� ���� �������� �����,",
"�������� ������ �������� ���� ��� ������� ���������� ��������. � ������", "���������� ������ ������ ��������� ������ ����. �, ������� ��, ����. ����, 1 ���� 1 ����� 1+1."]

# ����� ����
while True:
    print(f"\n\n���� �������� � �������")
    print(f"��������� �������:")
    print(f"1 - ��������� ����� �� ������ ����")
    print(f"2 - ��������� ����� �� ������� ����")
    print(f"3 - ��������� ����� �� ������")
    print(f"4 - ������� ����� �� ������")
    print(f"5 - �������� ����� �� ������")
    print(f"6 - ��������� �������������� ��������� (+ � -)")
    print(f"7 - ������� � ������� �������� ����� ������������� ����� � ������ �����������.")
    print(f"8 - ��������� ���������")
    try:
        n = int(input("������� ����� �������: "))
        if n <= 0 or n >= 9:
            print("�� ����� �������������� ����� �������!")
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
        elif n == 7:
            sent = make_sentences_list(text)
            words_list = freq_occur_word(sent, text)
            #text = fast_deleteword(text, words_list)
            for word in words_list:
                text = deleteword(text, False, word) 
        elif n == 8:
            break
    except Exception:
        print("��������� ������ ����� ������. �� ����� ����� �����?")