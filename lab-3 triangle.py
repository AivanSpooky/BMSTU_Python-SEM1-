# ������� ��7-12� ���. ������ �3 - �����������

# ���� ��������� ����� ������������
x_a = int(input("������� ���������� x ����� A: "))
y_a = int(input("������� ���������� � ����� A: "))
x_b = int(input("������� ���������� x ����� B: "))
y_b = int(input("������� ���������� � ����� B: "))
x_c = int(input("������� ���������� x ����� C: "))
y_c = int(input("������� ���������� � ����� C: "))

# ������� ������� AB BC AC �� �����������
ab = ((x_a - x_b)**2+(y_a - y_b)**2)**0.5
bc = ((x_b - x_c)**2+(y_b - y_c)**2)**0.5
ac = ((x_a - x_c)**2+(y_a - y_c)**2)**0.5
print(f"\n������� ������������: AB={ab:.5f} BC={bc:.5f} AC={ac:.5f}")

# ������� ����� �����������, ����������� �� ����������� ����
max_side = max(ab, bc, ac)
if max_side == ab:   # ���� � - ����������?
    bisector = (bc*ac*(bc+ac+ab)*(bc+ac-ab))**0.5/(bc+ac)
elif max_side == bc:   # ���� A - ����������?
    bisector = (ab*ac*(ab+ac+bc)*(ab+ac-bc))**0.5/(ab+ac)
else:   # ���� B - ����������
    bisector = (ab*bc*(ab+bc+ac)*(ab+bc-ac))**0.5/(ab+bc)
print(f"����� �����������, ����������� �� ����������� ���� ����� {bisector:.5f}")

# ����������, �������� �� ����������� ������������
if ab**2>(bc**2+ac**2) or bc**2>(ab**2+ac**2) or ac**2>(ab**2+bc**2):
    print(f"����������� �������� ������������")
else:
    print(f"����������� �� ������������")
    
# ���� ��������� ����� ����� K
x_k = int(input("\n������� ���������� x ����� ����� K: "))
y_k = int(input("������� ���������� y ����� ����� K: "))

# ����������, ��� ��������� ����� ������������ ������������
cond1 = (x_a - x_k)*(y_b - y_a) - (x_b - x_a)*(y_a - y_k) # ������������ ab
cond2 = (x_b - x_k)*(y_c - y_b) - (x_c - x_b)*(y_b - y_k) # ������������ bc
cond3 = (x_c - x_k)*(y_a - y_c) - (x_a - x_c)*(y_c - y_k) # ������������ ac
# print(cond1, cond2, cond3)
if (cond1<0 and cond2<0 and cond3<0) or (cond1>0 and cond2>0 and cond3>0):
    print(f"\n����� ����� ������ ������������")
    # ������� ������� AK BK CK
    ak = ((x_a - x_k)**2+(y_a - y_k)**2)**0.5
    bk = ((x_b - x_k)**2+(y_b - y_k)**2)**0.5
    ck = ((x_k - x_c)**2+(y_k - y_c)**2)**0.5
    
    # ������� ������������� ���������� ������������� ABK, BCK, ACK
    p_abk = (ab+ak+bk)/2
    p_bck = (bc+bk+ck)/2
    p_ack = (ac+ak+ck)/2
    
    # ������� ������ ������������� ABK, BCK, ACK ����������� �� K (����������)
    height_to_ab = 2/ab*(p_abk*(p_abk-ab)*(p_abk-ak)*(p_abk-bk))**0.5
    height_to_bc = 2/bc*(p_bck*(p_bck-bc)*(p_bck-bk)*(p_bck-ck))**0.5
    height_to_ac = 2/ac*(p_ack*(p_ack-ac)*(p_ack-ak)*(p_ack-ck))**0.5
    distance = min(height_to_ab, height_to_bc, height_to_ac) # ������� �� �����
    print(f"���������� �� ����� K �� ��������� ������� ����� {distance:.5f}")
    
elif cond1==0 or cond2==0 or cond3==0:
    print(f"\n����� ����� �� ������� ������������")
    print(f"���������� �� ����� �� ��������� ������� ����� 0")
else:
    print(f"\n����� ����� ��� ������������")