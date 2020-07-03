"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None
pref_action=None


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
        for j in i:
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
    i,j = action
    if (result_board[i][j]!=EMPTY):
        raise Exception("Invalid Move")
    else:
        result_board[i][j]=move
    return result_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if ((board[0][0] == board[1][1]) and (board[1][1]==board[2][2]) and (board[0][0] != None)):
        return board[0][0]
    elif ((board[0][2] == board[1][1]) and (board[1][1]==board[2][0]) and (board[0][2] != None)):
        return board[0][2]
    
    for i in range (0,3):
        j=0
        if ((board[i][j]==board[i][j+1]) and (board[i][j+1]==board[i][j+2]) and (board[i][j] != None)):
            return board[i][j]
    
    for j in range (0,3):
        i=0
        if ((board[i][j]==board[i+1][j]) and (board[i+1][j]==board[i+2][j]) and (board[i][j] != None)):
            return board[i][j]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (winner(board) != None):
        return True
    for i in board:
        for j in i:
            if (j==EMPTY):
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if (terminal(board)):
        if (winner(board)==X):
            return 1
        elif (winner(board) == O):
            return -1
        else:
            return 0
    return None


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if(player(board)==X):
        maxvalue(board)
        print(pref_action)
        return pref_action
    else:
        minvalue(board)
        print(pref_action)
        return pref_action

def minvalue(board):
    if (terminal(board)):
        return utility(board)
    v = 99999999
    for actionss in actions(board):
        vc = maxvalue(result(board,actionss))
        if(v>=vc):
            v = vc
            global pref_action
            pref_action = actionss
    return v

def maxvalue(board):
    if (terminal(board)):
        return utility(board)
    v = -99999999
    for actionsss in actions(board):
        vc = minvalue(result(board,actionsss))
        if (v <= vc):
            v=vc
            global pref_action
            pref_action=actionsss
    return v