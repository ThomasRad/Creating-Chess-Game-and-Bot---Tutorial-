import ChessE
import pygame as p


width = height = 512
dimension = 8 
square_size = height // dimension
max_fps = 15
images = {}

"""
Global dictonary of images. Will be called just once.
"""


def load_images():
    
    pieces = ["wp", "wR", "wN","wB","wK","wQ","bp", "bR", "bN","bB","bK","bQ"]
    for piece in pieces:
        images[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"),(square_size,square_size))

"""
This will handle user input and updating graphics 
"""

def main():
    p.init()
    screen = p.display.set_mode((width,height))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessE.GameState()
    load_images()
    
    running = True

    #Keeps track of last click 
    sqselected = ()
    
    # Keep track of the clicks 
    playerclicks = []

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                
                # This gets the location x and y 
                location = p.mouse.get_pos()
                col = location[0]//square_size
                row = location[1]//square_size

                #Check to see if already clicked the same square
                if sqselected == (row,col):

                    #Unselect it here 
                    sqselected = ()

                    # Also reset the player clicks too. 
                    playerclicks = []

                else: 
                    sqselected = (row,col)
                    playerclicks.append(sqselected)

                # Telling the system to move the piece 

                if len(playerclicks) == 2:
                    move = ChessE.move(playerclicks[0],playerclicks[1],gs.board)
                    print(move.getchessnotation())
                    gs.makemove(move)
                    
                    #Reset playclicks and selected
                    playerclicks = []
                    sqselected = ()


        drawGamestate(screen,gs)
        clock.tick(max_fps)
        p.display.flip()

    print(gs.board)

def drawGamestate(screen,gs):
    drawboard(screen)
    drawpieces(screen,gs.board)



def drawboard(screen):
    colors = [p.Color("white"),p.Color('grey')]
    for r in range(dimension):
        for c in range(dimension):
            color = colors[((r+c) % 2)]
            p.draw.rect(screen,color,p.Rect(c*square_size,r*square_size,square_size,square_size))


def drawpieces(screen,board):
    for r in range(dimension):
        for c in range(dimension):
            piece = board[r][c]
            if piece != "--":
                screen.blit(images[piece], p.Rect(c*square_size,r*square_size,square_size,square_size))


if __name__ == "__main__":
    main()
