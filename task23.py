# Напишите функцию, которая принимает одно число и проверяет,
# является ли оно простым
# *Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n
# (само число)*

# Хакер Василий получил доступ к классному журналу 
# и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия,
# но наоборот: все максимальные – на минимальные.


# 1 5 2 1 5 4

# 1 1 2 1 1 4

grades = input().split() 
grades = list(map(int, grades))
min_grade = min(grades) 
max_grade = max(grades)
for i in range(len(grades)):
    if grades[i] == max_grade:
        grades[i] = min_grade

print(' '.join(map(str, grades)))
