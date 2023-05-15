"""
������� ���� ��7-12� ���������13 "���� ������ � ��������� �����"
��������� ��������� � ������� ���� ��������� ��������� ��������:
1. ������� ���� ��� ������
2. ���������������� ���� ������ (������� ���� ������������ ���� � ���������
��� ��������)
3. ������� ���������� ���� ������
4. �������� ������ � ����� ���� ������
5. ����� �� ������ ����
6. ����� �� ���� �����
7. ����� �� ���������
"""

# ����������� ������
import os.path

"""
��������� ���� ������ (�������� - ������)
����:
- ��� ������ (3 ��������� ���������� �����)
- ��������� (������)
- ������� (�����)
- �������� �� ������ ����������� (����� 0-1)
"""
db = []

def max_len(file):
    with open(file, "r", encoding="koi8-r") as f:
        max_lens = [3, 0, 0, 0]
        f = f.readlines()
        for i in range(len(f)):
            line = f[i].split(",")
            if len(line) != 4:
                print("���� ������ ������ �����������! (���������� ����� ������� �� 4)")
                return None
            for j in range(4):
                if j > 0:
                    max_lens[j] = max(max_lens[j], len(line[j]))
        return max_lens
            
def printdb(file, len_list, find_cr=None):
    allowed = True
    printed = False
    forb_words = "~!@#$%^&*()_+`1234567890-=,./<>?|{}[]"
    with open(file, "r", encoding="koi8-r") as f:
        line = f.readline()
        while line != "":
            line = line.split(",")
            if len(line) != 4:
                print("���� ������ ������ �����������! (���������� ����� ������� �� 4)")
                return
            for i in range(1, 5):
                el = line[i-1]
                if i == 1:
                    if len(el) != 3:
                        print("���� ������ ������ �����������! (��� ������ ������ �����������)")
                        return
                    for let in el:
                        if let in forb_words:
                            print("���� ������ ������ �����������! (��� ������ ������ �����������)")
                            return
                    line[i-1] = el.upper()
                elif i == 2:
                    for let in el:
                        if let in forb_words:
                            print("���� ������ ������ �����������! (��������� ������ �����������)")
                            return
                elif i == 3:
                    if not(el.isdigit()):
                        print("���� ������ ������ �����������! (��������� ������� �����������)")
                        return
                else:
                    if el[-1] != "\n":
                        print("���� ������ ������ �����������!")
                        print("(��������� ������ � ������ ������ ���� ������� �� ����� ������)")
                        return
                    el = el[:len(el)-1]
                    if not(el.isdigit()):
                        print("���� ������ ������ �����������! (���������� ������� �����������)")
                        return
                    elif int(el) < 0 or int(el) > 1:
                        print("���� ������ ������ �����������! (���������� ������� �����������)")
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
        if not(printed):
            print("������ �� ���� ��������")
            
                    

