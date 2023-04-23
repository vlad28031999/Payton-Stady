# Дано натуральное число N и
# последовательность из N элементов. 
# Требуется вывести эту последовательность в обратном порядке.

def print_numbers(n):
    number = int(input(f"введите число #{n} "))
    if n > 1:
        print_numbers(n-1)
    print(number,end=" ")
n=int(input())
print_numbers(n)

