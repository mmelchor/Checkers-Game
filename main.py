from project import *

def main():
    player1 = input("Write Player 1 name: ")
    player2 = input("Write Player 2 name: ")
    board = CheckerBoard(str(player1), str(player2))
    board.Player1Piece()
    board.Player2Piece()
    while not board.isOver():
        print('Player 1 Turn')
        print('Click the piece you want to move')
        print('Then click the place where you want to move','\n')
        board.getcenter()
        print('Player 2 Turn')
        print('Click the piece you want to move')
        print('Then click the place where you want to move','\n')
        board.getcenter2()
        
        
                

main()
