print('Добро пожаловать в игру крестики - нолики')
print('Введите "X", если будете играть крестиком и "0"(ноль), если будете играть ноликом: ', end='')
player1 = input() #первый игрок
#проверка условия за кого играет первый игрок и установка крестика или нолика(зависимо что выберет первый игрок) для второго игрока
if player1 == 'X':
    player2 = '0'
else:
    player2 = 'X'
print('Поехали!')

#отсюда нужно написать клеточную систему

board = list(range(1,10)) #доска сколько в ней позицый(сколько полей)


def draw_board(board): # схема доски из чего она состоит
    print('-'*13)
    for i in range(3):
        print('|', board[0+i*3], '|', board[1+i*3], '|', board[2+i*3], '|')# из чего состоит строчка в консоле ну что разделяет их
        print('-'*13) 






def take_input(player_token):# ввод пользователя
   valid = False
   while not valid:
      player_answer = input("Куда поставим " + player_token+"? ")# консоль спрашивает пользователя куда поставить х или y
      try:
         player_answer = int(player_answer)
      except:
         print("Некорректный ввод. Вы уверены, что ввели число?")
         continue
      if player_answer >= 1 and player_answer <= 9:# диапозон ввода
         if(str(board[player_answer-1]) not in "XO"):# проверка что ввёл пользователь
            board[player_answer-1] = player_token
            valid = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")


def main(board):
    counter = 0
    res = False
    while not res:
        draw_board(board)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        
    draw_board(board)
main(board)