# ����� ����
f = None
file = None
forb_words = "~!@#$%^&*()_+`1234567890-=,./<>?|{}[]"
while True:
    print(f"\n\n���� �������� � ����� ������ (� ��������� �����)")
    print(f"��������� �������:")
    print(f"1 - ������� ���� ��� ������")
    print(f"2 - ���������������� ���� ������")
    print(f"3 - ������� ���������� ���� ������")
    print(f"4 - �������� ������ � ����� ���� ������")
    print(f"5 - ����� �� ������ ����")
    print(f"6 - ����� �� ���� �����")
    print(f"7 - ��������� ���������")
    try:
        n = int(input("������� ����� �������: "))
    except Exception:
        print("��������� ������ ����� ������. �� ����� ����� �����?")
    if n <= 0 or n >= 8:
        print("�� ����� �������������� ����� �������!")
    elif n == 1:
        while True:
            file = input(f"\n������� �������� ����� ��� ������\n(� ����������� .txt): ")
            if file == "0":
                file = None
                break
            elif not(os.path.exists(file)):
                print("�� ����� �������������� ����!")
                print("���� ������ ��������� � ��������, �������� '0'")
            else:
                break
    elif n == 2:
        while True:
            file = input(f"\n������� ����, � ������� �� ������ ������� ��\n" \
                         "��� ������������ ��� � ������� ����� �� (� ����������� .txt): ")
            with open(file, "w") as f:
                while True:
                    try:
                        line_count = int(input("������� ���������� �������: "))
                        break
                    except Exception:
                        print("��������� ������ ����� ������. �� ����� ����� �����?")
                for i in range(line_count):
                    print(f"\n���������� ������ #{i+1}")
                    line = []
                    while True:
                        code = input("������� ��� ������: ")
                        if len(code) != 3:
                            print("�� ����� ��� ������ �����������!")
                            continue
                        for let in code:
                            if let in forb_words:
                                print("�� ����� ��� ������ �����������!")
                                break
                        else:
                            code = code.upper()
                            line.append(code)
                            break
                    while True:
                        cont = input("������� ���������, �� ������� ��������� ������: ")
                        for let in cont:
                            if let in forb_words:
                                print("�� ����� ��������� �����������!")
                                break
                        else:
                            line.append(cont)
                            break
                    while True:
                        people = input("������� ��������� ������: ")
                        if people.isdigit():
                            line.append(people)
                            break
                        print("�� ����� ��������� �����������!")
                    while True:
                        rep = input("������� �������� �� ������ ����������� (0 - ���, 1 - ��): ")
                        if rep.isdigit():
                            rep = int(rep)
                            if rep < 0 or rep > 1:
                                print("�� ����� �������� �����������!")
                                continue
                            line.append(str(rep))
                            break
                        print("�� ����� ��������� �����������!")
                    f.write(",".join(line))
                    line = []
                    f.write("\n")
            break           
    elif n == 3:
        if file == None:
            print("�� �� ������� ����!")
        else:
            print("\n")
            len_list = max_len(file)
            if len_list != None:
                printdb(file, len_list)
    elif n == 4:
        if file == None:
            print("�� �� ������� ����!")
        else:
            print("\n")
            with open(file, "a") as f:
                line = []
                while True:
                    code = input("������� ��� ������: ")
                    if len(code) != 3:
                        print("�� ����� ��� ������ �����������!")
                        continue
                    for let in code:
                        if let in forb_words:
                            print("�� ����� ��� ������ �����������!")
                            break
                    else:
                        code = code.upper()
                        line.append(code)
                        break
                while True:
                    cont = input("������� ���������, �� ������� ��������� ������: ")
                    for let in cont:
                        if let in forb_words:
                            print("�� ����� ��������� �����������!")
                            break
                    else:
                        line.append(cont)
                        break
                while True:
                    people = input("������� ��������� ������: ")
                    if people.isdigit():
                        line.append(people)
                        break
                    print("�� ����� ��������� �����������!")
                while True:
                    rep = input("������� �������� �� ������ ����������� (0 - ���, 1 - ��): ")
                    if rep.isdigit():
                        rep = int(rep)
                        if rep < 0 or rep > 1:
                            print("�� ����� �������� �����������!")
                            continue
                        line.append(str(rep))
                        break
                    print("�� ����� ��������� �����������!")
                f.write(",".join(line))
                line = []
                f.write("\n")
    elif n == 5:
        if file == None:
            print("�� �� ������� ����!")
        else:
            print()
            while True:
                try:
                    num = int(input("������� ����� ���� (�� �������� ��������� �����): "))
                    if num <= 0 or num >= 5:
                        print("����������, ������� ������������ ����� ����! (�� 1 �� 4)")
                    else:
                        break
                except Exception:
                    print("��������� ������ ����� ������. �� ����� ����� �����?")
            criteria = input("������� �������� ���������� ����, �� �������� ���������� ����� ������: ")
            print()
            len_list = max_len(file)
            if len_list != None:
                printdb(file, len_list, [[num, criteria]])            
    elif n == 6:
        if file == None:
            print("�� �� ������� ����!")
        else:
            print()
            while True:
                try:
                    n1 = int(input("������� ����� 1-��� ���� (�� �������� ��������� �����): "))
                    if n1 <= 0 or n1 >= 5:
                        print("����������, ������� ������������ ����� ����! (�� 1 �� 4)")
                    else:
                        break
                except Exception:
                    print("��������� ������ ����� ������. �� ����� ����� �����?")
            cr1 = input("������� �������� 1-��� ����, �� �������� ���������� ����� ������: ")
            print()
            while True:
                try:
                    n2 = int(input("������� ����� 2-��� ���� (�� �������� ��������� �����): "))
                    if n2 <= 0 or n2 >= 5:
                        print("����������, ������� ������������ ����� ����! (�� 1 �� 4)")
                    elif n2 == n1:
                        print("����������, ������� ������ ����� ����! (�������� �� �������)")
                    else:
                        break
                except Exception:
                    print("��������� ������ ����� ������. �� ����� ����� �����?")
            cr2 = input("������� �������� 2-��� ����, �� �������� ���������� ����� ������: ")
            len_list = max_len(file)
            if len_list != None:
                printdb(file, len_list, [[n1, cr1], [n2, cr2]])
    elif n == 7:
        break