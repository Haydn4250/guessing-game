from random import choice
from colorama import Fore, init
init()

#функция проверяющая правильность длины пароля
def wrong_len_password(lenght):
    while True:
        lenght = input()
        if lenght.isdigit() == False:
            print(Fore.CYAN + 'введи число!', Fore.WHITE)
        else:
            lenght = int(lenght)
            return lenght

#функция генерации пароля
def generate_password(lenght, chars):
    password = ''
    for _ in range(lenght):
        password += choice(chars)
    return password

#функция проверки ответа
def wrong_answer():
    while True:
        flag = input()
        if flag == 'да':
            return True
        if flag == 'нет':
            return False
        else:
            print(Fore.CYAN + 'ответь только "да" или "нет"!')

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
flag = ''
lenght = ''
print(Fore.CYAN + 'привет, я программа генерирующая рандомный пароль!', 'введи длину предпологаемого пароля', sep ='\n')
lenght = wrong_len_password(lenght)

#функция проверяющая наличие условий пароля
while True:
    #цифры в пароле
    print(Fore.CYAN + 'Нужны ли цифры в твоем пароле?')
    if wrong_answer() == True:
        chars += choice(digits)
    #буквы нижнего регистра в пароле
    print('Нужны ли буквы нижнего регистра в твоем паролле?')
    if wrong_answer() == True:
        chars += choice(lowercase_letters)
    #буквы верхнего регистра в пароле
    print('Нужны ли буквы верхнего регистра в твоем пароле?')
    if wrong_answer() == True:
        chars += choice(uppercase_letters)
    #пунктационные знаки
    print('Нужны ли пунктационные знаки в твоем пароле?')
    if wrong_answer() == True:
        chars += choice(punctuation)
    #неоднозначные символы: il1Lo0O 
    print('Исключать ли неоднозначные символы, такие как: il1Lo0O ?')
    if wrong_answer() == True:
        for c in chars:
            if c in 'il1Lo0O':
                chars = chars.replace(c, '')
    
    if len(chars) == 0:
        print('вы точно уверены, что пароль вам нужен?')
        if wrong_answer() == True:
            print('Тогда давайте выбирем параметры пароля сначала!')
            chars = ''
        else:
            print('тогда пока!')
            break
        
    elif len(chars) == 1:
        print('не бывает пароля из одного знака', 'Начнем сначала?', sep='\n')
        if wrong_answer() == True:
            print('Тогда давайте выбирем параметры пароля сначала!')
            chars = ''
        else:
            print('тогда пока!')
            break

    elif len(chars) == 2:
        print('лучше добавьте еще 1 параметр для безопасности', 'начнем сначала?', sep='\n')
        if wrong_answer() == True:
            print('Тогда давайте выбирем параметры пароля сначала!')
            chars = ''
        else:
            print('как пожелаете!')
            print('Ваш пароль:')
            print(generate_password(lenght, chars))
            break
    else:
        print('Ваш пароль:')
        print(generate_password(lenght, chars))
        break
input()





