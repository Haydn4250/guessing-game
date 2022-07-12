from colorama import Fore, init
import random

init()
attempt = 0
digit = 102
flag = Fore.GREEN + 'продолжить'

def is_valid(digital):
    if str(digital).isdigit():
        digital = int(digital)
        if 0 < digital < 101:
            return True
        else:
            return False
    else:
         return False

print(Fore.WHITE + 'Добро пожаловать в игру "угадайка", мы загадываем число (от 0 до 100 включительно), а ты угадываешь. \n Итак, поехали!')

while flag != 'закончить':
    num = random.randrange(101)
    
    while num != digit:
        print(Fore.WHITE + 'введите число: ', end='')
        digit = input()
        while is_valid(digit) == False:
            print('Введите правильное число(от 0 до 100 включительно!) ')
            print(Fore.WHITE + 'введите число: ', end='')
            digit = input()

        digit = int(digit)
        if num == digit:
            print(Fore.GREEN + 'Вы угадали, поздравляем!')
        elif num > digit:
            print(Fore.YELLOW + "Слишком мало, попробуйте еще раз")
        else:
            print(Fore.RED + 'Слишком много, попробуйте еще раз')
        attempt += 1
    
    print(Fore.WHITE + 'ваше количество попыток: ' + str(attempt))
    attempt = 0
    print(Fore.WHITE + 'продолжить или закончить?', end = '\n')
    flag = input()
    if flag == 'закончить':
        print(Fore.RED + 'заканчиваем')
    elif flag == 'продолжить':
        print(Fore.GREEN + 'продолжаем')
    else:
        print('ты дурак? \n У тебя 2 варианта ответа!')

