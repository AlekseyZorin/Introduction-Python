# Задача 16
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
#   5
#     1 2 3 4 5
#     3
#     -> 1

import random

# n = int(input('Ведите длину списка: '))
n = 10

my_list_A = []
count = 0 

# x = int(input('Введите число которое хотите найти: '))
x = 5

for i in range(n):
    my_list_A.append(random.randint(0, 10))
    if my_list_A[i] == x:
        count += 1
print(my_list_A)
print(f'Ваше число {x} встречается в списке {count} раз')

