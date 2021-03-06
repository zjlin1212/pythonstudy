#!/usr/bin/env python
#copyRight by heibanke


def drawBoard(board):    
    # "board" is a list of 10 strings representing the board (ignore index 0)
    blank_board = '|     '*3+'|'
    edge_board = '+-----'*3+'+'
    def drawLine(board_line):
        insert_sym = '|'
        print blank_board
        print "|%3s%3s%3s%3s%3s  |"%(board_line[0],insert_sym,board_line[1],insert_sym,board_line[2])
        print blank_board
        print edge_board
        
    print edge_board
    drawLine(board[7:10])
    drawLine(board[4:7])
    drawLine(board[1:4])

def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print 'use X or O?'
        letter = raw_input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def playerMove(board,letter):
    # Let the player type in his move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split():
        print 'Your next step? (1-9)'
        move = raw_input()
        try:
            if not isSpaceFree(board, int(move)):
                print 'It was occupied'%move
                move=''
                continue
        except:
            print 'please input the number(1-9)'
            continue
        
    board[int(move)] = letter 
    
    return isWinner(board,letter)
    
def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print 'Do you want to play again? (yes or no)'
    return raw_input().lower().startswith('y')


def isWinner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal


def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' ' or board[move] in '1 2 3 4 5 6 7 8 9'.split()


def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True





if __name__=="__main__":
    print 'welecome Tic Tac Toe!'

    while True:
        # Reset the board
        theBoard = '0 1 2 3 4 5 6 7 8 9'.split()
        player1Letter, player2Letter = inputPlayerLetter()
        Letter = (player1Letter, player2Letter)
        print u' ' +Letter[0] + 'First.'
        turn = 0
        gameIsPlaying = True

        while gameIsPlaying:
            
            # Player's turn.
            drawBoard(theBoard)
            current_letter = Letter[turn]
            
            print " it"+current_letter+" turn"
            
            if playerMove(theBoard,current_letter):
                drawBoard(theBoard)
                print current_letter+'wins'
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print 'Game over. Nobody wins'
                    break
                else:
                    turn = (turn+1)%2

        if not playAgain():
            break
