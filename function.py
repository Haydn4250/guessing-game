<<<<<<< HEAD
print('*' * 10, 'Крестики нолики', '*'*10)

board = list(range(1,10))


def draw_board(board):
    print('-'*13)
    for i in range(3):
        print('|', board[0+i*3], '|', board[1+i*3], '|', board[2+i*3], '|')
        print('-'*13) 

draw_board(board)
=======
def position(digit):
    x = digit // 10 #число обозначающее номер столбца
    y = digit % 10 #число обозначающее номер строки
    for i in range(1, 4):
        for j in range(1, 4):
            if x == i and y == j:
                return()   #возвращает название переменной в которую вставляется крестик или нолик
                
>>>>>>> 4449bd48e101e20e53a986a605ab59af7437b0fd
