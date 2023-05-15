"""
Смирнов Иван ИУ7-12Б Лабработа-13 Защита
Дан текстовый файл. Нужно в другой текстовый файл переписать
строки в обратном порядке. Файл целиком хранить нельзя,
только построчно.
"""

import os

# Исходный файл input.txt
#try:

with open("input.txt", "r", encoding="cp1251") as f:
    with open("output.txt", "w+", encoding="cp1251") as of:
        n = 0
        line = f.readline()
        while line != "":
            n += 1
            line = f.readline()
        f.seek(0)
        while n > 0:
            for i in range(n):
                line = f.readline()
            of.write(line)
            f.seek(0)
            n -= 1

            
#except Exception:
   # print("Файл нельзя открыть! (Возможно он был удален)")

