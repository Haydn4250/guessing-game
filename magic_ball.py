from random import choice
from colorama import Fore, init
init()

answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]

print(Fore.CYAN + 'Приветствую, я магический шар, и я знаю ответ на любой твой вопрос.')
print('Как имя твое, человек!?: ',Fore.WHITE, end = '')
name = input()
print(Fore.CYAN + 'Рад приветсвовать тебя, ', end='')
print(Fore.GREEN + name)

while 1 < 2:
    print(Fore.CYAN + 'Каков твой вопрос?', Fore.WHITE)
    question = input()
    print(Fore.GREEN, choice(answers))
    print(Fore.CYAN + 'У тебя еще есть вопрос?', Fore.WHITE)
    
    while 1 < 2:
        flag  = input()
        if flag.lower() == 'нет':
            print(Fore.RED + 'тогда прощай!')
            break
        elif flag.lower() == 'да':
            print(Fore.GREEN + 'отлично, тогда продолжаем!')
            break
        else:
            print(Fore.RED + 'Напиши только да или нет!')
    if flag == 'нет':
        break