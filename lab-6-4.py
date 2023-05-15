# Смирнов Иван ИУ7-12Б ЛабРабота №6 Списки Часть 1
# 4. Найти наиболее длинную непрерывную последовательность целых чисел,
# в которой все, начиная с 3-го, являются произведением двух предыдущих.

# Ввод данных списка
while True:
    n = int(input("Введите размер списка: "))
    if n <= 0:
        print("Введите положительную длинну списка!")
    else:
        break
a = [0] * n
for i in range(n):
    a[i] = int(input(f"Введите целый {i+1}-ый элемент: "))

# Находим последовательность
sequence = []
cur_seq = []  # Текущая последовательность
i = 0  # Текущий элемент
while i < n:
    if len(cur_seq) < 2:  # Если в тек. посл. меньше 2 элем. то добавляем
        cur_seq.append(a[i])
        i += 1
        continue
    elif a[i] == a[i-1]*a[i-2]:  # Если тек. элем. равен произв. двух пред.
        cur_seq.append(a[i])  # Добавляем
        i += 1
    else:
        if len(sequence) < len(cur_seq) and len(cur_seq) > 2:  # Если пол. посл. меньше по длинне, чем текущая
            sequence = cur_seq.copy()
        cur_seq = []
        i -= 1
        continue
if len(sequence) < len(cur_seq) and len(cur_seq) > 2:
    sequence = cur_seq.copy()
    cur_seq = []

# Выводим полученную последовательность
if len(sequence) < 3:
    print("Последовательность найти не удалось")
else:
    print("Полученная последовательность чисел (через пробел):")
    print(*sequence)
    print(f"Длинна последовательности = {len(sequence)}")