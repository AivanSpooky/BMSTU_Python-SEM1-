"""
������� ���� ��7-12� ���������13 ������
� ������� ���������� ������������� ����� � ������������� �������� (��������� ��������)
������� ����� ���� output.txt � ����������������� ��������. ������ �� ��������
������� �������� ��������� (�� �������).
"""

import os

file = input("������� ���� ��� ���������������� �������: ")
try:
    if file == "output.txt":
        print("����������, ������� ������ ��� �����!")
        exit(1)
    f = open(file, "r")
    line = f.readline().strip()
    n = None
    m = 0
    while line != "":
        nums = line.split(" ")
        for i in nums:
            if i == "":
                print("������ ����� ������ (�������� � ����� ������������ ������ �������)")
                exit(1) 
            if not(i.isdigit()):
                print("������ ����� ������ (� ������� ���� �������, ������� �� �������� ����� ������)")
                exit(1)
        if n == None:
            n = len(nums)
        if len(nums) != n:
            print("������ ����� ������ (������� �� �������� ����������)")
            exit(1)
        line = f.readline().strip()
        m += 1
    if n == None:
        print("������ ����� ������ (�������� ���� ������ ��� ������� �� ���������� ��������)")
        exit(1) 
    if m != n:
        print("������ ����� ������ (������� �� �������� ����������)")
        exit(1)
    f.close()
except Exception:
    print("���� �� ������� ������� (�������� ��� �� ���������� ��� ��� ���� �� ��������).")
    exit(1)   
if os.path.exists("output.txt"):
    try:
        os.remove("output.txt")
    except Exception:
        print("��������� ������. (���� output.txt ��� ���������, ������� ���)")
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
print("����������������� ������� �������� � ���� output.txt")
f.close()
f1.close()