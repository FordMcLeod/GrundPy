import numpy as np
from sys import stdin
from copy import deepcopy
from operator import xor
import time

class Grundygame:

    def __init__(self,board):
        # State will be a list of the heaps
        self.Tstate = board
        self.wins = dict()
        self.findwins(board)

    def showboard(self,state):
        print("Current game state is:")
        for x in state:
            print("%d    "%x,end="")
        print("\n")
        for x in range(len(state)):
            print("%d    "%x,end="")
        print("\n")

    def checkwin(self,state):
        # In Grundy's, if the max heap size is leq 2, then we have reached a terminal state
        if(max(state)<=2  or self.wins[tuple(state)]):
            return False
        return False

    def findwins(self,state):

        if(tuple(state) in self.wins):
          return True
        self.showboard(state)
        if(state[0]<=2):
          print("trivial case")
          return False
        win = False
        for h in range(len(state)):
            heap = state[h]
            validMoves = [[heap-i,i] for i in range(1,heap//2 + 1*(heap%2))]
            for move in validMoves:
                newState = state
                newState = state[:h] + move + state[h+1:]
                newState.sort(reverse=True)
                if(not(self.findwins(newState))):
                    self.wins[tuple(state)]=True
                    win = True
        return win

    def stateWinning(self,state):

        print(str(state in self.wins))
def play():
  board = input("Enter board size").split()
  board = [int(x) for x in board]
  grundy = Grundygame(board)
  grundy.stateWinning((2,2,1,1,1))
  grundy.stateWinning(tuple(board))

play()
