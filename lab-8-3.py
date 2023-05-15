"""
������� ���� ��7-12� ��������� �8 "�������. ����� 1"
3. ����� �������, ������� ����������� ������� ����� �������� ����� �������������
� ������������� ���������
"""

# ���� �������
while True:  # ���-�� ����� �������
    m = int(input("������� ���������� ����� �������: "))
    if m <= 0:
        print("������� ������������� ���������� �����!")
    else:
        break
while True:  # ���-�� �������� �������
    n = int(input("������� ���������� �������� �������: "))
    if n <= 0:
        print("������� ������������� ���������� ��������!")
    else:
        break
matrix = [[0]*n for i in range(m)]
# ������ �������� �������
for i in range(m):
    for j in range(n):
        matrix[i][j] = int(input(f"������� {j+1}-�� ������� {i+1}-�� ������: "))

# ������ �������, ������� ����������� ������� ����� �������� ����� �������������
# � ������������� ��������� 
min_dif = None
ind_min_dif = 0
for i in range(m):
    dif = 0
    for line in matrix:
        dif -= line[i]
    if min_dif is None or dif < min_dif:
        min_dif = dif
        ind_min_dif = i

# ���������� ������������ ����� �������� ������� ��� � ���������������� ������
max_len = len(str(matrix[0][0]))  # ����. ����� �������� �������
for line in matrix:
    max_len = max(max_len, len(str(max(line))), len(str(min(line))))
# ������� �������
print("\n���������� �������:")
for line in matrix:
    print("", end="|")
    for elem in line:
        print(str(elem).ljust(max_len + max_len//2+1," "), end="|")
    print("")
# ������� ���������� �������
print(f"{ind_min_dif+1}-�� ������� ����� ����������� ������� ����� �������� ����� \
������������� � ������������� ���������, ������ {min_dif}")