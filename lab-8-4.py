"""
������� ���� ��7-12� ��������� �8 "�������. ����� 1"
4. ����������� ������� ������� � ������������ � ����������� ������
���������.
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

# ������ ������� � ������������ � ����������� ������ ���������
max_sum = None  # ����. ����� ��������� �������
ind_max_sum = 0  # ������ ������� � ����. ������
min_sum = None  # ���. ����� ��������� �������
ind_min_sum = 0  # ������ ������� � ���. ������
for i in range(m):
    summ = 0
    for line in matrix:
        summ += line[i]
    if max_sum is None or summ > max_sum:
        max_sum = summ
        ind_max_sum = i
    if min_sum is None or summ < min_sum:
        min_sum = summ
        ind_min_sum = i
# �������� ������ ������� �������
for i in range(n):
    matrix[i][ind_max_sum], matrix[i][ind_min_sum] = matrix[i][ind_min_sum], matrix[i][ind_max_sum]

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