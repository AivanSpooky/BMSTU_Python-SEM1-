# ������� ���� ��7-12� ��������� �6 ������ ����� 1
# 3. ����� �������� K-�� ���������� � ������.

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

# ������ ������ ����������
while True:
    k = int(input(f"������� ������ ���������� K: "))
    if k <= 0:
        print("������� ������������� K!")
    elif k >= n+1:
        print("�� ����� �������������� K ��� ������� ������!")
    else:
        break

# ������� �������� K-��� ����������
extremums_found = 0
for i in range(1,n):
    if (a[i-1] < a[i] and a[i+1] < a[i] ) or(a[i-1] > a[i] and a[i+1] > a[i]):
        extremums_found += 1
        if extremums_found == k:
            print(f"\n�������� {k}-��� ���������� = {a[i]:8g}")
            break
else:
    print(f"\n� ������ ��� {k}-��� ����������")