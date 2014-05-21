#!/bin/python2.7
# codecademy - Python
# Battleship - Simple One Player

from random import randint					# Import random number generator

board = []									# Set empty board

for x in range(5):							# For range 0 - 4 (0 - 5 not including 5)
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)					# Join elements of board; separate with " " rather than commas and quotes

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)		# This allos for different board sizes rathe than radinit(0, 5)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(4):
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Collumn:"))

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
        print "Game Over"
    board[guess_row][guess_col] = "X"
    print (turn + 1)
    if turn == 3:
        print "Game Over"
    print_board(board)