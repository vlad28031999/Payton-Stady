# Задача 16: Требуется вычислить, сколько раз встречается 
# некоторое число X в массиве A[N]. 
# Пользователь в первой строке вводит натуральное число N – 
# количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X 
# Ввод: 5
# Ввод: 3 2 3 7 5
# Ввод: 3
# -> 2


import random
N = int(input())
lst = map(int, (input().split()))
x = int(input())
print(min(lst, key=lambda a:abs(a-x)))
array = [random.randint(a, b) for i in range(n)]
print(array)
for i in (array):
    if i == x:
    count+=1
print(f'Число {x} найдено {count} раза!')
