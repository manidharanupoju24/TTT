__author__ = 'Suraj'

from node import Node


class Tree():  # Tree structure
    def __init__(self):
        self.numberOfTurns = 0
        self.entries = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.leafNode = [1, 0, -1]

    def display(self):  # Prints the present board position
        print('\n %s | %s | %s' % (self.entries[0], self.entries[1], self.entries[2]))
        print('---|---|---')
        print(' %s | %s | %s' % (self.entries[3], self.entries[4], self.entries[5]))
        print('---|---|---')
        print(' %s | %s | %s\n' % (self.entries[6], self.entries[7], self.entries[8]))

    def userTurn(self):
        userInput = input('Your(X) turn to play:\t')
        self.entries[int(userInput[0]) - 1] = userInput[2]
        self.numberOfTurns += 1
        return self.entries

    def traversal(self):
        tree = Tree()
        root = tree.userTurn()
        board = Node(root)
        while board.value not in self.leafNode:
            nextBoard = tree.generateNextBoard(board)
            board.add(nextBoard)
            board = nextBoard
            self.numberOfTurns = + 1

    def generateNextBoard(self, board):
        for i in range(10):
            if self.numberOfTurns % 2 == 0 & board[i] == ' ':
                board[i] = 'O'
                break
            elif board[i] == ' ':
                board[i] = 'X'
                break
        return board
