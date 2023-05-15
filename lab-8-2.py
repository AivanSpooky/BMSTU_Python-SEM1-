"""
������� ���� ��7-12� ��������� �8 "�������. ����� 1"
2. ����������� ������� ������ � ���������� � ���������� �����������
������������� ���������.
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

# ������ ������, ���������� ���������� � ���������� ���������� �������������
max_neg = None  # ������������ ���������� �������������
ind_max_neg = 0  # ������ ������, ���������� ������������ ���������� �������������
min_neg = None  # ������������ ���������� �������������
ind_min_neg = 0  # ������ ������, ���������� ������������ ���������� �������������
for i in range(len(matrix)):
    neg_count = 0  # ���������� ������������� � ������
    for elem in matrix[i]:
        if elem < 0:  # ����� ������������� - ��������� � �������
            neg_count += 1
    if max_neg is None or neg_count > max_neg:  # ����� ����� ����. ���-�� �������������
        max_neg = neg_count
        ind_max_neg = i
    if min_neg is None or neg_count < min_neg:  # ����� ����� ����. ���-�� �������������
        min_neg = neg_count
        ind_min_neg = i
# �������� ������ ������ �������
matrix[ind_max_neg], matrix[ind_min_neg] = matrix[ind_min_neg], matrix[ind_max_neg]

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