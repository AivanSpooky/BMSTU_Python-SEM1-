# ������� ���� ��7-12� ��������� �6 ������ ����� 1
# 2a. ������� ������� � �������� �������� � ��������������
# ����� ������� Python.

# ���� ������ ������
while True:
    n = int(input("������� ������ ������: "))
    if n <= 0:
        print("������� ������������� ������ ������!")
    else:
        break
a = [0] * n
for i in range(n):
    a[i] = float(input(f"������� {i+1}-�� �������: "))

# ������ ������ ��������, ������� ���������� �������
while True:
    ind_elem = int(input(f"������� ������ ��������, ������� ����� �������: "))
    if ind_elem <= 0:
        print("������� ������������� ����� ��������!")
    elif ind_elem >= n+1:
        print("�� ����� �������������� ����� �������� ��� ������� ������!")
    else:
        break

# ������� �� ������ ��������� ����� ��������
a.pop(ind_elem-1)

# ������� ���������� ������
print("\n���������� ������:")
for i, el in enumerate(a):
    print(f"{i+1}-�� �������: {el}")