"""
������� ���� ��7-12� ��������� �8 "�������. ����� 1"
5. ����� ������������ �������� � ���������� ������� ��� ������� ���������� �
����������� - ��� �������� ����������
"""

# ���� ���������� �������
while True:  # ���-�� ����� �������
    n = int(input("������� ���������� ����� � �������� ���������� �������: "))
    if n <= 0:
        print("������� ������������� ���������� ����� � ��������!")
    else:
        break
matrix = [[0]*n for i in range(n)]
# ������ �������� �������
for i in range(n):
    for j in range(n):
        matrix[i][j] = int(input(f"������� {j+1}-�� ������� {i+1}-�� ������: "))

# ������ ������������ �������� ��� ������� ����������
max_over_main = None  # ����. ������� ��� ������� ����������
for i in range(n):
    for j in range(i+1, n):
        if max_over_main is None or matrix[i][j] > max_over_main:
            max_over_main = matrix[i][j]
# ������ ����������� �������� ��� �������� ����������
min_under_side = None  # ���. ������� ��� �������� ����������
for i in range(n):
    for j in range(n-i, n):
        if min_under_side is None or matrix[i][j] < min_under_side:
            min_under_side = matrix[i][j]

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
# ������� ���������� ��������
print(f"\n{max_over_main} - ������������ ����� ��� ������� ����������")
print(f"{min_under_side} - ����������� ����� ��� �������� ����������")