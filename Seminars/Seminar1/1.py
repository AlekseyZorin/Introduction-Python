# Задача 1
# За день машина проезжает n километров.
# Сколько дней нужно, чтобы проехать маршрут длиной m километров?
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.

# day = int(input('Введите сколько км проехала машина за один день: '))
# total = int(input('Какой маршрут проехали в км: '))
# result = (day - 1 + total)// day
# print(f'Машина проедет {total} километров за {result} дней ')



# Задача 2
# В некоторой школе решили набрать три новых математических класса и
# оборудовать кабинеты для них новыми партами.
# За каждой партой может сидеть два учащихся.
# Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.


# class_1 = int(input("Введите количество учащихся в первом классе: "))
# class_2 = int(input("Введите количество учащихся во втором классе: "))
# class_3 = int(input("Введите количество учащихся в третьем классе: "))

# part_1 = (class_1 + 1) // 2
# print(f'Для первого класса нужно:  {part_1} парт')
# part_2 = (class_2 + 1) // 2
# print(f'Для второго класса нужно:  {part_2} парт')
# part_3 = (class_3 + 1) // 2
# print(f'Для третьего класса нужно:  {part_3} парт')

# print(f'Всего нужно {part_1 + part_2 + part_3} парт')

#либо 

# class_1 = int(input("Введите количество учащихся в первом классе: "))
# class_2 = int(input("Введите количество учащихся во втором классе: "))
# class_3 = int(input("Введите количество учащихся в третьем классе: "))

# print(f'Для классов надо закупить {(class_1//2 + class_1 % 2) + (class_2//2 + class_2 % 2) + (class_3//2 + class_3 % 2) }')



# Задача 3
# Вагоны в электричке пронумерованы натуральными числами, начиная с 1
# (при этом иногда вагоны нумеруются от «головы» поезда, а иногда – с «хвоста»;
#   это зависит от того, в какую сторону едет электричка).
# В каждом вагоне написан его номер.
# Витя сел в i-й вагон от головы поезда и обнаружил, что его вагон имеет номер j.
# Он хочет определить, сколько всего вагонов в электричке.
# Напишите программу, которая будет это делать или сообщать, что без дополнительной информации это сделать невозможно.

# i = int(input("В какой номер вагона сел Витя?: "))
# j = int(input("Какой номер вагона оказался после посадки?: "))

# if i == j:
#     print('Не достаточно данных для определения общего количества вагонов')
# else:
#     print(f'В поезде всего {i + j - 1} вагонов') 



# Задача 4
# Дано натуральное число. Требуется определить, является ли год с данным номером високосным.
# Если год является високосным, то выведите YES, иначе выведите NO.
# Напомним, что в соответствии с григорианским календарем, год является високосным,
# если его номер кратен 4, но не кратен 100, а также если он кратен 400.

# year = int(input("Введи год: "))

# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0: # and (приоритет умножения '*'), а or (приоритет сложения '+') 
#     print("Год високосный")
# else:
#     print("Год НЕ високосный")
