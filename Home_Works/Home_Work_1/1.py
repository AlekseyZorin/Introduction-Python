# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)


# number = int(input('Введите трёхачное число: '))

# if number > 99 and number < 1000:
#     num1 = number // 100
#     num2 = number // 10 % 10
#     num3 = number % 10
#     print(f'Сумма цифр вашего трёхзначного числа = {num1 + num2 + num3}')
# elif number < -99 and number > -1000:
#     number *= -1
#     num1 = number // 100
#     num2 = number // 10 % 10
#     num3 = number % 10
#     print(f'Сумма цифр вашего трёхзначного числа = {num1 + num2 + num3}')
# else:
#     print('Ваше число не трёхзначное')




# Либо с помощью строки

# number = input('Введите трёхачное число: ')

# if number.isdigit() and len(number) == 3: # проверка на то что все символы это цифры и что длина равна 3 символам(трехзначное число)
#     print(f'Сумма цифр вашего трёхзначного числа = {int(number[0])+ int(number[1])+ int(number[2])}')
# else:
#     print('Ваше число не трёхзначное')

