# Задача №31
# Последовательностью Фибоначчи называется последовательность чисел 
# a0 , a1 , ..., an , ..., где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи 
# Input: 7 
# Output: 21

# n = int(input('Введи номер числа Фибоначи который хотите узнать: '))

# def Fib(n):
#     if n in (0, 1):
#         return 1
#     return Fib(n - 1) + Fib(n - 2)
# print(Fib(n))







# # Задача по нахождению факториала с помощью рекурсии

# n = int(input('Введи число факториала который хотите узнать: '))

# def Factory(n):
#     if n < 1:
#         return 1
#     return n * Factory(n-1)
# print(Factory(n))






# Задача №33
# Хакер Василий получил доступ к классному журналу
# и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: 
# все максимальные – на минимальные. 
# Input: 5 -> 1 3 3 3 4 
# Output: 1 3 3 3 1

# Способ с помощью рекурсии 

# import random

# n = int(input('Введи количество оценнок в журнале: '))
# grades = [random.randint(1, 5) for _ in range(n)] # список оценок
# print(grades)
# min_grade = min(grades) # наименьшая оценка
# max_grade = max(grades) # наибольшая оценка

# def replace_max_grades(grades, max_grade, min_grade, i=0):
#     if i == len(grades): # базовый случай - если дошли до конца списка оценок
#         return grades
#     if grades[i] == max_grade:  # если текущая оценка является максимальной, заменяем ее на минимальную
#         grades[i] = min_grade
#     return replace_max_grades(grades, max_grade, min_grade, i+1) # рекурсивно вызываем функцию для следующей оценки в списке


# new_grades = replace_max_grades(grades, max_grade, min_grade) # заменяем максимальные оценки на минимальные
# print(new_grades) # выводим измененные оценки



# Способ с помощью цикла 

# import random

# n = int(input('Введи количество оценнок в журнале: '))
# log = [random.randint(1, 5) for _ in range(n)]
# print(log)

# min_gredes = min(log)
# max_gredes = max(log)

# for i in range(len(log)):
#     if log[i] == max_gredes:
#         log[i] = min_gredes

# print(log)










# Задача №35
# Напишите функцию, которая принимает одно число и проверяет, 
# является ли оно простым Напоминание: 
# Простое число - это число, которое имеет 2 делителя: 1  и n(само число) 
# Input: 5 
# Output: yes


# Нахождение с помощью рекурсии

# n = int(input('Введи число для проверки: '))

# def easy(n, i = 2):
#     if n <= 2: return True if n == 2 else False
#     if n % i == 0: return False
#     if i * i > n: return True
#     return Easy(n, i + 1)
# print(Easy(n))



# Нахождение с помощью цикла 

# def is_simple(num: int) -> bool:
#     if num in [1, 2]:
#         return True
#     elif num % 2 == 0:
#         return False
#     else:
#         for i in range(3, num // 2 + 1, 2):
#             if num % i == 0:
#                 return False
#     return True

# num = int(input('Введите число: '))
# print(is_simple(num))







# Задача №37
# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы 
# (даже для ввода и вывода). 
# Input:    2 -> 3 4 
# Output: 4 3


# n = int(input('Введи размер последовательности: '))

# def revers(n):
#     if n == 0:
#         return ""
#     i = input('Введи число: ')
#     return revers(n-1) + i          # А чтобы вывести в порядке ввода надо поменять i + Revers(n-1) местами

# print(revers(n))


# Либо

# num = int(input('Введи размер последовательности: '))

# def reverse_sequence(num):
#     if num == 1:
#         return num
#     else:
#         return f'{num} {reverse_sequence(num-1)}'

# print(reverse_sequence(num))








