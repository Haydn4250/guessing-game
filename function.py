print('*' * 10, 'Крестики нолики', '*'*10)

board = list(range(1,10))


def drao_boad(board):
    print('-'*13)
    for i in range(3):
        print('|', board[0+i*3], '|', board[1+i*3], '|', board[2+i*3], '|')
        print('-'*13) 

drao_boad(board)