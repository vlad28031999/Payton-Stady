# Задача 28: Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.
# return sum(a, b) + 1 - такое использовать нельзя

# *Пример:*

# 2 2
#     4

def sum_num(num_a,num_b):
    if num_b == 0:
        return num_a
    else:
        return sum_num(num_a+1,num_b-1)

num_a = int(input('Введите число :'))
print()
num_b = int(input('Введите второе число: '))
print(f'Сумма чисел равна = {sum_num(num_a,num_b)}:')