"""
������� ���� ��7-12� ���������10 "���������� ������������ �������� ���������"
��������� ��������� ����������� �������� ��������� �� �������� � ���������
������� ����� ��������� (����� ���������� ��������������� � ����� �������).
"""

# ������������� �������
def greater_func(x):
    return x**5/5+x**4/4-x**3*2/3+x**2/2-5*x

# �������
def function(x):
    return x**4 + x**3 - 2*x**2 + x - 5

# ����� ���������� ���������������
def middle_rectangles(start, end, n):
    global eps
    step = (end-start)/n  # ��� �������� ��� N ���������
    i = start+step  # �������
    mid_rect_summ = 0
    while i - end < eps:
        mid_rect_summ += function((i + i-step)/2)*step
        i += step
    return mid_rect_summ

# ����� �������
def parabola(start, end, n):
    if n % 2 == 1:
        return "-"
    h = (end-start)/(n)
    par_summ = function(start) + function(end)
    for i in range(1, n):
        if i%2 != 0:
            par_summ += 4*function(start + i*h)
        else:
            par_summ += 2*function(start + i*h)
    return par_summ * h / 3

# ���������� �����������
def absolute_error(method):
    global real
    return abs(method - real) if abs(method - real) != 0 else 1e-10

# ������������� �����������
def relative_error(abs_err):
    global real
    return abs(abs_err / real) if real != 0 else "-"


# ���� ������ � ����� ������� ��������������, � ����� N1 � N2 - ����������
# ��������� ������� ��������������.
while True:
    try:
        start = float(input("������� ������ ������� ��������������: "))
        break
    except Exception:
        print("��������� ������ ����� ������. �� ����� ����� �����?")
while True:
    try:
        end = float(input("������� ����� ������� ��������������: "))
        if end <= start:
            print(f"����� ������ ���� ������ ������ ({start})")
        else:
            break
    except Exception:
        print("��������� ������ ����� ������. �� ����� ����� �����?")
while True:
    try:
        n1 = int(input("������� ���������� ��������� ������� �������������� (N1): "))
        if n1 <= 0:
            print("������� ������������� ���������� ���������")
        else:
            break
    except Exception:
        print("��������� ������ ����� ������. �� ����� ����� ����� �����?")
while True:
    try:
        n2 = int(input("������� ���������� ��������� ������� �������������� (N2): "))
        if n2 <= 0:
            print("������� ������������� ���������� ���������")
        else:
            break
    except Exception:
        print("��������� ������ ����� ������. �� ����� ����� ����� �����?")

# ��������� ��������� �������� ��������� ������� ���������� ���������������
eps = 1e-8  # ����������� ��� ��������� ������������ �����
n1_midrect = middle_rectangles(start, end, n1)  # ������� ��� N1 ���������
n2_midrect = middle_rectangles(start, end, n2)  # ������� ��� N2 ���������

# ��������� ��������� �������� ��������� ������� �������
n1_parabola = parabola(start, end, n1)  # ������� ��� N1 ���������
n2_parabola = parabola(start, end, n2)  # ������� ��� N2 ���������

# ����� �������
print("\n\n")
print(f"{'':<32}|{'N1':<16}|{'N2':<16}")
print(f"-"*66)
print(f"{'����� ���������� ���������������':<30}|{n1_midrect:<16.8f}|{n2_midrect:<16.8f}")
print(f"-"*66)
print(f"{'����� �������':<32}|{n1_parabola:<16.8f}|{n2_parabola:<16.8f}")

# ������� ���������� � ������������� ����������� ��� ������� �� �������
real = greater_func(end)-greater_func(start)  # �������� �������� ���������
if real < eps:
    real = 0

# ������� ���������� � ������������� ����������� ��� ������� �� �������
abs_err_1_n1 = absolute_error(n1_midrect)
abs_err_1_n2 = absolute_error(n2_midrect)
abs_err_2_n1 = absolute_error(n1_parabola)
abs_err_2_n2 = absolute_error(n2_parabola)

rel_err_1_n1 = relative_error(abs_err_1_n1)
rel_err_1_n2 = relative_error(abs_err_1_n2)
rel_err_2_n1 = relative_error(abs_err_2_n1)
rel_err_2_n2 =  relative_error(abs_err_2_n2)

# ������� ����������� ��� ��������������� ������� � ���������� ��������
print(f"\n\n����� ���������� ���������������")
if real == 0:
    print(f"��� {n1} ���������:")
    print(f"���. �����������: {abs_err_1_n1:<10.5g} ���. �����������: {rel_err_1_n1:<10.5}")
    print(f"��� {n2} ���������:")
    print(f"���. �����������: {abs_err_1_n2:<10.5g} ���. �����������: {rel_err_1_n2:<10.5}")
    print(f"\n����� �������")
    print(f"��� {n1} ���������:")
    print(f"���. �����������: {abs_err_2_n1:<10.5g} ���. �����������: {rel_err_2_n1:<10.5}")
    print(f"��� {n2} ���������:")
    print(f"���. �����������: {abs_err_2_n2:<10.5g} ���. �����������: {rel_err_2_n2:<10.5}")
else:
    print(f"��� {n1} ���������:")
    print(f"���. �����������: {abs_err_1_n1:<10.5g} ���. �����������: {rel_err_1_n1:<10.5g}")
    print(f"��� {n2} ���������:")
    print(f"���. �����������: {abs_err_1_n2:<10.5g} ���. �����������: {rel_err_1_n2:<10.5g}")
    print(f"\n����� �������")
    print(f"��� {n1} ���������:")
    print(f"���. �����������: {abs_err_2_n1:<10.5g} ���. �����������: {rel_err_2_n1:<10.5g}")
    print(f"��� {n2} ���������:")
    print(f"���. �����������: {abs_err_2_n2:<10.5g} ���. �����������: {rel_err_2_n2:<10.5g}")    

# ������� �������� ������ ����� � ��������� ��� � ���������� accurate_method
# ����� ���. ����. - 1; ����� ������� - 2.
print("\n�������� ������ �����:")
most_accurate = min(abs_err_1_n1, abs_err_1_n2, abs_err_2_n1, abs_err_2_n2)
eps = most_accurate/2
if abs_err_1_n1 - most_accurate < eps:
    print(f"����� ���������� ��������������� ��� {n1} ��������")
    accurate_method = 1
elif abs_err_1_n2 - most_accurate < eps:
    print(f"����� ���������� ��������������� ��� {n2} ��������")
    accurate_method = 1
elif abs_err_2_n1 - most_accurate < eps:
    print(f"����� ������� ��� {n1} ��������")
    accurate_method = 2
else:
    print(f"����� ������� ��� {n2} ��������")
    accurate_method = 2

# ������� ��� �������� �������� ����� ������ ����� ��������� �������� ����� �������
n = 1
current_accuracy = None  # �������� ��� �������� n
next_accuracy = None  # �������� ��� 2*n
if accurate_method == 1:
    while current_accuracy == None or abs(current_accuracy - next_accuracy) > eps:
        current_accuracy, next_accuracy = next_accuracy, parabola(start, end, n)
        n *= 2
else:
    while current_accuracy == None or abs(current_accuracy - next_accuracy) > eps:
        current_accuracy, next_accuracy = next_accuracy, middle_rectangles(start, end, n)
        n *= 2

# ����� ������������ ���������� ��������
print(f"\n��� ���������� ������������ �������� ����� ������ ������� ���������� \
{n} ��������")