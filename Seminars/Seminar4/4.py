# Задача №27
# Пользователь вводит текст(строка). 
# Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов. 
# Определите, сколько различных слов содержится в этом тексте. 
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells 
# I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells 
# Output: 13


# text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
# # text = "За косой-косой косой Косой, косой-косой косой-косой косой-косой косой Косой косой-косой косой-косой Косой косой-косой Косой луг косо косил"
# text = text.lower()
# print(text)

# my_list = text.split(' ')
# print(my_list)

# rez = set(my_list)
# print(rez)
# print(len(rez))


# Либо второй вариант

# str_split = input('Введите ваш текст: ').lower().split()

# str_cnt = {}

# for word in str_split:
#     str_cnt[word] = str_cnt.get(word, 0) + 1
# print(f'Число уникальных слов в вашем предложение равно: {len(str_cnt)}')
# print(str_cnt)


# Задача №25
# Напишите программу, которая принимает на вход строку, 
# и отслеживает, сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n. 
# Input: a a a b c a a d c d d 
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# text = 'a a a b c a a d c d d'.split()

# dicti = dict().fromkeys(text, 0)
# print(dicti)

# for simvol in text:
#     if dicti[simvol] == 0:
#         print(simvol, end = " ")
#     else:
#         print(f"{simvol}_{dicti[simvol]}", end = " ")
#     dicti[simvol] += 1


# Либо второй вариант решения

# string = "a a a b c a a d c d d".split()

# for i in range(len(string)):
#     print(f"{string[i]}_{string[0:i].count(string[i])}" if string[0:i].count(string[i]) != 0 else string[i], end=" ")



# Либо третий способ 


# stroka = input().split()

# result = {}

# for i in stroka:
#     if i in result:
#         print(f"{i}_{result[i]}", end=" ")
#     else:
#         print(i, end=" ")
#     result[i] = result.get(i, 0) + 1    


# Либо четвёртый способ


# text = list(input('Введите строку: '))

# rezult = dict()

# for simvol in text:
#     if simvol in rezult:
#         rezult[simvol] = rezult[simvol] + 1
#     else:
#         rezult[simvol] = 0
#     count_rezult = rezult[simvol]    
#     print(f'{simvol}_{count_rezult}' if count_rezult > 0 else simvol, end=' ')






