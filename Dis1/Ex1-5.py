# 1 - Задайте натуральное число N. Напишите 
# программу, которая составит список простых 
# множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]


import sympy

def multi(n):
    '''функция сначала находит
     простые числа в пределах заданного числа с помощью
     sympy
    и далее находит среди них список
     множетелей заданного числа'''
    list2 =list(sympy.primerange(0, n+1))
    
    multi_list = []
    for i in list2:
        if n%i ==0:
            multi_list.append(i)
    return(multi_list)


print(multi(int(input('Введите натуральное число '))))



# 2 - Задайте последовательность чисел. 
# Напишите программу, которая выведет 
# список неповторяющихся элементов исходной
#  последовательности. Не использовать множества.
# Постарайтесь решить за одно условие
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

first_list = [1,1,1,1,2,2,2,3,3,3,4]

'''функция принимает ма'''

def unique_num_list(arr):
    '''функция принимает список цифр и убирает из 
    него все повторы, путем создания нового списка
    и добавления в него уникальных символов'''
    new_arr = []
    for i in arr:
            if i not in new_arr:
                    new_arr.append(i)
    return (new_arr)
print(unique_num_list(first_list))



# 3 - В файле, содержащем фамилии студентов и их оценки,
#  изменить на буквы в верхнем регистре тех студентов, 
# которые имеют средний балл более «4».
# Нужно перезаписать файл.
# Пример:
# Ангела Меркель 5
# Энакин Скайуокер 5
# Фредди Меркури 3
# Александр Пушкин 4

# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# ЭНАКИН СКАЙУОКЕР 5
# Фредди Меркури 3
# Александр Пушкин 4


from typing import List

def upper_case(file: List[str], accept:str) -> str:
    '''функция принимает список строк и меняет буквы в
    опредленных строках на прописные буквы, если мы видим
    определенную оценку (число) после строки'''

    file_new = ""
    for name in file:
        if name.count(accept):
            name = name.upper()
        string = name +'\n'
        file_new +=string
    return file_new


with open ('student.txt', 'w') as file_new:
    file_new.write('Angela Merkel 5\n')
    file_new.write('Enakin Sky 5\n')
    file_new.write('Freddy Merq 3\n')
    file_new.write('Sasha Pushkin 4\n')

with open ('student.txt', 'r') as file_new:
    line = file_new.read().split('\n')

upper_file = upper_case(line, accept='5')

with open ('student.txt', 'w') as file_new:
    file_new.write(upper_file)

#Задачу частично подглядела на семинаре. Оказывается каждое 
#действие с файлом нужно делать, заново открывая файл
#я пыталась все в одном сделать и не получалось

# 4- Шифр Цезаря - это способ шифрования, где каждая буква
#  смещается на определенное количество символов влево 
# или вправо. 
# При расшифровке происходит обратная операция.
# К примеру, слово "абба" можно зашифровать 
# "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, 
# "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает
#  в файл шифрованный текст, а также функцию, которая 
#  спрашивает ключ, считывает текст и дешифровывает его.
# abc = 'abcdefghijklmnopqrstuvwxyz'  


def code_text(file: str, shift: int):
    '''эта функция принимает тест на латинице и шифрует
     его с помощью шифра Цезаря. Можно сделать для русского текста,
     но нужны другие числа и диапазоны из таблицы ASCIl'''

    new_text = []
    new_simbol = ''
    for i in file:
        if ord(i)>=65 and ord(i) <= 90:
            new_simbol = chr((((ord(i)-65)+shift)%26)+65)
            new_text.append(new_simbol)
        elif ord(i)>=97 and ord(i)<=122:
            new_simbol = chr((((ord(i)-97)+shift)%26)+97)
            new_text.append(new_simbol)
        else:
            new_text.append(i)
        
    return ''.join(new_text)

def decode_text(file: str, shift: int):

    new_text = []
    new_simbol = ''
    for i in file:
        if ord(i)<=65 and ord(i) >= 90:
            new_simbol = chr((((ord(i)-65)-shift)%26)+65)
            new_text.append(new_simbol)
        elif ord(i)<=97 and ord(i)>=122:
            new_simbol = chr((((ord(i)-97)-shift)%26)+97)
            new_text.append(new_simbol)
        else:
            new_text.append(i)
        
    return ''.join(new_text)
 


with open ('code.txt', 'w') as new_text:
    new_text.write('hello rediska! how are you?\n')

with open ('code.txt', 'r') as new_text:
    file_code = new_text.read()

code_file = code_text(file_code, shift=2)

with open ('code.txt', 'a') as new_text:
    
    new_text.write(code_file)


decode_file = decode_text(file_code, shift=2)

with open ('code.txt', 'a') as new_text:
    
    new_text.write(decode_file)



# 5 - Реализуйте RLE алгоритм: реализуйте модуль
#  сжатия и восстановления данных. Входные и
#  выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG 
# python is sooooooo coooooool
# файл второй:
# 12A11B10C6D5E4FG python is s7o c7ol
# Первая функция - текст зашифровывает
# Вторая - расшифровывает
# Две промежуточные - считывают с файла и записывают в файл
from collections import Counter
import re

def compress(file: str):
    file_comp = list(file)
    new = str(dict(Counter(file_comp)))
    return new

# def delete(file):
#     reg = compress(file)
#     reg = re.sub(r'[\W_]+', '', file)
#     return reg

with open ('copmr.txt', 'w') as new_compr:
    new_compr.write('AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG?\n')

with open ('copmr.txt', 'r') as new_compr:
    file_compr = new_compr.read()


code_del = compress(file_compr)

with open ('copmr.txt', 'a') as new_compr:
    
    new_compr.write(code_del)



#знаю, что неправильно сделала, но пока не нашла хороший способ , 
# чтобы сделать эту задачу

    

