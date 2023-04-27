# Задача 26
# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8 

num = int(input('Введи число которое хотите возвести в степень: '))
degree = int(input('Введи число степени в которую хотите возвести: '))

def degree_of_number(num, degree):
    return 1 if degree < 1 else degree_of_number(num, degree - 1) * num

print(degree_of_number(num, degree))
