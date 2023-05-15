"""
������� ���� ��7-12� ��������� �8 "�������. ����� 1"
6. ��������� ���������������� ���������� �������.
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

# ��������� ���������������� ���������� �������
for i in range(n):
    for j in range(i, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

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