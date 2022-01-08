"""

This Class will be responsible for determining both the state and valid moves for the current state. 
Keeps a move log,

"""

class GameState():
    def __init__(self):

        #Board is a 2x2 dim list, desinated by color and piece type.

        self.board = [
        ["bR","bN","bB","bQ","bK","bB","bN","bR"],
        ["bp","bp","bp","bp","bp","bp","bp","bp"],
        ["--","--","--","--","--","--","--","--"],
        ["--","--","--","--","--","--","--","--"],
        ["--","--","--","--","--","--","--","--"],
        ["--","--","--","--","--","--","--","--"],
        ["wp","wp","wp","wp","wp","wp","wp","wp"],
        ["wR","wN","wB","wQ","wK","wB","wN","wR"]
        ]

        self.whitetomove = True
        self.movelog = []
        
