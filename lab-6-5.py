# ������� ���� ��7-12� ��������� �6 ������ ����� 1
# 5. �������� ������� �������� (������ ������� � ����������� �������������)

# ���� ������ ������
while True:
    n = int(input("������� ������ ������: "))
    if n <= 0:
        print("������� ������������� ������ ������!")
    else:
        break
a = [0] * n
for i in range(n):
    a[i] = int(input(f"������� ����� {i+1}-�� �������: "))

# ���� ����������� ������������� �������
if min(a) >= 0:
    print("� ������ ��� ������������� ���������!")
    exit()
else:
    min_below_zero = a.index(min(a))

# ���� ������ ������� �������
first_zero = -1
for i in range(n):
    if a[i] == 0:
        first_zero = i
        break
if first_zero == -1:
    print("� ������ ��� ������� ���������!")
    exit()

# ������ �������� �������
a[first_zero], a[min_below_zero] = a[min_below_zero], a[first_zero]

# ������� ���������� ������
print("\n���������� ������:")
for i, el in enumerate(a):
    print(f"{i+1}-�� �������: {el}")