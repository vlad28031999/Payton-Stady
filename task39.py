# Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут 
# в первом массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов 
# в первом массиве, затем N чисел - элементы массива. Затем число M - количество элементов во втором массиве. 
# Затем элементы второго массива


arrey_size=int(input("Введите размер первого массива: "))
array=list()
for i in range (arrey_size):
    temp=int(input(f"введите {i+1} элемент: "))
    array.append(temp)
arrey_size=int(input("Введите размер второго массива: "))
array_two=list()
for i in range (arrey_size):
    temp=int(input(f"введите {i+1} элемент: "))
    array_two.append(temp)
for i in range(len(array)):
    if not array[i] in array_two:
        print(array[i],end=", ")