"""
Смирнов Иван ИУ7-12Б
"""

# Нахождение n
def findN(file):
    with open(file, "r") as f:
        n = 0
        line = f.readline()
        while line != "":
            n += 1
            line = f.readline()
    return n

# Перевод числа в римскую с/c + нахождение максимальной длины числа
def romeNums(n, mx):
    ls = {"M":1000, "CM":900, "D":500, "CD":400, "C":100, "XC":90, "L":50, "XL":40, "X":10, "IX":9, "V":5, "IV":4, "I":1}
    s = ""
    for w in ls:
        while n >= int(ls[w]):
            s += w
            n -= ls[w]
    mxs = max(mx, len(s))
    return s, mxs


file1 = "in1.txt"
file2 = "in2.txt"

mLen = 0

# 1 часть задания
with open(file1, "r") as f, open("out1.txt", "w") as f1:
    n = findN(file1)
    for i in range(n):
        num = int(f.readline())
        rn, mLen = romeNums(num, mLen)
        if len(rn) < mLen:
            spaces = mLen - len(rn)
            if spaces % 2 == 0:
                rn = " "*(spaces//2) + rn + " "*(spaces//2)
            else:
                rn = " "*(spaces//2) + rn + " "*(spaces - (spaces//2))
        f1.write(rn+"\n")

# 2 часть задания
with open(file2, "r") as f, open("out2.txt", "w") as f2:
    n1 = findN(file2)
    for _ in range(n1):
        nLine = int(f.readline())-1
        with open("out1.txt", "r") as f1:
            for i in range(n):
                line = f1.readline()
                if i == nLine:
                    f2.write(line)