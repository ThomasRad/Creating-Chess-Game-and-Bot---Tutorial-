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
        
        """

        Takes a move as a parameter and executes it. 

        """

    
    def makemove(self,move):
        self.board[move.startrow][move.startcol] = "--"
        self.board[move.endrow][move.endcol] = move.piecemoved
        self.movelog.append(move)
        self.whitetomove = not self.whitetomove

        """ 
        We want to create an undo move as well.
        """

    def undomove(self):
        if len(self.movelog) != 0:
            move = self.movelog.pop()
            self.board[move.startrow][move.startcol] = move.piecemoved
            self.board[move.endrow][move.endcol] = move.piececaptured
            self.whitetomove = not self.whitetomove 
    
    """
    Bascailly what moves your are legally allowed to do 
    """

    def getvalidmoves(self):
        return self.getallpossiblemoves()

    """
    This just looks at all moves, doesn't care about legal moves such as causing you to lose by checks. 
    """

    def getallpossiblemoves(self):
        
        # Loop over the whole board and scan for pieces 

        moves = [move((6,4),(4,4),self.board)]
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):

                # use the first index to determine which color 

                turn = self.board[r][c][0]

                # See if the piece is White or Black and do the following then. 

                if (turn == "w" and self.whitetomove) & (turn == "b" and not self.whitetomove):
                    piece = self.board[r][c][1]

                    # codifing for specific pieces 

                    if piece == "p":
                        self.getpawnmoves(r,c,moves)
                    
                    elif piece == "R":
                        self.getrookmoves(r,c,moves)

        return moves  
    

    # want to define moves for various pieces 

    def getpawnmoves(r,c,moves):
        pass

    def getrookmoves(r,c,moves):
        pass



        

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
        self.moveid = self.startrow * 1000 + self.startcol * 100 + self.endrow * 10 + self.endcol
        print(self.moveid)

    " Overriding = method"

    def __eq__(self, other):
        if isinstance(other,move):
            return self.moveid == other.moveid
        return False


    def getchessnotation(self):
        return self.getrankfile(self.startrow,self.startcol) + self.getrankfile(self.endrow, self.endcol)

    def getrankfile(self,r,c):
        return self.coltofiles[c] + self.rowstoranks[r]
        
        


