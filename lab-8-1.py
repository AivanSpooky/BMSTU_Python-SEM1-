"""
������� ���� ��7-12� ��������� �8 "�������. ����� 1"
1. ����� ������, ������� ���������� ������� ��������������.
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

# ������ ������, ���������� ���������� ������� ��������������
max_average = -1  # ������������ �������
ind_max_average = 0  # ������ ������, ���������� ������������ �������
for i in range(len(matrix)):
    summ = 0  # ��������� �������� ������
    for elem in matrix[i]:
        summ += elem
    if summ/n > max_average:  # ����� ����� ���������� �������?
        max_average = summ/n
        ind_max_average = i

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
# ����� ������, ���������� ���������� ������� ��������������
print(f"\n{ind_max_average+1}-�� ������ �������� ���������� ������� �������������� ���������, ������ {max_average:8g}")