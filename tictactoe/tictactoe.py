"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countx=0;
    counto=0;
    for i in board:
        for j in i:
            if (j==X):
                countx=countx+1
            elif (j==O):
                counto=counto+1
    if (countx>counto):
        return O
    elif (countx==counto):
        return X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    act = set()
    row=0
    for i in board:
        column=0
        for j in board:
            if (j==EMPTY):
                act.add((row,column))
            column=column+1
        row=row+1
    return act


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    move = player(board)
    result_board = copy.deepcopy(board)
    for i,j in action:
        if (result_board[i][j]!=EMPTY):
            raise Exception("Invalid Move")
        else:
            result_board[i][j]=move
    return result_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
