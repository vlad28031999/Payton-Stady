# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.

arrey_size=int(input("Введите размер первого массива: "))
array=list()
for i in range (arrey_size):
    temp=int(input(f"введите {i+1} элемент: "))
    array.append(temp)
resault=0
for i in range(len(array)):
    resault=resault+(array[i+1 :]).count(array[i])
print(resault)
            
