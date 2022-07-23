def draw_board():
    board = list(range(1,10))
    print('-'*13)
    for i in range(3):
        print('|', board[0+i*3], '|', board[1+i*3], '|', board[2+i*3], '|')
        print('-'*13) 

def position(digit):
    x = digit // 10 #число обозначающее номер столбца
    y = digit % 10 #число обозначающее номер строки
    for i in range(1, 4):
        for j in range(1, 4):
            if x == i and y == j:
                return()   #возвращает название переменной в которую вставляется крестик или нолик
                
def take_input(player_token):# ввод пользователя
   board = list(range(1,10))
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
    board = list(range(1,10))
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
