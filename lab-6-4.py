# ������� ���� ��7-12� ��������� �6 ������ ����� 1
# 4. ����� �������� ������� ����������� ������������������ ����� �����,
# � ������� ���, ������� � 3-��, �������� ������������� ���� ����������.

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

# ������� ������������������
sequence = []
cur_seq = []  # ������� ������������������
i = 0  # ������� �������
while i < n:
    if len(cur_seq) < 2:  # ���� � ���. ����. ������ 2 ����. �� ���������
        cur_seq.append(a[i])
        i += 1
        continue
    elif a[i] == a[i-1]*a[i-2]:  # ���� ���. ����. ����� ������. ���� ����.
        cur_seq.append(a[i])  # ���������
        i += 1
    else:
        if len(sequence) < len(cur_seq) and len(cur_seq) > 2:  # ���� ���. ����. ������ �� ������, ��� �������
            sequence = cur_seq.copy()
        cur_seq = []
        i -= 1
        continue
if len(sequence) < len(cur_seq) and len(cur_seq) > 2:
    sequence = cur_seq.copy()
    cur_seq = []

# ������� ���������� ������������������
if len(sequence) < 3:
    print("������������������ ����� �� �������")
else:
    print("���������� ������������������ ����� (����� ������):")
    print(*sequence)
    print(f"������ ������������������ = {len(sequence)}")