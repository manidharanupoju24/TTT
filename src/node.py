__author__ = 'Suraj'
class Node():
    def __init__(self, board):
        self.board = board
        self.children = []
        self.parent = None
        self.value = None

    def parent(self):
        return self.parent

    def add(self, board):
        node1 = Node(board)
        self.children.append(node1)
        node1.parent = self
        return node1

