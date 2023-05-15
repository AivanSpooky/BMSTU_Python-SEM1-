sp = [5, 3, 4, 3, 2, 1, 1]

def BubleSort(ls):
    for i in range(len(ls)):
        for j in range(len(ls)-i-1):
            if ls[j+1] < ls[j]:
                ls[j], ls[j+1] = ls[j+1], ls[j]
    return ls

def shakersort(ls): 
    left = 0
    right = len(ls) - 1
    while left < right: 
        r_new = left
        for i in range(left,right):
            if ls[i] > ls[i+1]:
                ls[i], ls[i + 1] = ls[i + 1], ls[i] 
                r_new = i
        right = r_new

        l_new = right
        for i in range(right - 1, left - 1, -1):
            if (ls[i] > ls[i+1]):
                ls[i], ls[i + 1] = ls[i + 1], ls[i] 
                l_new = i
        left = l_new
    return ls

def selection_sort(ls):
    for i in range(len(ls)):
        min_ind = i
        for j in range(i + 1,len(ls)):
            if ls[j] < ls[min_ind]: 
                min_ind = j
        ls[i],ls[min_ind] = ls[min_ind],ls[i]
    return ls

def insertion_sort(ls):
    for i in range(1, len(ls)):
        temp = ls[i]
        j = i - 1
        while (j >= 0 and temp < ls[j]):
            ls[j + 1] = ls[j]
            j = j - 1
        ls[j + 1] = temp
    return ls

def insertion_sort_with_bin_search(ls): 
    for i in range(1, len(ls)):
        temp = ls[i]
        left, right = 0, i
        while left < right:
            mid = (left + right)//2
            if temp < ls[mid]: 
                right = mid 
            else: 
                left = mid + 1
        j = i
        while (j > left and j > 0):
            ls[j] = ls[j-1] 
            j = j - 1
        ls[left] = temp
    return ls

def insertion_sort_with_barier(ls):
    ls = ls + [0]
    for i in range(1, len(ls)):
        print(ls)
        if ls[i - 1] > ls[i]:
            ls[-1] = ls[i]
            j = i - 1
            while ls[j] > ls[-1]:
                ls[j + 1] = ls[j]
                j = j - 1
            ls[j + 1] = ls[-1]
    return ls[:-1]

def shell(mas):
  step = len(mas) // 2
  while step:
    for i, el in enumerate(mas):
      while i >= step and el < mas[i - step]:
        print(mas)
        mas[i] = mas[i - step]
        i -= step
      mas[i] = el
    step = 1 if step == 2 else int(step * 5 // 11)
  return mas

def quicksort(arr, start = 0, end = None):
    if len(arr) == 0:
        return arr
    pind = 0
    pivot = arr[pind]
    left = [x for x in arr if x < pivot] 
    midle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot] 
    return quicksort(left, 0, len(left)) + midle + quicksort(right, 0, len(right))





print("Изначальный список: ")
print(sp)
# print("Сортировка Пузырьком: ")
# print(BubleSort(sp))
# print("Сортировка шейкер: ")
# print(shakersort(sp))
# print("Сортировка выбором: ")
# print(selection_sort(sp))
# print("Сортировка вставками: ")
# print(insertion_sort(sp))
# print("Сортировка вставками с бин поиском: ")
# print(insertion_sort_with_bin_search(sp))
# print("Сортировка вставками с барьером: ")
# print(insertion_sort_with_barier(sp))
print("Сортировка Шелла: ")
print(shell(sp))
# print("Быстрая сортировка: ")
# print(quicksort(sp))