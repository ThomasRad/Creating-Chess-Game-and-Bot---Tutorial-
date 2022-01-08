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

    def makemove(self,move):
        self.board[move.startrow][move.startcol] = "--"
        self.board[move.endrow][move.endcol] = move.piecemoved
        self.movelog.append(move)
        self.whitetomove = not self.whitetomove

class move():

    ranktorows = {"1":7,"2":6,"3":5,"4":4,"5":3,"6":2,"7":1,"8":0}
    rowstoranks = {v: k for k, v in ranktorows.items()}
    filestocol = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7}
    coltofiles = {v: k for k, v in filestocol.items()}

    def __init__(self,startsq, endsq, board):
        self.startrow = startsq[0]
        self.startcol = startsq[1]
        self.endrow = endsq[0]
        self.endcol = endsq[1]
        self.piecemoved = board[self.startrow][self.startcol]
        self.piececaptured = board[self.endrow][self.endcol]

    def getchessnotation(self):
        return self.getrankfile(self.startrow,self.startcol) + self.getrankfile(self.endrow, self.endcol)

    def getrankfile(self,r,c):
        return self.coltofiles[c] + self.rowstoranks[r]
        
        


